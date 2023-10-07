#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
path="/data/web_static/releases/test"
sudo mkdir -p "$path" /data/web_static/shared
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee "$path/index.html"
sudo ln -sf "$path" /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "57i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
