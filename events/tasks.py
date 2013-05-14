from djcelery import celery
from celery.utils.log import get_task_logger

from facepy import GraphAPI
from events.models import FbEvent, FbUser

# from copy import deepcopy

logger = get_task_logger(__name__)


@celery.task
def process_events(access_token):
	graph = GraphAPI(access_token)
	query_events = """
		SELECT
			 all_members_count,
			 attending_count,
			 creator,
			 declined_count,
			 description,
			 eid,
			 end_time,
			 name,
			 not_replied_count,
			 pic,
			 pic_big,
			 pic_cover,
			 pic_small,
			 pic_square,
			 privacy,
			 start_time,
			 ticket_uri,
			 timezone,
			 unsure_count,
			 venue
			 FROM event

		 WHERE eid IN (SELECT eid FROM event_member WHERE
			 (uid = me() OR
				 uid IN (SELECT uid2 FROM friend WHERE uid1 = me())))
		 AND start_time > now() LIMIT 20
		"""

	events_results = graph.fql(query_events)
	events_objects = []
	eids = []

	for event_data in events_results["data"]:
		eid = event_data["eid"]
		if eid in eids:
			continue
		else:
			eids.append(eid)
			try:
				event = FbEvent.objects.get(pk=eid)
				update_event.s(args=(event, event_data))
			except FbEvent.DoesNotExist:
				log_event("CREATED", event_data)
				event = FbEvent.objects.create_event(**event_data)
				events_objects.append(event)

	FbEvent.objects.bulk_create(events_objects)
	for eid in eids:
		# process_users_in_events.delay(access_token, eid)
		process_users_in_events(access_token, eid)


def get_query_for_querying_users(eid, rsvp_status):
	return ("""
		SELECT
		 uid,
		 name,
		 age_range,
		 current_address,
		 sex
		 FROM user

		 WHERE uid IN
			 (SELECT uid FROM event_member WHERE eid = %s AND rsvp_status = '%s')
		""") % (eid, rsvp_status)

@celery.task
def process_users_in_events(access_token, eid):
	graph = GraphAPI(access_token)
	for rsvp_status in ["attending", "unsure", "declined", "not_replied"]:
		process_users_in_events_by_rsvp_status(
			graph,
			eid,
			get_query_for_querying_users(eid, rsvp_status),
			rsvp_status)


def process_users_in_events_by_rsvp_status(graph, eid, query_users,
		rsvp_status):
	users_results = graph.fql(query_users)
	ThroughModel = FbEvent.users.through
	users_objects = []
	through_objects = []

	for user_data in users_results["data"]:
		uid = user_data['uid']

		try:
			user = FbUser.objects.get(pk=uid)
			update_user.s(args=(user, user_data))
		except FbUser.DoesNotExist:
			log_user("CREATED", user_data)
			user = FbUser.objects.create_user(**user_data)
			users_objects.append(user)

		through_props = dict(
			fbevent_id=eid,
			fbuser_id=uid,
			rsvp_status=rsvp_status)

		if ThroughModel.objects.filter(**through_props).exists() is False:
			through_objects.append(ThroughModel(**through_props))


	FbUser.objects.bulk_create(users_objects)
	ThroughModel.objects.bulk_create(through_objects)
	# return dict(
	# 	users_objects=users_objects,
	# 	through_objects=through_objects
	# )

@celery.task
def update_event(event, event_data):
	has_changed = FbEvent.objects.update_event(event, **event_data)
	if has_changed:
		log_event("UPDATED", event_data)


@celery.task
def update_user(user, user_data):
	has_changed = FbUser.objects.update_user(user, **user_data)
	if has_changed:
		log_user("UPDATED", user_data)


def log_event(title, event_data):
	logger.info("%s event: %s, %s" % (
		title,
		event_data.get("eid", ""),
		event_data.get("name", "")))

def log_user(title, user_data):
	logger.info("%s user: %s" % (title, user_data))
