def incomingPost(jsonobject):
    import json
    import os
    #path='/events/mobile'
    parsejson=json.dumps(jsonobject)
    parsed = json.loads(parsejson)
    #print(parsed)
    platform = parsed['platform']#'mobile'
    branch = parsed['branch']#'staging'
    print(parsed['jsonData'])

    #print(platform)
    #print(branch)

    def platform_name(igllo):
        if igllo == 'mobile':
            #print("it's a mobile post")
            platform='mobile'
            path = '/mobile'
        elif igllo == 'server':
            #print("it's a server/post")
            platform='server'
            path = '/server'
        elif igllo == 'web':
            #print("it's a web post")
            platform='web'
            path = '/web'
        elif igllo == 'gift':
            #print("it's a gift post")
            path = '/gift'
        else:
            #print("Unvalid platform name")
            raise ValueError
        if branch_name(branch)==True:
            #print('Create list of staging events list')
            #print('delete all master in ' + path, " "+platform)
            return (path)
        else:
            #print('delete all staging in ' + path)
            #print('Create list of master events list')
            return {path}

    def branch_name(ollgi):
        if ollgi == 'master':
            #print('master branch')
            master=True
            return master
            #path = path + '/master'
        elif ollgi == 'staging':
            #print('staging branch')
            master=False
            return master
            #path = path + '/staging'
        else:
            print("Wrong branch name")
            raise ValueError

    road=platform_name(platform)
    way=(str(road)).strip(' {\'}')
    print (jsonobject)
    print(jsonobject['jsonData'])
    events=jsonobject['jsonData']
    i=0
    for event in range(len(events)):
        event_cathegory=(events[i]['eventName'])
        print("For " + way + " . Create category "+event_cathegory)
        i=i+1


#openair = '{"branch":"master","joiobject":"arguments","platform":"mobile"}'
#incomingPost(openair)
