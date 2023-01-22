#!/usr/bin/python3
"""
Distributes an archive to web server
"""
from fabric.api import put, run, local, env
import os
from datetime import datetime

env.hosts = ["54.146.93.137", "18.209.224.64"]


def do_pack():
    '''
    Packs files in the web_static to final archive
    '''
    local("mkdir -p versions")
    time = "%Y%m%d%H%M%S"
    archive_name = ("versions/web_static_{}.tgz".format(
                    datetime.strftime(datetime.now(), time)))
    pack = local("tar -czvf {} web_static".format(archive_name))

    if pack.failed is True:
        return None
    else:
        return pack


def do_deploy(archive_path):
    """
    Unpacks and distributes web static archive
    """
    if not os.path.exists(archive_path):
        return False

    name = os.path.basename(archive_path)
    stripped = os.path.splitext(name)[0]
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(stripped))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(name, stripped))
        run("rm -rf /tmp/{}".format(name))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(stripped, stripped))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(stripped))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(stripped))

    except Exception:
        return False
    return True
