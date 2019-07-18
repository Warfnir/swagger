import json
import os


def add_event(platform_name,category_name,branch_name,event_name):
    toAdd = {event_name: {
        "options": {
            "tags": [
                category_name
            ],
            "summary": "(" + branch_name + ")",
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
    copy_event(platform_name,category_name,branch_name,toAdd,event_name)#.upadte(toAdd))

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


def update_event(platform,branch):
    """Updates existing event in given /platform/branch or adds new if it doesn't exists."""
    path = os.path.dirname(os.path.abspath(__file__))
    path, sep, rest = path.rpartition('\\')
    path += f'\\static\\{platform}.json'
    with open(path, 'r') as file:
        data = file.read()
        obj = data[data.find(('{')): data.rfind('}') + 1]
        jsonObj = json.loads(obj)
        all_paths = (jsonObj['paths'])
        vals = list(all_paths.values())
        keyz = list(all_paths.keys())
        i=0
        for val in vals:
            if val['options']['summary'] == '('+branch+')':
                jsonObj.get('paths').pop(keyz[i])
            elif len(val['options']['summary']) > 10:
                print("Both master and staging are present!")
                if branch == 'staging':
                    val['options']['summary'] = '(master)'
                else:
                    val['options']['summary'] = '(staging)'
            i=i+1
        #print(data)
        file.close()
        with open(path, 'w') as file:
            json.dump(jsonObj, file)


def copy_event(platform, category_name, branch, toAdd,event_name):
    """Adds new event if it doesn't exists yet in a given /platform/branch."""
    path = os.path.dirname(os.path.abspath(__file__))
    path, sep, rest = path.rpartition('\\')
    path += f'\\static\\{platform}.json'
    # Open file and check if event already exists
    with open(path, 'r') as file:
        data = file.read()
        obj = data[data.find(('{')): data.rfind('}') + 1]
        jsonObj = json.loads(obj)   # File content
        all_paths=(jsonObj['paths'])
        #print((all_paths))
        vals=list(all_paths.values())
        keyz=list(all_paths.keys())
        #print(keyz)
        cnt=0
        for val in vals:
            print(keyz[cnt])
            zloto=(val['options']['tags'])

            #print(str(zloto))
            #if(str(zloto).find('CategoryNames'))!=-1:
            #print(zloto)
            #print(val)
            if keyz[cnt]==event_name:
                val['options']['summary']='(master staging)'
                toAdd[event_name]['options']['summary'] = '(master staging)'
            cnt=cnt+1
            #jeśli kategoria już istnieje dodaj edytowany branch i jego schemat
        print("adding event")
        #print(jsonObj.get('paths'))
        jsonObj.get('paths').update(toAdd)
        #print(jsonObj.get('paths'))
            # for i in jsonObj.get('paths'):
            #    print(i)
            # print(jsonObj.get('paths').get('MY_EVENT'))
            # jsonObj.get('paths')
            #cnt=cnt+1

        # jsonObj.get('paths').update(toAdd)
        # for i in jsonObj.get('paths'):
        #     print(i)
        # print(jsonObj.get('paths').get('MY_EVENT'))
        # jsonObj.get('paths')

    with open(path, 'w') as file:
        json.dump(jsonObj, file)
    pass


#copy_event('server', 'CALL', 'master')
