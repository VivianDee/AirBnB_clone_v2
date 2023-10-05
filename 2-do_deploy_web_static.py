#!/usr/bin/python3
"""
    This scrip Distributes an archive to my web servers,
    using the function do_deploy
"""
from fabric.api import *
from fabric import *
from datetime import datetime
import os
import sys


env.hosts = ['100.24.205.80', '54.85.130.183']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Distributes an archive to my web servers"""
    for i in env.hosts:
        if not os.path.exists(archive_path):
            return False

        upload = put(archive_path, '/tmp/')

        file_name = archive_path.split('/')[1].split('.tgz')[0]
        comp_file = "{}.tgz".format(file_name)

        directory = run("sudo mkdir -p /data/web_static/releases/{}".format(file_name))
        command = "sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(comp_file, file_name)
        result = run(command)

        """Delete the archive and symlink from the web server"""
        sym_link = "/data/web_static/current"
        check = run("sudo rm /tmp/{}.tgz".format(file_name))
        check2 = run("sudo rm -rf {}".format(sym_link))

        check3 = run("sudo cp -r /data/web_static/releases/{}/web_static/* /data/web_static/releases/".format(file_name))
        check4 = run("sudo ln -sf /data/web_static/releases/{} {}".format(file_name, sym_link))
        check5 = run("sudo service nginx restart")

        if upload.failed or result.failed or check.failed or check2.failed or check3.failed or check4.failed or check5.failed:
            return False
        else:
            print("New version deployed!")
            return True