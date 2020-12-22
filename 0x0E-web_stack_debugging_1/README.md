<h1 class="gap">Project 0x0E. Web stack debugging #1</h1>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file at the root of the folder of the project is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash scripts must pass <code>Shellcheck</code> without any error</li>
<li>Your Bash scripts must run without error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
<li>You are not allowed to use <code>wget</code></li>
</ul>

<hr class="gap">
<h2 class="gap">Tasks</h2>

 <h4 class="task">
    0. Nginx likes port 80
</h4>
 <p>Using your debugging skills, find out what&rsquo;s keeping your Ubuntu container&rsquo;s Nginx installation from listening on port <code>80</code>. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.</p>

<p>Requirements:</p>

<ul>
<li>Nginx must be running, and listening on port <code>80</code> of all the server&rsquo;s active IPv4 IPs </li>
<li>Write a Bash script that configures a server to the above requirements</li>
</ul>