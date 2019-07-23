from core import jsonmodyfier
import os
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
    for i,event in enumerate(events):
        event_cathegory = events[i]['categoryName']
        event_parameters = events[i]['data']
        event_Name = events[i]['eventName']
        print(i, event_Name)
        # jsonmodyfier.add_event(way, event_cathegory, branch, event_Name)  # need to send params when they are ready
#
# openair = '{"branch":"master","joiobject":"arguments","platform":"mobile"}'
# incomingPost(openair)
