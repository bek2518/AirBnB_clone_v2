#!/usr/bin/python3
"""
Generates thz archive from contents of the webstatic folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    '''
    Packs files in the web_static to final archive
    '''
    local("mkdir -p versions")
    time = "%Y%m%d%H%M%S"
    archive_name = ("web_static_{}.tgz".format(
                    datetime.strftime(datetime.now(), time)))
    pack = local("tar -czvf {} web_static".format(archive_name))

    if pack.failed is True:
        return None
    else:
        return pack
