# Installs a Nginx server

exec {'/usr/bin/env apt-get -y update': }
exec {'/usr/bin/env apt-get -y install nginx': }
exec {'/usr/bin/env echo "Hellow World" > /var/www/html/index.html': }
exec {'/usr/bin/env sed -i "/server_name _;/ a\\\trewrite ^/redirect_me https://www.youtube.com permanent;" /etc/nginx/sites-available/default': }
exec {'/usr/bin/env sed -i "/server_name _;/ a\\\terror_page 404 /404.html;" /etc/nginx/sites-available/default': }
exec {'/usr/bin/env echo "Ceci n\'est pas une page" > /var/www/html/404.html': }
exec {'/usr/bin/env service nginx start': }
