#!/usr/bin/python3
"""
Fabric script that creates and
distributes an archive to the web servers
"""
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['34.204.50.206', '3.93.60.31']
def do_pack():
do_pack = __import__('1-pack_web_static').do_pack


def do_deploy():
    """generates a tgz archive"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return True
