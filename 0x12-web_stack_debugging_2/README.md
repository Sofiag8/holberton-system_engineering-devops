<h1 class="gap">Projects 0x12. Web stack debugging #2</h1>
<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A README.md file at the root of the folder of the project is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash scripts must pass <code>Shellcheck</code> without any error</li>
<li>Your Bash scripts must run without error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>


<hr class="gap">
<h2 class="gap">Tasks</h2>
  <h4 class="task">
    0. Run software as another user
</h4>
<p>The user <code>root</code> is, on Linux, the &ldquo;superuser&rdquo;. It can do anything it wants, that&rsquo;s a good and bad thing. A good practice is that one should never be logged in the <code>root</code> user, as if you fat finger a command and for example run <code>rm -rf /</code>, there is no comeback. That&rsquo;s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the <code>root</code> user can do, just need to use a specific command that you need to discover.</p>

<p>For the containers that you are given in this project as well as the checker, everything is run under the <code>root</code> user, which has the ability to run anything as another user.</p>

<p>Requirements:</p>

<ul>
<li>write a Bash script that accepts one argument</li>
<li>the script should run the <code>whoami</code> command under the user passed as an argument</li>
<li>make sure to try your script by passing different users</li>
</ul>

  <h4 class="task">
    1. Run Nginx as Nginx
</h4>
  <p>The <code>root</code> user is a superuser that can do anything on a Unix machine, the top administrator. Security wise, you must do everything that you can to prevent an attacker from logging in as <code>root</code>. With this in mind, it&rsquo;s a good practice not to run your web servers as <code>root</code> (which is the default for most configurations) and instead run the process as the less privileged <code>nginx</code> user instead. This way, if a hacker does find a security issue that allows them to break-in to your server, the impact is limited by the permissions of the <code>nginx</code> user.</p>

<p>Fix this container so that Nginx is running as the <code>nginx</code> user.</p>

<p>Requirements:</p>

<ul>
<li><code>nginx</code> must be running as <code>nginx</code> user</li>
<li><code>nginx</code> must be listening on all active IPs on port <code>8080</code></li>
<li>You cannot use <code>apt-get remove</code></li>
<li>Write a Bash script that configures the container to fit the above requirements</li>
</ul>

<p>After debugging:</p>

<pre><code>root@ab6f4542747e:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
root@ab6f4542747e:~#
root@ab6f4542747e:~# nc -z 0 8080 ; echo $?
0
root@ab6f4542747e:~#
</code></pre>
