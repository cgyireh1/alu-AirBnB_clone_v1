#!/usr/bin/python3
"""
Fabric script to distribute archived web_static files to web servers
"""
from fabric.api import put, run, env, local
from os.path import exists
env.hosts = ['34.204.50.206', '3.93.60.31']

def do_deploy(archive_path):
    """
    distributes archived web_static from do_pack() to web servers
    """
    if archive_path is None:
        return False
    return True
