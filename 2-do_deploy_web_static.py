#!/usr/bin/python3
"""a script to add compressed file to server
   the script will uncompreesed the files
   the script will served the servers the index.html files
"""
from fabric.api import run, put, env
import os.path
env.hosts = ["54.172.57.51", "34.232.78.100"]
env.key_filename = '~/.ssh/school'
env.user = "ubuntu"


def do_deploy(archive_path):
    """function that will run the script"""
    if not os.path.exists(archive_path):
        return False
    put(archive_path, "/tmp/")
    archive file path
    compressed_filepath = "versions/web_static_20230406235730.tgz"
    compressed_filename = compressed_filepath.split("/")[1]
    compressed_file_without_ext = compressed_filename.split(".")[0]
    folder_uncompressed_file = "/data/web_static/releases/{}".format(compressed_file_without_ext)
    run("sudo mkdir -p {}".format(folder_uncompressed_file))
    run("sudo tar -xzf /tmp/{} -C {}".format(compressed_filename, folder_uncompressed_file))
    run("sudo rm /tmp/{} ".format(compressed_filename))
    run("sudo mv {}/web_static/* {}".format(folder_uncompressed_file, folder_uncompressed_file))
    run("sudo rm -rf {}/web_static".format(folder_uncompressed_file))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(folder_uncompressed_file))
    return True
