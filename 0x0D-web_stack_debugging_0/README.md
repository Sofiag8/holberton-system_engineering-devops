<h1 class="gap">Project 0x0D. Web stack debugging #0</h1>

<h2>Background Context</h2>

<p>The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that&rsquo;s the &ldquo;fun&rdquo; part of the job!).</p>

<p>Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.</p>

<p>In this debugging series, broken/bugged webstacks will be given to you, the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, you should figure out what is going on and fix it manually.</p>

<p>Let&rsquo;s start with a very simple example. My server must: </p>

<ul>
<li>have a copy of the <code>/etc/passwd</code> file in <code>/tmp</code></li>
<li>have a file named <code>/tmp/isworking</code> containing the string <code>OK</code></li>
</ul>

<h2>Installing Docker</h2>

<p>For this project you will be given a container which you can use to solve the task. <strong>If</strong> you would like to have Docker so that you can experiment with it and/or solve this problem locally, you can install it on your machine, your Ubuntu 14.04 VM, or your Ubuntu 16.04 VM if you upgraded.</p>

<ul>
<li><a href="/rltoken/k_pbInP8sVHkPWS-7bUqDQ" title="Mac OS" target="_blank">Mac OS</a></li>
<li><a href="/rltoken/AYZe8xA3hfdHoDlXMJuNpQ" title="Windows" target="_blank">Windows</a></li>
<li><a href="/rltoken/ynOBcBBvuYZPm9lSHFNcoQ" title="Ubuntu 14.04" target="_blank">Ubuntu 14.04</a> (Note that Docker for Ubuntu 14 is deprecated and you will have to make some adjustments to the instructions when installing)</li>
<li><a href="/rltoken/tTuEaxo5gzKq23ZvgPODnA" title="Ubuntu 16.04" target="_blank">Ubuntu 16.04</a></li>
</ul>

<h2>Resources</h2>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>curl</code></li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash scripts must pass <code>Shellcheck</code> without any error</li>
<li>Your Bash scripts must run without error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

<hr class="gap">
<h2 class="gap">Tasks</h2>

 <h4 class="task">
    0. Give me a page!
</h4>
 <p>Be sure to read the <strong>Docker</strong> concept page</p>

<p>In this first debugging project, you will need to get <a href="/rltoken/B4vOap4dPNKxdZzBbepK7Q" title="Apache" target="_blank">Apache</a> to run on the container and to return a page containing <code>Hello Holberton</code> when querying the root of it.</p>

<p>After connecting to the container and fixing whatever needed to be fixed (here is your mission), you can see that curling port 80 return a page that contains <code>Hello Holberton</code>.
Paste the command(s) you used to fix the issue in your answer file.</p>