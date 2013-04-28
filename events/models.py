from django.db import models

F_MAX_LENGTH = 200


class Ticket(models.Model):

    def __unicode__(self):
        return "Ticket"


class Event(models.Model):
    EVENT_RATE = (
        (u'1', u'Not interesting'),
        (u'2', u'Not bad'),
        (u'3', u'Interesting'),
        (u'4', u'Tempting'),
        (u'5', u'You can not miss'),
    )

    name = models.CharField(max_length=F_MAX_LENGTH)
    location = models.CharField(max_length=F_MAX_LENGTH)
    rated = models.CharField(choices=EVENT_RATE, max_length=F_MAX_LENGTH)

    def __unicode__(self):
        return u'%s' % (self.name)


def get_modified_stuff(dict1, dict2):
    modified = {}
    for key, value in dict2.items():
        if value is not dict1[key]:
            modified[key] = dict2[key]

    return modified


def process_modified_stuff(model_instance, keys, data):
    dict1 = {}
    for key in keys:
        value = getattr(model_instance, key)
        dict1[key] = value

    modified = get_modified_stuff(dict1, data)
    for key, value in modified.items():
        setattr(model_instance, key, value)

    model_instance.save(update_fields=modified.keys())
    return modified.keys()

class FbUserManager(models.Manager):
    def create_user(self, **kwargs):

        if "current_address" in kwargs:
            current_address = kwargs.pop("current_address")
            if current_address is not None:
                location = FbLocation.objects.get_or_create(
                    city=current_address)
                kwargs["current_address"] = location

        if "age_range" in kwargs:
            age_range = kwargs.pop("age_range")
            if age_range is not None:
                kwargs["age_range_min"] = age_range.get("min", 0)
                kwargs["age_range_max"] = age_range.get("max", 0)

        return self.model(**kwargs)

    def update_user(self, user, **user_data):
        keys = self.model._meta.get_all_field_names()
        # Deletion needed, otherwise if throws error:
        #   AttributeError: 'FbUser' object has no attribute 'fbevent'
        del keys[keys.index("fbevent")]
        return process_modified_stuff(user, keys, user_data)


class FbEventManager(models.Manager):
    def create_event(self, **kwargs):

        name = kwargs.pop("name")
        common = Event.objects.create(name=name)
        kwargs["common"] = common

        venue = kwargs.pop("venue")
        if type(venue) is dict:
            try:
                venue_obj = FbLocation.objects.get(**venue)
            except FbLocation.DoesNotExist:
                venue_obj = FbLocation.objects.create_location(**venue)
            kwargs["venue"] = venue_obj

        creator_id = kwargs.pop("creator")
        try:
            creator = FbUser.objects.get(pk=creator_id)
        except FbUser.DoesNotExist:
            creator = FbUser.objects.create_user(pk=creator_id)
        kwargs["creator"] = creator

        if kwargs["ticket_uri"] is None:
            kwargs["ticket_uri"] = ""

        if kwargs["timezone"] is None:
            kwargs["timezone"] = ""

        if kwargs["privacy"] is None:
            kwargs["privacy"] = ""

        return self.model(**kwargs)

    def update_event(self, event, **event_data):
        keys = self.model._meta.get_all_field_names()
        # Deletion needed, otherwise if throws error:
        #   AttributeError: 'FbUser' object has no attribute 'fbevent'
        # del keys[keys.index("fbevent")]
        return process_modified_stuff(event, keys, event_data)


class FbLocationManager(models.Manager):
    def create_location(self, **kwargs):
        return self.model(**kwargs)


class FbUser(models.Model):
    uid = models.BigIntegerField(primary_key=True)
    age_range_min = models.PositiveSmallIntegerField(default=0)
    age_range_max = models.PositiveSmallIntegerField(default=0)
    current_address = models.ForeignKey('FbLocation', null=True)
    sex = models.CharField(max_length=F_MAX_LENGTH)
    objects = FbUserManager()


class FbLocation(models.Model):
    street = models.TextField(blank=True, default="")
    city = models.TextField()
    state = models.TextField(blank=True)
    country = models.TextField(blank=True)
    zip = models.CharField(max_length=F_MAX_LENGTH)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    l_id = models.PositiveIntegerField(null=True)
    name = models.TextField(blank=True)
    located_in = models.PositiveIntegerField(null=True)
    objects = FbLocationManager()


class FbEvent(models.Model):
    common = models.OneToOneField(Event, null=True)
    all_members_count = models.PositiveIntegerField()
    attending_count = models.PositiveIntegerField()
    creator = models.ForeignKey(
        'FbUser', related_name="user_creator", null=True)
    declined_count = models.PositiveIntegerField()
    description = models.TextField()
    eid = models.BigIntegerField(primary_key=True)
    end_time = models.DateTimeField(null=True)
    host = models.CharField(max_length=F_MAX_LENGTH)
    # name is already in 'models.Event'
    not_replied_count = models.PositiveIntegerField()
    pic = models.URLField()
    pic_big = models.URLField()
    # pic_cover = models.URLField()
    pic_small = models.URLField()
    pic_square = models.URLField()
    privacy = models.CharField(max_length=F_MAX_LENGTH)
    start_time = models.DateTimeField(null=True)
    ticket_uri = models.URLField(blank=True)
    timezone = models.CharField(max_length=F_MAX_LENGTH)
    unsure_count = models.PositiveIntegerField()
    venue = models.ForeignKey('FbLocation', null=True)

    # Not in facebook event table
    users = models.ManyToManyField(FbUser)

    objects = FbEventManager()
