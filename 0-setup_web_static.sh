#!/usr/bin/env bash
#a script to install nginx and create a dummy index.html

#updating the server
sudo apt-get update
# installing nginxwebserver
sudo apt-get install nginx -y

#creating the directory to store my html file
sudo mkdir -p /data/web_static/releases/test/
#creating the directory for the symbolic link
sudo mkdir -p /data/web_static/shared/

#creating a dummy index.html file to write inside my test directory
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

#creating a symbolic link t0 link our index.html to current directory
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# changing ownerning of the file to user ubutn and group ubuntu
sudo chown -R ubuntu:ubuntu /data/
#creating the location on the sever to served the index.html
sudo sed -i '/server_name _;/a \ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default
#restart the nginx webserver
sudo service nginx restart
