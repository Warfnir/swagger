import json
import os

toAdd = {"MY_EVENT": {
    "options": {
        "tags": [
            "Gift Master"
        ],
        "summary": "Returns my event",
        "responses": {
            "200": {
                "description": "OK",
                "schema": {
                    "$ref": "#/components/schemas/bookRequests"
                }
            }
        }
    }
}
}

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


def add_event():  # event, branch, platform):
    """Adds new event if it doesn't exists yet in a given /platform/branch."""
    path = os.path.dirname(os.path.abspath(__file__))
    path, sep, rest = path.rpartition('\\')
    path += '\\static\\'
    print(path)
    print(os.listdir(path))

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
    # pass

add_event()