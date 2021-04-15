#!/usr/bin/python3
"""script that generates a .tgz archive"""
from fabric.api import local
import datetime


def do_pack():
    """function"""
    try:
        now = datetime.datetime.now()
        date = now.strftime('%Y%m%d%H%M%S')
        local("mkdir -p versions")
        name = "web_static_" + date + ".tgz"
        path = "versions/" + name 
        local("tar -cvfz {} web_static".format(path))
        return path
    except:
        return None
