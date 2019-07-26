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
    keys = events.keys()
    jsonmodyfier.delete_events_from_given_branch(platform, branch)

    for i, key in enumerate(keys):
        event_category = events[key]['categoryName'].upper()
        event_parameters = events[key]['data']
        event_Name = key
        event_description = events[key]['description']
        jsonmodyfier.add_event(platform, branch, event_Name, event_category, event_parameters,
                               event_description)
