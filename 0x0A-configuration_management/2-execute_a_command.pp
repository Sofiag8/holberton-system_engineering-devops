# killing a process with a puppet manifest

exec { 'killmenow':
     path => '/usr/bin/',
     command => 'pkill -f ./killmenow',
}