# Bash script that sets up webserver for deployment of web_static

exec { 'Installation':
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; sudo service nginx start ;
    sudo mkdir -p /data/web-static/releases/test ; sudo mkdir -p /data/web-static/shared ;
    echo "Fake HTML file with simple content to test Nginx configuration" > /data/web_static/releases/test/index.html
    ; sudo ln -fs /data/web_static/releases/test/ /data/web_static/current ;
    sudo chown -R ubuntu:ubuntu /data ; 
    sudo sed -i "40i\\t\tlocation /hbnb_static/ {\n\t\t\t\talias /data/web_static/current/; \n\t\t}\n" /etc/nginx/sites-available/default ;
    sudo service nginx restart',
  provider => shell,
}
