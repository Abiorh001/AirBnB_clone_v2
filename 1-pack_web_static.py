#!/usr/bin/python3
# a script to compress html file to tar
from fabric.api import local
from datetime import datetime
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
