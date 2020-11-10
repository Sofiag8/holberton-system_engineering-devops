<h1 class="gap">Project 0x07. Networking basics #0</h1>
<h2>Learning Objectives</h2>

<h3>OSI Model</h3>

<ul>
<li>What it is</li>
<li>How many layers it has</li>
<li>How it is organized</li>
</ul>

<h3>What is a LAN</h3>

<ul>
<li>Typical usage</li>
<li>Typical geographical size</li>
</ul>

<h3>What is a WAN</h3>

<ul>
<li>Typical usage</li>
<li>Typical geographical size</li>
</ul>

<h3>What is the Internet</h3>

<ul>
<li>What is an IP address</li>
<li>What are the 2 types of IP address</li>
<li>What is <code>localhost</code></li>
<li>What is a subnet</li>
<li>Why IPv6 was created</li>
</ul>

<h3>TCP/UDP</h3>

<ul>
<li>What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)</li>
<li>What is the main difference between TCP and UDP</li>
<li>What is a port</li>
<li>Memorize SSH, HTTP and HTTPS port numbers</li>
<li>What tool/protocol is often used to check if a device is connected to a network</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your Bash script files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>shellcheck</code> without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

<h2>More Info</h2>

<p>The second line of all your Bash scripts should be a comment explaining what is the script doing</p>

   <hr class="gap">
      <h2 class="gap">Tasks</h2>

<h4 class="task">
    0. OSI model
</h4>
<p>Questions:</p>

<p>What is the OSI model?</p>

<ol>
<li>Set of specifications that network hardware manufacturers must respect</li>
<li>The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology</li>
<li>The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology</li>
</ol>

<p>How is the OSI model organized?</p>

<ol>
<li> Alphabetically</li>
<li>From the lowest to the highest level</li>
<li>Randomly</li>
</ol>

<h4 class="task">
    1. Types of network
</h4>
<p>Questions:</p>

<p>What type of network are Holberton iMacs connected to?</p>

<ol>
<li>Internet</li>
<li>WAN</li>
<li>LAN</li>
</ol>

<p>What type of network could connect an office in one building to another office in a building a few streets away?</p>

<ol>
<li>Internet</li>
<li>WAN</li>
<li>LAN</li>
</ol>

<p>What network do you use when you browse www.holbertonschool.com from your smartphone (not connected to the Wifi)?</p>

<ol>
<li>Internet</li>
<li>WAN</li>
<li>LAN</li>
</ol>

<h4 class="task">
    2. MAC and IP address
  </h4>
<p>Questions:</p>

<p>What is a MAC address?</p>

<ol>
<li>The name of a network interface</li>
<li>The unique identifier of a network interface</li>
<li>A network interface</li>
</ol>

<p>What is an IP address?</p>

<ol>
<li>Is to devices connected to a network what postal address is to houses</li>
<li>The unique identifier of a network interface</li>
<li>Is a number that network devices use to connect to networks</li>
</ol>

<h4 class="task">
    3. UDP and TCP
</h4>
<p>Questions:</p>

<ul>
<li>Which statement is correct for the TCP box:

<ol>
<li><code>It is a protocol that is transferring data in a slow way but surely</code></li>
<li><code>It is a protocol that is transferring data in a fast way and might loss data along in the process</code></li>
</ol></li>
<li>Which statement is correct for the UDP box:

<ol>
<li><code>It is a protocol that is transferring data in a slow way but surely</code></li>
<li><code>It is a protocol that is transferring data in a fast way and might loss data along in the process</code></li>
</ol></li>
<li>Which statement is correct for the TCP worker:

<ol>
<li><code>Have you received boxes x, y, z?</code></li>
<li><code>May I increase the rate at which I am sending you boxes?</code></li>
</ol></li>
</ul>

  <h4 class="task">
    4. TCP and UDP ports
  </h4>
 <p>Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.</p>

<p>If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.</p>

<p>While the full list of ports should not be memorized, it is important to know the most used ports, let&rsquo;s start by remembering 3 of them:</p>

<ul>
<li><strong>22</strong> for SSH</li>
<li><strong>80</strong> for HTTP</li>
<li><strong>443</strong> for HTTPS</li>
</ul>

<p>Write a Bash script that displays listening ports:</p>

<ul>
<li>That only shows listening sockets</li>
<li>That shows the PID and name of the program to which each socket belongs</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ sudo ./4-TCP_and_UDP_ports
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 *:sunrpc                *:*                     LISTEN      518/rpcbind
tcp        0      0 *:ssh                   *:*                     LISTEN      1240/sshd
tcp        0      0 *:32938                 *:*                     LISTEN      547/rpc.statd
tcp6       0      0 [::]:sunrpc             [::]:*                  LISTEN      518/rpcbind
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      1240/sshd
tcp6       0      0 [::]:33737              [::]:*                  LISTEN      547/rpc.statd
udp        0      0 *:sunrpc                *:*                                 518/rpcbind
udp        0      0 *:691                   *:*                                 518/rpcbind
udp        0      0 localhost:723           *:*                                 547/rpc.statd
udp        0      0 *:60129                 *:*                                 547/rpc.statd
udp        0      0 *:3845                  *:*                                 562/dhclient
udp        0      0 *:bootpc                *:*                                 562/dhclient
udp6       0      0 [::]:47444              [::]:*                              547/rpc.statd
udp6       0      0 [::]:sunrpc             [::]:*                              518/rpcbind
udp6       0      0 [::]:50038              [::]:*                              562/dhclient
udp6       0      0 [::]:691                [::]:*                              518/rpcbind
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
unix  2      [ ACC ]     STREAM     LISTENING     7724     518/rpcbind         /run/rpcbind.sock
unix  2      [ ACC ]     STREAM     LISTENING     6525     1/init              @/com/ubuntu/upstart
unix  2      [ ACC ]     STREAM     LISTENING     8559     835/dbus-daemon     /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     9190     1087/acpid          /var/run/acpid.socket
unix  2      [ ACC ]     SEQPACKET  LISTENING     7156     378/systemd-udevd   /run/udev/control
sylvain@ubuntu$
</code></pre>

<h4 class="task">
    5. Is the host on the network
  </h4>
<p>The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command <code>ping</code> uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network. </p>

<p>Write a Bash script that pings an IP address passed as an argument.</p>

<p>Requirements: </p>

<ul>
<li>Accepts a string as an argument</li>
<li>Displays <code>Usage: 5-is_the_host_on_the_network {IP_ADDRESS}</code> if no argument passed</li>
<li>Ping the IP 5 times</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ./5-is_the_host_on_the_network 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=12.9 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=13.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=7.83 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=63 time=11.3 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=63 time=7.57 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 7.570/10.682/13.679/2.546 ms
sylvain@ubuntu$
sylvain@ubuntu$ ./5-is_the_host_on_the_network
Usage: 5-is_the_host_on_the_network {IP_ADDRESS}
sylvain@ubuntu$ 
</code></pre>

