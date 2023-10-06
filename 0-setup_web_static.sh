#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static
if ! command -v nginx &> /dev/null; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

path="/data/web_static/releases/test"
path2="/data/web_static/shared"
sudo mkdir -p "$path"
sudo mkdir -p "$path2"

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee "$path/index.html"

symlink="/data/web_static/current"
if [ -L "$symlink" ]; then
    sudo rm "$symlink"
fi
sudo ln -sf "$path" /data/web_static/current

my_username=$(whoami)
sudo chown -R "$my_username":"$my_username" /data/
sudo sed -i "57i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default

sudo service nginx restart
