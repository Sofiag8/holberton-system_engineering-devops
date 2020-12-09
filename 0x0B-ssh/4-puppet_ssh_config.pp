# connecting to a server without
# using password
file_line {' password off':
     ensure => 'present',
     path   => '/etc/ssh/ssh_config',
     line   => 'PasswordAuthentication no',
     match  => 'PasswordAuthentication yes',
}
file_line { 'server connection':,
     ensure => 'present'
     path   => '/etc/ssh/ssh_config',
     line   => 'IdentifyFile ~/.ssh/holberton',
}