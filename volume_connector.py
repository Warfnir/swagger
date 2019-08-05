import os

import docker


def get_volume_path(volume_name):
    client = docker.from_env()
    volumes = client.volumes.list()
    volume = None
    for v in volumes:
        if v.name == "swagg-volume":
            volume = v.id
            break

    try:
        volume = client.volumes.get(volume)
    except Exception:
        volume = client.volumes.create(name=volume_name)
        os.mkdir(volume.attrs.get('Mountpoint')+'/platforms_branches')
    finally:
        client.close()
    return volume.attrs.get('Mountpoint')
