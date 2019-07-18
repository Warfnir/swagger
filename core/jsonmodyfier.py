import json
import os

event_name='callingcenter'
category_name='call'
branch_name='master'

def add_event(platform_name,category_name,branch_name,event_name):
    toAdd = {event_name: {
        "options": {
            "tags": [
                category_name
            ],
            "summary": "("+ branch_name+")",
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
    }#print
    print(toAdd[event_name])
    copy_event(platform_name,category_name,branch_name,toAdd)#.upadte(toAdd))

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


def update_event(event, branch, platform):
    """Updates existing event in given /platform/branch or adds new if it doesn't exists."""
    pass


def copy_event(platform, category_name, branch, toAdd):
    """Adds new event if it doesn't exists yet in a given /platform/branch."""
    print(platform,category_name,branch)
    # Designating path to file
    path = os.path.dirname(os.path.abspath(__file__))
    #print(path)
    path, sep, rest = path.rpartition('\\')
    #print(path)
    path += f'\\static\\{platform}.json'
    #print(path)

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
            cnt=cnt+1
            #print(str(zloto))
            #if(str(zloto).find('CategoryNames'))!=-1:
            print(zloto)
            print(val)
            if len(val['options']['summary'])>10:
                print("Both master and staging are present!")

            #jeśli kategoria już istnieje dodaj edytowany branch i jego schemat
        print("adding event")
        print(jsonObj.get('paths'))
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

    with open('C:\\Users\\dakim\\PycharmProjects\\swagger\\static\\server.json', 'w') as file:
        json.dump(jsonObj, file)
    pass


#copy_event('server', 'CALL', 'master')
