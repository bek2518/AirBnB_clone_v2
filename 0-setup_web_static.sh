#!/usr/bin/env bash
# Bash script that sets up webserver for deployment of web_static

sudo apt -y update
sudo apt -y install nginx
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "Fake HTML file with simple content to test Nginx configuration" > /data/web_static/release/test/index.html
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data

CONFIG=\
'\\t\tlocation /hbnb_static/ {\n\t\t\t\talias /data/web_static/current/; \n\t\t}\n'
sudo sed -i "40i $CONFIG" /etc/nginx/sites-available/default

sudo service nginx restart
