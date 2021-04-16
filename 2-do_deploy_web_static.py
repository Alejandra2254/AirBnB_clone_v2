#!/usr/bin/python3
"""script that generates a .tgz archive"""
from fabric.api import local
from os import path

def do_deploy(archive_path):
    if path.exists(archive_path) is False:
        return False
    try:
        #Upload the archive to the /tmp/ directory 
        put(archive_path, "/tmp")
        # Uncompress the archive to the folder
        no_extension = archive_path.split(".")
        run("mkdir -p /data/web_static/releases/{}".format(no_extension[0]))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(archive_path, archive_path))
        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_path))
        # Delete the symbolic link /data/web_static/current from the web server
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(archive_path, archive_path))
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive_path))
        run("rm -rf /data/web_static/current")
        # Create a new the symbolic link /data/web_static/current on the web server,
        # linked to the new version of your code
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive_path))
        return True
    except:
        return False

