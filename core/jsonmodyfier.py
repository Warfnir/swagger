import json
import os
import re
import traceback


def add_event(platform, branch, event_Name, event_cathegory, event_parameters):
    try:
        path = os.path.dirname(os.path.abspath(__file__))
        path, sep, rest = path.rpartition('\\')
        path += f'\\static\\{platform}.json'
        with open(path, 'r') as file:
            data = json.load(file)
            events = data['paths'].keys()
            print(events)
            branch = branch.upper() + ' '
            print(branch)
            added = False
            same_events = []
            old_key = None
            new_key = None
            new_value = None
            for event in events:
                # if event exists then append branch and new model
                if event_Name in event:
                    same_events.append(event)

            print('SAME: ',same_events)
            for event in same_events:
                tags = data['paths'][event]['options']['tags']
                print('TAGS:   ', tags, tags[0])
                if tags[0] == event_cathegory:
                    branches = event[event.find('('):event.find(')') + 1]
                    branches = branches[:-1] + branch.upper() + ')'
                    old_key = event
                    new_key = event_Name+' '+branches
                    print('NEW KEY:   ',new_key)
                    new_value = data['paths'][event]
                    new_value['options']['requestBody']['content'][branch[:-1]] = {'schema':event_parameters} #{'schema':{'type':'object', 'properties': event_parameters}}
                    print(new_value)
                    added = True
                    break

            if new_key:
                data['paths'].pop(old_key)
                data['paths'][new_key] = new_value

            #
            # if not added:
            #     event_Name = f'{event_Name} ({branch})'
            #     data['paths'][event_Name] = {'options':{'requestBody':{'content':{branch:{'schema':{'type':'object', 'properties':event_parameters}}}}}}

        with open(path, 'w+') as file:
            json.dump(data,file)


    except Exception as e:
        traceback.print_exc()


# with open('E:\Python Projects\swagger\static\gift.json', 'r') as file:
#     data = file.read()
#     obj = data[data.find(('{')): data.rfind('}') + 1]
#     jsonObj = json.loads(obj)
#     print(type(jsonObj))
#     print(jsonObj)
#     jsonObj.get('paths').update(toAdd)
#     for i in jsonObj.get('paths'):
#         print(i)
#     print(jsonObj.get('paths').get('MY_EVENT'))
#     jsonObj.get('paths')
#
# with open('E:\Python Projects\swagger\static\gift.json', 'w') as file:
#     json.dump(jsonObj, file)


def delete_events_from_given_branch(platform, branch):
    path = os.path.dirname(os.path.abspath(__file__))
    path, sep, rest = path.rpartition('\\')
    path += f'\\static\\{platform}.json'
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


def copy_event(platform, category_name, branch, toAdd, event_name):
    """Adds new event if it doesn't exists yet in a given /platform/branch."""
    path = os.path.dirname(os.path.abspath(__file__))
    path, sep, rest = path.rpartition('\\')
    path += f'\\static\\{platform}.json'
    # Open file and check if event already exists
    with open(path, 'r') as file:
        data = file.read()
        obj = data[data.find(('{')): data.rfind('}') + 1]
        jsonObj = json.loads(obj)  # File content
        all_paths = (jsonObj['paths'])
        # print((all_paths))
        vals = list(all_paths.values())
        keyz = list(all_paths.keys())
        # print(keyz)
        cnt = 0
        for val in vals:
            # print(keyz[cnt])
            zloto = (val['options']['tags'])
            present_event = (keyz[cnt])
            present_event = str(present_event).split(' ', 1)
            # print(present_event[0])
            # print(present_event[0] + '       ' + present_event[1])
            if present_event[0] == event_name:
                branch_name = str(present_event[1])
                end = len(branch_name) - 1
                # print (branch_name+'lllll'+branch)
                branch_name = branch_name + ' ' + branch
                # present_event[1]=str(present_event[1])[end]
                keyz[cnt] = present_event[0] + ' ' + branch_name
                # print(keyz[cnt])
                # print('tukej')
            # print(str(zloto))
            # if(str(zloto).find('CategoryNames'))!=-1:
            # print(zloto)
            # print(val)
            if keyz[cnt] == event_name:
                val['options']['summary'] = '(master staging)'
                toAdd[event_name]['options']['summary'] = '(master staging)'
                # jeśli kategoria już istnieje dodaj edytowany branch i jego schemat
            cnt = cnt + 1
        # print("adding event")
        # print(jsonObj.get('paths'))
        jsonObj.get('paths').update(toAdd)
        # print(jsonObj.get('paths'))
        # for i in jsonObj.get('paths'):
        #    print(i)
        # print(jsonObj.get('paths').get('MY_EVENT'))
        # jsonObj.get('paths')
        # cnt=cnt+1

        # jsonObj.get('paths').update(toAdd)
        # for i in jsonObj.get('paths'):
        #     print(i)
        # print(jsonObj.get('paths').get('MY_EVENT'))
        # jsonObj.get('paths')

    with open(path, 'w') as file:
        json.dump(jsonObj, file)
    pass

# copy_event('server', 'CALL', 'master')
