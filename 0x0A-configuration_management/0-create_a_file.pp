# create a file in /tmp

file { 'school':
  path    => '/tmp/school',
  ensure  => file,
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
