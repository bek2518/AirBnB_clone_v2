# Bash script that sets up webserver for deployment of web_static

exec { 'Installation':
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ;
    sudo service nginx start',
  provider => shell,
  before   => ['Create first directory'],
}

exec { 'Create first directory':
  command  => 'sudo mkdir -p /data/web-static/releases/test',
  provider => shell,
  before   => ['Create second directory']
}

exec { 'Create second directory':
  command  =>'sudo mkdir -p /data/web-static/shared',
  provider => shell,
  before   => ['Insert to file'],
}

file  { 'Insert to file':
  esnure  => file,
  path    => '/data/web_static/releases/test/index.html',
  content => 'Fake HTML file with simple content to test Nginx configuration',
  before  => Exec['link']
}

exec { 'link':
  command  => 'sudo ln -fs /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
  before   => Exec['Owner']
}

exec {'Owner':
  command  => 'sudo chown -R ubuntu:ubuntu /data',
  provider => shell,
  before   => Exec['Configuration'],
}

file { 'Configuration':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
  'server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                alias /data/web_static/current;
                try_files $uri $uri/ =404;
        }
    }',
  before  => ['restart service']
}

exec { 'restart service':
  provider => shell,
  command  => 'sudo service nginx restart'
  }
