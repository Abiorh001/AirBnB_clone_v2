#!/usr/bin/python
"""a script to add compressed file to server
   the script will uncompreesed the files
   the script will served the servers the index.html files"""
from fabric.api import run, put, env
import os.path
env.hosts = ["54.172.57.51", "34.232.78.100"]
env.key_filename = '~/.ssh/school'
env.user = "ubuntu"


def do_deploy(archive_path):
    """checking if archive_path exists"""
    if not os.path.exists(archive_path):
        return False
    """adding my archive_path from local machine to my server path /tmp/"""
    put(archive_path, "/tmp/")
    archive file path
    compressed_filepath = "versions/web_static_20230406235730.tgz"
    compressed_filename = compressed_filepath.split("/")[1]
    #my archive file without extension name .tgz
    compressed_file_without_ext = compressed_filename.split(".")[0]
    # uncompressed file folder
    folder_uncompressed_file = "/data/web_static/releases/{}".format(compressed_file_without_ext)
    # making a directory for my uncompreesed file
    run("sudo mkdir -p {}".format(folder_uncompressed_file))
    # uncompressing the archive file
    run("sudo tar -xzf /tmp/{} -C {}".format(compressed_filename, folder_uncompressed_file))
    # removing the archive file
    run("sudo rm /tmp/{} ".format(compressed_filename))
    # moving the uncompressed files to the right folder
    run("sudo mv {}/web_static/* {}".format(folder_uncompressed_file, folder_uncompressed_file))
    # removing the web_static folder
    run("sudo rm -rf {}/web_static".format(folder_uncompressed_file))
    # removing the previous added symbolic link
    run("sudo rm -rf /data/web_static/current")
    # creating a new symbolic link
    run("sudo ln -s {} /data/web_static/current".format(folder_uncompressed_file))
    # return True if all process done succesfully
    return True
