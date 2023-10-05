#!/usr/bin/python3
"""
    This script generates a .tgz archive from the contents of the web_static
    folder of my AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from a folder"""

    time = datetime.now()
    time = time.strftime("%Y%m%d%H%M%S")
    archive = "web_static_{}.tgz".format(time)

    if not os.path.exists("versions"):
        os.makedirs("versions")

    command = "tar -czvf versions/{} web_static".format(archive)

    compressed = local(command)
    if compressed.succeeded:
        return compressed
    else:
        return None
