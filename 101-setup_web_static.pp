# Bash script that sets up webserver for deployment of web_static

exec { 'Installation':
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ;
    sudo service nginx start',
  provider => shell,
}

exec { 'Create directories':
  command  => 'sudo mkdir -p /data/web-static/releases/test ;
    sudo mkdir -p /data/web-static/shared',
  provider => shell,
}

file  { 'Insert to file'
  esnure  => file,
  path    => '/data/web_static/releases/test/index.html',
  content => 'Fake HTML file with simple content to test Nginx configuration',
}

exec { 'link and owner':
  command  => 'sudo ln -fs /data/web_static/releases/test/ /data/web_static/current ;
    sudo chown -R ubuntu:ubuntu /data',
  provider => shell,
}

exec { 'Insert':
  command  =>'sudo sed -i "40i\\t\tlocation /hbnb_static/ {\n\t\t\t\talias /data/web_static/current/; \n\t\t}\n" /etc/nginx/sites-available/default',
  provider => shell,
}

exec { 'restart service':
  provider => shell,
  command  => 'sudo service nginx restart'
  }
