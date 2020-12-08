<h1 class="gap">Project 0x0B. SSH</h1>

    <h2>Background Context</h2>

<p>Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away.  Like level 2 of the application process, you will connect using <code>ssh</code>. But contrary to level 2, you will not connect using a password but an RSA key. We&rsquo;ve configured your server with the public key you created in the first task of <a href="/rltoken/LZ_8pMANOAmpn5-tiwqiJQ" title="a previous project" target="_blank">a previous project</a> shared in your <a href="/rltoken/l4Ao4ESbI_hMB6s4mjBKRw" title="intranet profile" target="_blank">intranet profile</a>.</p>

<p>You can access your server information in the <a href="/rltoken/owYhGMuyPTY4OyvSGJljGQ" title="my servers" target="_blank">my servers</a> section of the intranet, each line with contains the IP and username you should use to connect via <code>ssh</code>.</p>

<p><strong>Note:</strong> Your server is configured with an Ubuntu 16.04 LTS environment. You do <strong>not</strong> need to create a new virtual machine. If you decide you want to upgrade to Ubuntu 16.04, make sure to create a new VM. Do <strong>not</strong> attempt to upgrade your current Ubuntu 14.04 environment as that will inevitably be messy and can break things. Note that if you switch, none of your files and environment settings will be available and anything you need will have to be reinstalled or migrated.</p>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/yrpqgxdgQKwr3vYfhBpA_w" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a server</li>
<li>Where servers usually live</li>
<li>What is SSH</li>
<li>How to create an SSH RSA key pair</li>
<li>How to connect to a remote host using an SSH RSA key pair</li>
<li>The advantage of using  <code>#!/usr/bin/env bash</code> instead of <code>/bin/bash</code> </li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

<hr class="gap">
<h2 class="gap">Tasks</h2>

 <h4 class="task">
    0. Use a private key
</h4>
 <p>Write a Bash script that uses <code>ssh</code> to connect to your server using the private key <code>~/.ssh/holberton</code> with the user <code>ubuntu</code>.</p>

<p>Requirements:</p>

<ul>
<li>Only use <code>ssh</code> single-character flags</li>
<li>You cannot use <code>-l</code></li>
<li>You do not need to handle the case of a private key protected by a passphrase</li>
</ul>


 <h4 class="task">
    1. Create an SSH key pair
</h4>
<p>Write a Bash script that creates an RSA key pair.</p>

<p>Requirements:</p>

<ul>
<li>Name of the created private key must be <code>holberton</code></li>
<li>Number of bits in the created key to be created 4096</li>
<li>The created key must be protected by the passphrase <code>betty</code></li>
</ul>

<h4 class="task">
    2. Client configuration file
</h4>
 <p>Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let&rsquo;s configure it to our needs so that you can connect to a server without typing a password.
Share your SSH client configuration in your answer file.</p>

<p>Requirements:</p>

<ul>
<li>Your SSH client configuration must be configured to use the private key <code>~/.ssh/holberton</code></li>
<li>Your SSH client configuration must be configured to refuse to authenticate using a password</li>
</ul>

<h4 class="task">
    3. Let me in!
</h4>
<p>Now that you have successfully connected to your server, we would also like to join the party.</p>

<p>Add the SSH public key below to your server so that we can connect using the <code>ubuntu</code> user.</p>