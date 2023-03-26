# Puppet to make changes to our configuration file

file { 'config':
  ensure  => file,
  path    => '~/.ssh/config',
  content => '

Host *
    PasswordAuthentication no

Host myserver
    Hostname 54.90.3.149
    User ubuntu
    IdentityFile ~/.ssh/school
',
}
