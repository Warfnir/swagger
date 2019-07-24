import json
import os
import traceback


def add_event(platform, branch, event_Name, event_cathegory, event_parameters, event_description):
    try:
        path = os.path.dirname(os.path.abspath(__file__))
        path, sep, rest = path.rpartition('/')
        path += f'/static/{platform}.json'
        with open(path, 'r') as file:
            data = json.load(file)
            events = data['paths'].keys()
            branch = branch.upper() + ' '
            added = False
            same_events = []
            old_key = None
            new_key = None
            new_value = None
            for event in events:
                # if event exists then append branch and new model
                if event_Name in event:
                    same_events.append(event)

            for event in same_events:
                tags = data['paths'][event]['options']['tags']
                if tags[0] == event_cathegory:
                    branches = event[event.find('('):event.find(')') + 1]
                    branches = branches[:-1] + branch.upper() + ')'
                    old_key = event
                    new_key = event_Name + ' ' + branches
                    new_value = data['paths'][event]
                    new_value['options']['requestBody']['content'][branch[:-1]] = {
                        'schema': event_parameters}  # {'schema':{'type':'object', 'properties': event_parameters}}
                    print(new_value)
                    added = True
                    break

            if new_key:
                data['paths'].pop(old_key)
                data['paths'][new_key] = new_value
                data['paths'][new_key]['options']['description'] = event_description

            if not added:
                event_Name = f'{event_Name} ({branch})'
                data['paths'][event_Name] = {
                    'options': {'tags': [event_cathegory.upper()], 'description': event_description,
                                'requestBody': {'content': {branch: {
                                    'schema': event_parameters}}}}}
        with open(path, 'w+') as file:
            json.dump(data, file)

        return
    except Exception as e:
        traceback.print_exc()


def delete_events_from_given_branch(platform, branch):
    path = os.path.dirname(os.path.abspath(__file__))
    path, sep, rest = path.rpartition('/')
    path += f'/static/{platform}.json'
    try:
        with open(path, 'r+') as file:
            data = json.load(file)
            events = data['paths'].keys()
            branch = branch.upper() + ' '
            paths = dict()
            for event in events:
                branches = event[event.find('('):event.find(')') + 1]
                if branch in branches:
                    # delete branch from branches
                    branches = branches.replace(branch, '')

                    # delete event if doesnt have more branches
                    if len(branches) != 2:
                        value = data['paths'][event]
                        value['options']['requestBody']['content'].pop(branch[:-1])
                        paths[event.split('(')[0] + branches] = value
                else:
                    paths[event] = data['paths'][event]
            # data['paths'] = paths
        with open(path, 'w+') as file:
            data['paths'] = paths
            json.dump(data, file)
        return
    except Exception as e:
        traceback.print_exc()
