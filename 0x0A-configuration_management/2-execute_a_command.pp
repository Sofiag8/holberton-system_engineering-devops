# killing a process with a puppet manifest

exec { ' /usr/bin/env pkill -9 killmenow':
}