def incomingPost(jsonobject):
    import json
    import os
    parsejson=json.dumps(jsonobject)
    parsed = json.loads(parsejson)
    #print(parsed)
    ola = parsed['platform']#'mobile'
    ala = parsed['branch']#'staging'
    print(ola)
    print(ala)

    def platform_name(igllo):
        if igllo == 'mobile':
            print("it's a mobile post")
            path = '/mobile'
        elif igllo == 'server':
            print("it's a server/post")
            path = '/server'
        elif igllo == 'web':
            print("it's a web post")
            path = '/web'
        elif igllo == 'gift':
            print("it's a gift post")
            path = '/gift'
        else:
            print("Unvalid platform name")
            raise ValueError
        branch_name(ala, path)

    def branch_name(ollgi, path):
        if ollgi == 'master':
            print('master branch')
            path = path + '/master'
        elif ollgi == 'staging':
            print('staging branch')
            path = path + '/staging'
        else:
            print("Wrong branch name")
            raise ValueError
        print(path)
        return (path)

    platform_name(ola)


#openair = '{"branch":"master","joiobject":"arguments","platform":"mobile"}'
#incomingPost(openair)
