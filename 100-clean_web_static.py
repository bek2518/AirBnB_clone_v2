#!/usr/bin/python3
"""
Creates and distributes an archive to web server and cleans up
out of dsate archives
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
        return archive_name


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


def deploy():
    """
    Creates and deploys the archive
    """
    archive_path = do_pack()

    if archive_path is None:
        return False
    value = do_deploy(archive_path)
    return(value)


def do_clean(number=0):
    """
    Deletes out-of-date
    """
    given = int(number)
    archive_list = os.listdir ('./versions/')
    archive_list = sorted(archive_list)
    if given == 0:
        given += 1
    archive_list = archive_list[given:]

    for i in range((len(archive_list))):
        local("rm -rf /versions/{}".format(archive_list[i]))
        stripped = os.path.splitext(archive_list[i])[0]
        run("rm -rf /data/web_static/releases/{}".format(stripped))
