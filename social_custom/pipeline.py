from events import tasks


def write_extra_details(request, *args, **kwargs):
    user = kwargs['user']
    response = kwargs['response']
    user.gender = response.get("gender")
    user.save()

    access_token = response.get("access_token")
    tasks.process_events.delay(access_token)
