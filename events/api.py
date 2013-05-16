# myapp/api.py
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authentication import SessionAuthentication

from events.models import FbEvent, FbLocation, FbUser, FbEventFbUser


class FbLocationResource(ModelResource):
		class Meta:
				queryset = FbLocation.objects.all()
				resource_name = 'fblocation'
				authentication = SessionAuthentication()


class FbUserResource(ModelResource):
		class Meta:
				queryset = FbUser.objects.all()
				resource_name = 'fbuser'
				authentication = SessionAuthentication()


class FbEventFbUserResource(ModelResource):
		fbuser = fields.ToOneField(FbUserResource, 'fbuser', full=True)

		class Meta:
				queryset = FbEventFbUser.objects.all()
				authentication = SessionAuthentication()


class FbEventResource(ModelResource):
		venue = fields.ForeignKey(FbLocationResource, 'venue', full=True,
				null=True)

		class Meta:
				queryset = FbEvent.objects.all()
				resource_name = 'fbevents'
				allowed_methods = ['get']
				# fields = [
				# 	'attending_count',
				# 	'declined_count',
				# 	'pic_square'
				# 	'start_time',
				# 	'unsure_count']

		def dehydrate(self, bundle):
				event = bundle.obj
				bundle.data['name'] = event.common.name
				if event.pic_cover is not None:
					bundle.data['pic_cover_source'] = event.pic_cover.source

				males = dict(
					all_members = event.users.filter(sex="male").count())
				females = dict(
					all_members = event.users.filter(sex="female").count())
				for rsvp_status in ["attending", "unsure", "declined", "not_replied"]:
					tmp = FbEventFbUser.objects.filter(
							fbevent=event,
							rsvp_status=rsvp_status).count()
					males[rsvp_status] = FbEventFbUser.objects.filter(
							fbevent=event,
							rsvp_status=rsvp_status,
							fbuser__sex="male").count()
					females[rsvp_status] = tmp - males[rsvp_status]

				bundle.data['males'] = males
				bundle.data['females'] = females
				return bundle


# class FbEventDetailsResource(ModelResource):
# 		venue = fields.ForeignKey(FbLocationResource, 'venue', full=True,
# 				null=True)

# 		users = fields.ToManyField(FbEventFbUserResource,
#       attribute=lambda bundle: bundle.obj.users.through.objects.filter(
#           fbevent=bundle.obj), full=True)

# 		class Meta:
# 				queryset = FbEvent.objects.all()
# 				resource_name = 'fbeventdetails'
# 				allowed_methods = ['get']

# 		def dehydrate(self, bundle):
# 				event = bundle.obj
# 				common = event.common
# 				bundle.data['name'] = common.name
# 				return bundle
