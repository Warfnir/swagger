import json
import os
import re
import traceback


def add_event(platform_name, category_name, branch_name, event_name):
    toAdd = {event_name + " ( " + branch_name + " )": {
        "options": {
            "tags": [
                category_name
            ],
            # "summary": "(" + branch_name + ")",
            "description": "give a description here"
            # "responses": {
            #     "200": {
            #         "description": "OK",
            #         "schema": {
            #             "$ref": "#/components/schemas/staging"
            #         }
            #     }
            # }
        }
    }
    }
    print('tutaj')
    copy_event(platform_name, category_name, branch_name, toAdd, event_name)  # .upadte(toAdd))


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


def check_if_event_exists(event, branch, platform):
    """Returns boolean whether event with specified name exists in given /platform/branch"""
    pass


def delete_events_from_given_branch(platform, branch):
    """Updates existing event in given platform and deletes all with the current branch."""
    path = os.path.dirname(os.path.abspath(__file__))
    path, sep, rest = path.rpartition('\\')
    path += f'\\static\\{platform}.json'
    try:
        with open(path, 'r+') as file:
            data = json.load(file)
            events = data['paths'].keys()
            branch = branch.upper() + ' '

            for event in events:
                branches = event[event.find('('):event.find(')') + 1]
                if branch in branches:
                    # delete branch from branches
                    branches = branches.replace(branch,'')

                    # delete event if doesnt have more branches
                    if len(branches) == 2:
                        data['paths'].pop(event)

                    # delete model of given branch
                    else:
                        data['paths'][event]['options']['requestBody']['content'].pop(branch[:-1])
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
