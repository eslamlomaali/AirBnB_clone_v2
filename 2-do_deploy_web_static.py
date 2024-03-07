#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy:
"""

from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['54.152.60.211', '34.229.71.198']  # <IP web-01>, <IP web-02>
# env.user = "ubuntu"
# env.key_filename = "~/.ssh/school"

def do_deploy(archive_path):
    """Distributes the archive to the web servers."""
    if not exists(archive_path):
        return False  # Returns False if the file is not found

    filename = archive_path.split('/')[-1]
    no_tgz = '/data/web_static/releases/{}'.format(filename.split('.')[0])
    tmp = "/tmp/{}".format(filename)

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(no_tgz))
        return True
    except Exception as e:
        print(e)
        return False
