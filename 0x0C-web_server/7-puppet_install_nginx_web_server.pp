# Installs a Nginx server

# define the package to install
package { 'nginx':
  ensure => installed,
}

#write 'Hello World!' to the index.html file 
file { '/var/www/html/index.html':
  content => Hello World!,
}

# Configure Nginx to listen on port 80 and perform a redirect
class { 'nginx':
  default_site_enabled => true,
}

nginx::resource::vhost { 'default':
  listen_port => '80',
  proxy       => false,
  rewrite     => [
    '^/redirect_me https://www.youtube.com permanent',
  ],
}

# Start Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}
