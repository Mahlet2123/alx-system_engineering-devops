# Installs a Nginx server

# define the package to install
package { 'nginx':
  ensure => installed,
}

#define the service to manage
service { 'nginx':
  ensure => running,
  enable => true,
}

#define the nginx configuration
file { '/etc/nginx/sites-available/default':
  content => "
  server {
    listen 80;
    server_name localhost;

  location / {
    root /var/www/html;
    index index.html;
    return 301 https://example.com;
  }

  location /redirect_me {
    return 301 https://example.com/new_location;
  }
}
"
  require => Package['nginx'],
  notify  => Service['nginx'],
}

#define the index.html file to serve
file { '/var/www/html/index.html':
  content => Hello World!,
  require => Package['nginx'],
}
