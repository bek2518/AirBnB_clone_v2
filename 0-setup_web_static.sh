#!/usr/bin/env bash
# Bash script that sets up webserver for deployment of web_static

if [ ! -x /usr/sbin/nginx ]
then
	sudo apt -y update
	sudo apt -y install nginx
	sudo service nginx start
fi

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "Fake HTML file with simple content to test Nginx configuration" > /data/web_static/release/test/index.html
ln -fs /data/web_static/release/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data

CONFIG=\
'\\t\tlocation /hbnb_static/ {\n\t\t\t\talias /data/web_static/current/; \n\t\t}\n'
sudo sed -i "43i $CONFIG" /etc/nginx/sites-available/default

sudo service nginx restart
