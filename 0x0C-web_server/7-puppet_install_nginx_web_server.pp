# Installs a Nginx server

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ;',
}

exec {'/usr/bin/env echo "Hellow World" > /var/www/html/index.html': }
exec {'/usr/bin/env sed -i "/server_name _;/ a\\\trewrite ^/redirect_me http://www.holbertonschool.com permanent;" /etc/nginx/sites-available/default': }
exec {'/usr/bin/env sed -i "/server_name _;/ a\\\terror_page 404 /custom_404.html;" /etc/nginx/sites-available/default': }
exec {'/usr/bin/env echo "Ceci n\'est pas une page" > /var/www/html/custom_404.html': }
exec {'/usr/bin/env service nginx start': }
