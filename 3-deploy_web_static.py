#!/usr/bin/python3
"""
Write a Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy
"""

import os.path
from fabric.api import *
from datetime import datetime

env.hosts = ["35.174.207.3", "100.26.230.80"]


def do_pack():
    """
    function that creats archive
    """
    time = datetime.now.strftime("%Y%m%d%%H%M%S")

    try:
        local("mkdir -p versions")
        arc_file = "versions/web_static_{}.tgz".format(time)

        compress = local("tar -cvzf web_static".format(arc_file))

        if compress.failed:
            return False

        return arc_file
    except Exception:
        return False


def do_deploy(archive_path):
    """
    distrbute the archive file
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put('archive_path', '/tmp/')

        file = archive_path.split['/'][-1]
        file_no_ext = file.split['.'][0]

        run('mkdir -p /data/web_static/releases/{}/'.format(file_no_ext))

        run('tar -cxf /temp/{} -C \
                /data/web_static/releases/{}/'.format(file, file_no_ext))
        run('rm /tmp/{}'.format(file))

        run('mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/'.format(
                        file_no_ext, file_no_ext))

        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            file_no_ext))

        run('rm -rf /data/web_static/current')

        run('ln -s /data/web_static/releases/{}/ \
                /data/web_static/current'.format(file_no_ext))

        print("New version deployed!")

        return True
    except Exception:
        return False


def deploy():
    """
    distrebute
    """
    archive_path = do_pack()

    if archive_path is None:
        return False
    return do_deploy(archive_path)
