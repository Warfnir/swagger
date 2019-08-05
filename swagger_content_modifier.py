import json
import os
import traceback


def save_new_content(parsed,volume_path):
    with open(f'{volume_path}/platforms_branches/{parsed["platform"].lower()}/{parsed["branch"].lower()}.json', 'w') as file:
        json.dump(parsed['jsonData'], file)


def generate_new_swagger_file(platform,volume_path):
    # load scheme
    with open(f'./static/scheme.json') as file:
        scheme = json.load(file)
    # get list of files with branches
    branches_files = os.listdir(f'{volume_path}/platforms_branches/{platform}')
    # for each file add events
    for file_name in branches_files:
        with open(f'{volume_path}/platforms_branches/{platform}/{file_name}', 'r') as file:
            file_events = json.load(file)
            file_events_keys = file_events.keys()
            act_events_keys = scheme.get('paths').keys()
            # compare all events from file with actual events
            for file_key in file_events_keys:
                event_added = False
                for act_key in act_events_keys:
                    if file_key in act_key:
                        # if events are the same compare categories
                        file_category = file_events[file_key]['categoryName'].upper()
                        act_category = scheme['paths'][act_key]['options']['tags']
                        act_category = act_category[0]
                        # if category is the same, append branch at the end of event key value
                        if file_category == act_category:
                            content = scheme['paths'][act_key]  # old content
                            scheme['paths'].pop(act_key)  # delete key
                            new_key = act_key[:-1] + file_name[:-5].upper() + ' )'  # create new key
                            # update content if its not null
                            file_data = file_events[file_key]['data']
                            if file_data != None:
                                content['options']['requestBody']['content'][file_name[:-5].upper()] = {
                                    'schema': file_data}
                            else:
                                content['options']['requestBody']['content'][file_name[:-5].upper()] = {
                                    'schema': {'type': 'object', 'required': [], 'properties': {}}}
                            # update scheme
                            scheme['paths'][new_key] = content
                            event_added = True
                            break
                            # else continue looping
                # if there was no the same event with the same category then append new one
                if not event_added:
                    new_key = f'{file_key} ( {file_name[:-5].upper()} )'
                    content = file_events[file_key]['data']
                    category = file_events[file_key]['categoryName'].upper()
                    if content:
                        scheme['paths'][new_key] = {'options': {'tags': [category],
                                                                'description': file_events[file_key]['description'],
                                                                'requestBody': {'content': {
                                                                    file_name[:-5].upper(): {'schema': content}}}}}
                    else:
                        scheme['paths'][new_key] = {'options': {'tags': [category],
                                                                'description': file_events[file_key]['description'],
                                                                'requestBody': {'content': {
                                                                    file_name[:-5].upper(): {
                                                                        'schema': {'type': 'object', 'required': [],
                                                                                   'properties': {}}}}}}}
    scheme['info']['title'] = platform.upper()
    scheme['info']['description'] = f'Description of {platform.upper()}'
    return scheme


def process_request(json_data, volume_path):
    parsed = json.dumps(json_data)
    parsed = json.loads(parsed)

    save_new_content(parsed, volume_path)

    platform = parsed['platform'].lower()
    new_content = generate_new_swagger_file(platform,volume_path)

    with open(f'./static/{platform}.json', 'w') as file:
        json.dump(new_content, file)
