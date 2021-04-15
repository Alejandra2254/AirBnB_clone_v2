#!/usr/bin python3
"""script that generates a .tgz archive"""
from fabric.api import local
import datetime


def do_pack():
    try:
        now = datetime.datetime.now()
        date = now.strftime('%Y%m%d%H%M%S')
        local("mkdir -p versions")
        name = "web_static_" + date + ".tgz"
        local("tar -cvfz versions/{} web_static".format(name))
        return name
    except:
        return None
