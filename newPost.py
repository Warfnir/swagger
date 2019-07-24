from core import jsonmodyfier
import json


def incomingPost(jsonobject):
    pass
    # path='/events/mobile'

    parsed = json.dumps(jsonobject)
    parsed = json.loads(parsed)

    platform = parsed['platform']  # 'mobile'
    branch = parsed['branch']  # 'staging'

    events = jsonobject['jsonData']

    jsonmodyfier.delete_events_from_given_branch(platform, branch)

    for i, event in enumerate(events):
        event_cathegory = events[i]['categoryName']
        event_parameters = events[i]['data']
        event_Name = events[i]['eventName']
        event_description = events[i]['description']
        jsonmodyfier.add_event(platform, branch, event_Name, event_cathegory, event_parameters,
                               event_description)  # need to send params when they are ready
