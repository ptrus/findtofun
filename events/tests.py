from django.utils import unittest
from models import FbUser, FbEvent


class ModelsTestCase(unittest.TestCase):
    def test_user_update_only_neccessary(self):
        test_user = FbUser.objects.create(uid=1, sex="Male")
        modified = FbUser.objects.update_user(test_user, sex="Female")
        self.assertEqual(modified, ["sex"])
        self.assertEqual(test_user.sex, "Female")

    def test_event_update_only_neccessary(self):
    	test_event = FbEvent.objects.create_event(
        	all_members_count=5,
        	attending_count=1,
        	creator=1,
        	declined_count=1,
        	eid=1, 
        	name="Event",
        	not_replied_count=1,
        	venue={"city":"Ljubljana"},
        	ticket_uri=None,
        	timezone=None,
        	privacy=None,
        	unsure_count=1
        )

        test_event.save()

        modified = FbEvent.objects.update_event(
        	test_event,
        	all_members_count=10)
        self.assertEqual(modified, ["all_members_count"])
        self.assertEqual(test_event.all_members_count, 10)
