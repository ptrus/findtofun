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
				bundle.data['males'] = event.users.filter(sex="male").count()
				bundle.data['females'] = event.users.filter(sex="female").count()
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
