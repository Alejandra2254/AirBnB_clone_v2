#!/usr/bin python3
"""script that generates a .tgz archive"""
from fabric.api import *
import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    try:
        now = datetime.datetime.now()
        date = now.strftime('%Y%m%d%H%M%S')
        name = "web_static_" + date + ".tgz"
        local("tar -cvfz versions/{} web_static".format(name))
        return name
    except:
        return None
