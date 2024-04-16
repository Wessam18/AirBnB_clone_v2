#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """archive file"""

    time = datetime.now().strftime("%Y%m%d%H%M%S")

    directory = local("mkdir -p versions")
    if directory.failed:
        return None

    arc_file = f'versions/web_static_{time}.tgz'

    compress = local(f"tar -cvzf {arc_file} web_static")

    if compress.failed:
        return None

    return arc_file
