#!/usr/bin/python3
""" a script to compress html file to tar and uncompreesed and deploy to
webserver"""
from fabric.api import local, run, put, env
from datetime import datetime
import os

env.hosts = ["54.172.57.51", "34.232.78.100"]
env.key_filename = os.path.expanduser('~/.ssh/school')
env.user = "ubuntu"


def do_pack():
    """a function to compres the file"""
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_filepath = "versions/web_static_{}.tgz".format(time_now)
    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(archive_filepath))
        return "{}".format(archive_filepath)
    except Exception as e:
        return None


def do_deploy(archive_path):
    """Function that will run the script to uncompressed and deploy."""
    if not os.path.exists(archive_path):
        return False
    put(archive_path, "/tmp/")
    compressed_filename = archive_path.split("/")[1]
    compressed_file_without_ext = compressed_filename.split(".")[0]
    folder_uncompressed_file = "/data/web_static/releases/{}".format(
        compressed_file_without_ext)
    run("sudo mkdir -p {}".format(folder_uncompressed_file))
    run("sudo tar -xzf /tmp/{} -C {}".format(
        compressed_filename, folder_uncompressed_file))
    run("sudo rm /tmp/{} ".format(compressed_filename))
    run("sudo mv {}/web_static/* {}".format(
        folder_uncompressed_file, folder_uncompressed_file))
    run("sudo rm -rf {}/web_static".format(folder_uncompressed_file))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(
        folder_uncompressed_file))
    return True


def deploy():
    """function to create and deploy an archive  file to the webserver."""
    compressed_file_path = do_pack()
    if compressed_file_path is None:
        return False
    return do_deploy(compressed_file_path)
