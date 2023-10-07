#!/usr/bin/python3
"""
    This script creates and distributes an archive to my web servers.
"""
do_pack = __import__('1-pack_web_static').do_pack
from fabric.api import env
from fabric.api import local
from fabric import *


def deploy():
    """Creates and distributes an archive to my web servers"""
    archive_path = do_pack()

    if not archive_path:
        return False

    result = local(
        "fab -f 2-do_deploy_web_static.py do_deploy:archive_path={} -i {} -u {}".format(
            archive_path, env.key_filename[0], env.user), capture=True)
    print(result.stdout)
    return result.succeeded
