# connecting to a server without using password
file_line { '/etc/ssh/ssh_config':,
     ensure => 'present'
     path   => '/etc/ssh/ssh_config',
     line   => 'PasswordAuthentication no; IdentifyFile ~/.ssh/holberton',
}