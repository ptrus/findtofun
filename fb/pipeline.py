from django.http import HttpResponseRedirect
from facepy import GraphAPI
from events.models import Event

def write_extra_details(request, *args, **kwargs):
    user = kwargs['user']
    response = kwargs['response']
    user.gender = response.get("gender")
    user.save()
    
    graph = GraphAPI(response.get("access_token"))
    query = """
        SELECT eid, name, host, venue, location, start_time, end_time, update_time FROM event 
        WHERE eid IN (
           SELECT eid FROM event_member 
           WHERE (uid IN (SELECT uid2 FROM friend WHERE uid1 = me())  OR uid = me())
           )
        AND start_time > now()
        """
        
#    query_results = graph.fql(query)
#    if query_results.has_key("data"):
#        events_data = query_results["data"]
#        events_objects = []
#        
#        for event in events_data:
#            host = event["host"]
#            name = event["name"]
#            location = event["location"]
#            start_time = event["start_time"]
#            end_time = event["end_time"]
#            update_time = event["update_time"]
#            
#            events_objects.append(Event.objects.create_event(
#                 None, name, location, start_time, end_time
#             ))
#            
#        Event.objects.bulk_create(events_objects)    
            