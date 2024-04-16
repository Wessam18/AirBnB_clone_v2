#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """archive file"""

    time = datetime.now().strftime("%Y%m%d%H%M%S")

    directory = local("mkdir -p versions")
    if directory.failed:
        return None

    arc_file = 'versions/web_static_{}.tgz'.format(time)

    compress = local("tar -cvzf {} web_static".format(arc_file))

    if compress.failed:
        return None

    return arc_file
