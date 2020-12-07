# killing a process with a puppet manifest

exec { "killmenow":
     command => "pkill -f ./killmenow",
     path    => "/usr/bin/",
}