#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy
"""
from os.path import exists
from fabric.api import env, put, run, sudo

env.hosts = ["54.175.135.133"]


def do_deploy(archive_path):
    """
    deploy archive the web servers
    """

    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        file = archive_path.split('/')[-1]
        file_without_ext = file.split('.')[0]

        run('mkdir -p /data/web_static/releases/{}/'.format(file_without_ext))

        run('tar -xzf /tmp/{} -C \
                /data/web_static/releases/{}'.format(file, file_without_ext))

        run('rm /tmp/{}'.format(file))

        run('mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/'.format(
                    file_without_ext, file_without_ext))

        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            file_without_ext))

        run('rm /data/web_static/current')

        run('ln -sf /data/web_static/releases/{} \
                /data/web_static/current'.format(file_without_ext))

        print('New version deployed!')

        return True

    except Exception:
        return False
