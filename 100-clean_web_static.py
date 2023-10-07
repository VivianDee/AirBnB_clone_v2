#!/usr/bin/python3
"""Fabric script that deletes out-of-date archives."""
from fabric.api import *
import os


env.hosts = ['100.24.205.80', '54.85.130.183']


def do_clean(number=0):
    """Deletes out-of-date archives."""
    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1

    archives_path = "/data/web_static/releases"
    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs -I {{}} rm {{}}".format(number))
    with cd(archives_path):
        run("sudo ls -t | sudo tail -n +{} | sudo xargs -I {{}} sudo rm -rf {{}}".format(number))

