from django.utils import unittest
from models import FbUser, FbEvent
import helpers as h
from django.utils.dateparse import parse_datetime
import pytz


user_data = dict(
    uid=1,
    name="Ipri",
    sex="Male",
    age_range=dict(min=18, max=24),
    current_address=dict(city="Ljubljana"))

event_data = dict(
    all_members_count=1,
    attending_count=1,
    creator=1,
    declined_count=1,
    description="Good event",
    eid=1,
    end_time="2013-05-14 03:00:00",
    host="Ipri",
    name="G event",
    not_replied_count=1,
    pic="http://goog.gl/1.jpg",
    pic_cover=dict(
        cover_id=1,
        source="http://goog.gl/1.jpg",
        offset_y=0,
        offset_x=0),
    pic_big="http://goog.gl/2.jpg",
    pic_small="http://goog.gl/3.jpg",
    pic_square="http://goog.gl/4.jpg",
    start_time="2013-05-14 03:00:00",
    ticket_uri="http://goog.gl/5",
    timezone="Europe/Rome",
    privacy="null",
    unsure_count=1,
    venue={"city": "Ljubljana"})


class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        try:
            FbEvent.objects.get(pk=event_data["eid"]).delete()
        except FbEvent.DoesNotExist:
            pass

        try:
            FbUser.objects.get(pk=user_data["uid"]).delete()
        except FbUser.DoesNotExist:
            pass

        event = FbEvent.objects.create_event(**event_data)
        user = FbUser.objects.create_user(**user_data)

        user.save()
        event.save()

        self.user = user
        self.event = event

    # def test_fbuser_with_fbevent(self):
    #     found = self.event.users.all()
    #     self.assertEqual(len(found), 0)

    #     self.event.users.add(self.user)
    #     self.event.save()
    #     found = self.event.users.all()
    #     self.assertEqual(len(found), 1)
    #     print self.event.users.all()[0]


def auto_change_value(obj, attr):
    data = {}
    value = getattr(obj, attr)
    if isinstance(value, (long, int)):
        data[attr] = value + 1
    if isinstance(value, (basestring)):
        naive = parse_datetime(value)
        if naive is not None:
            aware = pytz.timezone("Europe/Paris").localize(
                naive, is_dst=None)
            new_value = aware.strftime("%Y-%m-%d %H:%M:%S")
        else:
            # Regular string
            new_value = value + "!"

        data[attr] = new_value

    return data


class HelpersTestCase(unittest.TestCase):
    def setUp(self):
        try:
            FbUser.objects.get(uid=1).delete()
        except FbUser.DoesNotExist:
            pass

    def test_change_textfields(self):
        user = FbUser.objects.create(uid=1, sex="Male")
        user_data = dict(sex="Female")
        modified_attrs = h.change_textfields(user, user_data, user_data.keys())
        self.assertEqual(user_data.keys(), modified_attrs)

    def test_change_numfields(self):
        user = FbUser.objects.create(uid=1, age_range_min=1)
        user_data = dict(age_range_min=2)
        modified_attrs = h.change_numfields(user, user_data, user_data.keys())
        self.assertEqual(user_data.keys(), modified_attrs)


class FbUserModelTestCase(unittest.TestCase):
    def setUp(self):
        try:
            FbUser.objects.get(uid=1).delete()
        except FbUser.DoesNotExist:
            pass

        user = FbUser.objects.create_user(**user_data)
        user.save()

        self.user = user
        self.user_data = user_data

    def test_change_nothing(self):
        has_changed = FbUser.objects.update_user(self.user, **self.user_data)
        self.assertFalse(has_changed)

    def change_and_assert(self, **data):
        user = self.user
        FbUser.objects.update_user(user, **data)
        key, value = data.popitem()
        self.assertEqual(getattr(user, key), value)

    def auto_change_and_assert(self, attr):
        data = auto_change_value(self.user, attr)
        self.change_and_assert(**data)

    def test_change_name(self):
        self.auto_change_and_assert("name")

    def test_change_sex(self):
        self.auto_change_and_assert("sex")

    def test_change_age_range(self):
        user = self.user
        data = {"age_range": dict(min=1, max=2)}
        FbUser.objects.update_user(user, **data)
        self.assertEqual(user.age_range_min, data["age_range"]["min"])
        self.assertEqual(user.age_range_max, data["age_range"]["max"])

    def test_change_location(self):
        user = self.user
        data = {"current_address": dict(city="Maribor")}
        FbUser.objects.update_user(user, **data)
        self.assertEqual(user.current_address.city,
                         data["current_address"]["city"])


class FbEventModelTestCase(unittest.TestCase):
    def setUp(self):
        try:
            FbEvent.objects.get(pk=1).delete()
        except FbEvent.DoesNotExist:
            pass

        event = FbEvent.objects.create_event(**event_data)
        event.save()

        self.event = event
        self.event_data = event_data

    def change_and_assert(self, **data):
        event = self.event
        FbEvent.objects.update_event(event, **data)
        key, value = data.popitem()
        self.assertEqual(getattr(event, key), value)

    def auto_change_and_assert(self, attr):
        data = auto_change_value(self.event, attr)
        self.change_and_assert(**data)

    def test_change_nothing(self):
        has_changed = FbEvent.objects.update_event(
            self.event, **self.event_data)
        self.assertFalse(has_changed)

    def test_change_allmemberscount(self):
        self.auto_change_and_assert("all_members_count")

    def test_change_attending_count(self):
        self.auto_change_and_assert("attending_count")

    def test_change_declined_count(self):
        self.auto_change_and_assert("declined_count")

    def test_change_not_replied_count(self):
        self.auto_change_and_assert("not_replied_count")

    def test_change_unsure_count(self):
        self.auto_change_and_assert("unsure_count")

    def test_change_pic(self):
        self.auto_change_and_assert("pic")

    def test_change_pic_big(self):
        self.auto_change_and_assert("pic_big")

    def test_change_pic_small(self):
        self.auto_change_and_assert("pic_small")

    def test_change_pic_square(self):
        self.auto_change_and_assert("pic_square")

    def test_change_description(self):
        self.auto_change_and_assert("description")

    def test_change_host(self):
        self.auto_change_and_assert("host")

    def test_change_privacy(self):
        self.auto_change_and_assert("privacy")

    def test_change_start_time(self):
        self.auto_change_and_assert("start_time")

    def test_change_end_time(self):
        self.auto_change_and_assert("end_time")

    def test_change_timezone(self):
        self.auto_change_and_assert("timezone")

    def test_change_name(self):
        event = self.event
        new_name = event.common.name + "!"
        FbEvent.objects.update_event(event, name=new_name)
        self.assertEqual(event.common.name, new_name)

    def test_change_creator(self):
        event = self.event
        data = dict(creator=(event.creator.uid + 1))
        FbEvent.objects.update_event(event, **data)
        self.assertEqual(event.creator.uid, data["creator"])

    def test_change_venue(self):
        event = self.event
        data = dict(venue=dict(city="Maribor"))
        FbEvent.objects.update_event(event, **data)
        self.assertEqual(event.venue.city, data["venue"]["city"])
