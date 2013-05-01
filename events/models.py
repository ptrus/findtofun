from django.db import models
import helpers as h

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


class FbUserManager(models.Manager):
    def create_user(self, **user_data):
        if "current_address" in user_data:
            current_address = user_data.pop("current_address")
            if current_address is not None:
                location = FbLocation.objects.filter(**current_address)
                if len(location) > 0:
                    user_data["current_address"] = location[0]
                else:
                    user_data["current_address"] = FbLocation.objects.create(
                        **current_address)

        if "age_range" in user_data:
            age_range = user_data.pop("age_range")
            if age_range is not None:
                user_data["age_range_min"] = age_range.get("min", 0)
                user_data["age_range_max"] = age_range.get("max", 0)

        sex = user_data.get("sex")
        if sex is None:
            user_data["sex"] = ""

        return self.model(**user_data)

    def update_user(self, user, **user_data):
        modified_attrs = []

        modified_attrs.extend(h.change_textfields(
            user, user_data, ["name", "sex"]))

        if (isinstance(user_data.get("current_address"), dict)):
            current_address = user_data["current_address"]
            location = FbLocation.objects.filter(**current_address)
            if len(location) == 0:
                user.current_address = FbLocation.objects.create(
                    **current_address)
                modified_attrs.append("current_address")

        if "age_range" in user_data:
            new_age_range = user_data.pop("age_range")
            if new_age_range is not None:
                new_age_range_min = new_age_range.get("min", 0)
                new_age_range_max = new_age_range.get("max", 0)

                if (isinstance(new_age_range_min, int) and
                        user.age_range_min is not new_age_range_min):
                    user.age_range_min = new_age_range_min
                    modified_attrs.append("age_range_min")
                if (isinstance(new_age_range_max, int) and
                        user.age_range_max is not new_age_range_max):
                    user.age_range_max = new_age_range_max
                    modified_attrs.append("age_range_max")

        has_changed = len(modified_attrs) > 0
        if has_changed:
            user.save(update_fields=modified_attrs)

        return has_changed


class FbEventManager(models.Manager):
    def create_event(self, **event_data):
        name = event_data.pop("name")
        if name is not None:
            event_data["common"] = Event.objects.create(name=name)

        venue = event_data.pop("venue")
        if isinstance(venue, dict):
            location = FbLocation.objects.filter(**venue)
            if len(location) > 0:
                event_data["venue"] = location[0]
            else:
                event_data["venue"] = FbLocation.objects.create(**venue)

        cover_data = event_data.pop("pic_cover")
        if isinstance(cover_data, dict):
            cover = FbCover.objects.filter(**cover_data)
            if len(cover) > 0:
                event_data["pic_cover"] = cover[0]
            else:
                event_data["pic_cover"] = FbCover.objects.create(**cover_data)

        creator_id = event_data.pop("creator")
        if isinstance(creator_id, (int, long)):
            try:
                creator = FbUser.objects.get(pk=creator_id)
            except FbUser.DoesNotExist:
                creator = FbUser.objects.create_user(pk=creator_id)
            event_data["creator"] = creator

        privacy = event_data.get("privacy")
        if privacy is None:
            event_data["privacy"] = ""

        ticket_uri = event_data.get("ticket_uri")
        if ticket_uri is None:
            event_data["ticket_uri"] = ""

        timezone = event_data.get("timezone")
        if timezone is None:
            event_data["timezone"] = ""

        return self.model(**event_data)

    def update_event(self, event, **event_data):
        modified_attrs = []

        tmp = ["all_members_count", "attending_count", "declined_count",
            "not_replied_count", "unsure_count"]
        modified_attrs.extend(h.change_numfields(event, event_data, tmp))

        tmp = ["pic", "pic_big", "pic_small", "pic_square", "ticket_uri"]
        modified_attrs.extend(h.change_urlfields(event, event_data, tmp))

        tmp = ["description", "end_time", "host", "privacy", "start_time",
            "timezone"]
        modified_attrs.extend(h.change_textfields(event, event_data, tmp))

        if isinstance(event_data.get("name"), basestring):
            new_name = event_data["name"]
            event.common.name = new_name
            event.common.save()

        if "creator" in event_data:
            new_creator_id = event_data.get("creator")
            if (isinstance(new_creator_id, (int, long)) and
                    event.creator.uid is not new_creator_id):
                modified_attrs.append("creator")
                try:
                    new_creator = FbUser.objects.get(pk=new_creator_id)
                except FbUser.DoesNotExist:
                    new_creator = FbUser.objects.create_user(pk=new_creator_id)
                event.creator = new_creator

        if isinstance(event_data.get("venue"), dict):
            venue = event_data["venue"]
            new_venue = FbLocation.objects.filter(**venue)
            if len(new_venue) == 0:
                event.venue = FbLocation.objects.create(**venue)
                modified_attrs.append("venue")

        if isinstance(event_data.get("cover"), dict):
            cover = event_data["cover"]
            new_cover = FbCover.objects.filter(**cover)
            if len(new_cover) == 0:
                event.cover = FbCover.objects.create(**cover)
                modified_attrs.append("cover")

        has_changed = len(modified_attrs) > 0
        if has_changed:
            event.save(update_fields=modified_attrs)

        return has_changed


class FbLocationManager(models.Manager):
    def create_location(self, **kwargs):
        return self.model(**kwargs)


class FbUser(models.Model):
    uid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=F_MAX_LENGTH)
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


class FbCover(models.Model):
    cover_id = models.BigIntegerField(primary_key=True)
    source = models.URLField()
    offset_y = models.PositiveIntegerField()
    offset_x = models.PositiveIntegerField()


class FbEvent(models.Model):
    all_members_count = models.PositiveIntegerField()
    attending_count = models.PositiveIntegerField()
    creator = models.ForeignKey(
        'FbUser', related_name="user_creator", null=True)
    declined_count = models.PositiveIntegerField()
    description = models.TextField()
    eid = models.BigIntegerField(primary_key=True)
    end_time = models.DateTimeField(null=True)
    host = models.CharField(max_length=F_MAX_LENGTH)
    common = models.OneToOneField(Event, null=True)
    not_replied_count = models.PositiveIntegerField()
    pic = models.URLField()
    pic_big = models.URLField()
    pic_cover = models.OneToOneField(FbCover, null=True)
    pic_small = models.URLField()
    pic_square = models.URLField()
    privacy = models.CharField(max_length=F_MAX_LENGTH)
    start_time = models.DateTimeField(null=True)
    ticket_uri = models.URLField(blank=True)
    timezone = models.CharField(max_length=F_MAX_LENGTH)
    unsure_count = models.PositiveIntegerField()
    venue = models.ForeignKey('FbLocation', null=True)

    # Not in facebook event table
    users = models.ManyToManyField(FbUser, through="FbEventFbUser")

    objects = FbEventManager()


class FbEventFbUser(models.Model):
    fbevent = models.ForeignKey('FbEvent')
    fbuser = models.ForeignKey('FbUser')
