import docker

client = docker.from_env()
volumes = client.volumes.list()
volume = None
volume_exists = False
for v in volumes:
    if v.name == "swagg-volume":
        volume = v.id
        volume_exists = True
        break

if volume_exists:
    volume = client.volumes.get(volume)
    print(volume.name,'\n', volume,'\n', volume.attrs.get('Mountpoint'))
else:
    volume = client.volumes.create(name='swagg-volume')
    print(volume.attrs.get('Mountpoint'))