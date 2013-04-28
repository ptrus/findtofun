from djcelery import celery
from facepy import GraphAPI
from events.models import FbEvent, FbUser, FbLocation
import time


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
		 AND start_time > now()
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
				# update event
			except FbEvent.DoesNotExist:
				print event_data
				event = FbEvent.objects.create_event(**event_data)
				events_objects.append(event)

	location_objects = []
	for event in events_objects:
		if (event.venue is not None and
				event.venue not in location_objects):
			location_objects.append(event.venue)

	FbLocation.objects.bulk_create(location_objects)
	FbEvent.objects.bulk_create(events_objects)

	for eid in eids:
		process_users_in_events.delay(access_token, eid)
		time.sleep(3)


@celery.task
def process_users_in_events(access_token, eid):
	graph = GraphAPI(access_token)
	query_users = ("""
		SELECT
		 uid,
		 age_range,
		 current_address,
		 sex
		 FROM user

		 WHERE uid IN
			 (SELECT uid FROM event_member WHERE eid = %s)
		""") % (eid)

	users_results = graph.fql(query_users)
	ThroughModel = FbEvent.users.through
	users_objects = []
	through_objects = []
	location_objects = []

	for user_data in users_results["data"]:
		uid = user_data['uid']

		try:
			user = FbUser.objects.get(pk=uid)
			# update user
		except FbUser.DoesNotExist:
			print user_data
			user = FbUser.objects.create_user(**user_data)
			users_objects.append(user)
			if (user.current_address is not None and
					user.current_address not in location_objects):
				location_objects.append(user.current_address)

		through_props = dict(
			fbevent_id=eid,
			fbuser_id=uid)

		if ThroughModel.objects.filter(**through_props).exists() is False:
			through_objects.append(ThroughModel(**through_props))

	FbLocation.objects.bulk_create(location_objects)
	FbUser.objects.bulk_create(users_objects)
	ThroughModel.objects.bulk_create(through_objects)
