<h1 class="gap">Project 0x0F. Load balancer</h1>
<h2>Background Context</h2>

<p>You have been given 2 additional servers:</p>

<ul>
<li>gc-[STUDENT_ID]-web-02-XXXXXXXXXX</li>
<li>gc-[STUDENT_ID]-lb-01-XXXXXXXXXX</li>
</ul>

<p>Let&rsquo;s improve our web stack so that there is a redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.</p>

<p>For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.</p>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.7</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

<hr class="gap">
<h2 class="gap">Tasks</h2>
 <h4 class="task">
    0. Double the number of webservers
</h4>

  <p>In this first task you need to configure <code>web-02</code> to be identical to <code>web-01</code>. Fortunately, you built a Bash script during your <a href="/rltoken/YygI112jB085j-4C3dRX2A" title="web server project" target="_blank">web server project</a>, and they&rsquo;ll now come in handy to easily configure <code>web-02</code>. Remember, always try to automate your work!</p>

<p>Since we&rsquo;re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.</p>

<p>Requirements:</p>

<ul>
<li>Configure Nginx so that its HTTP response contains a custom header (on <code>web-01</code> and <code>web-02</code>)

<ul>
<li>The name of the custom HTTP header must be <code>X-Served-By</code></li>
<li>The value of the custom HTTP header must be the hostname of the server Nginx is running on</li>
</ul></li>
<li>Write <code>0-custom_http_response_header</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task

<ul>
<li><a href="/rltoken/3AOvROMUNUrzxEWhli4GTw" title="Ignore" target="_blank">Ignore</a> <a href="/rltoken/i5f8DYX_rRYFz4hfbG_GJg" title="SC2154" target="_blank">SC2154</a> for <code>shellcheck</code></li>
</ul></li>
</ul>


  <h4 class="task">
    1. Install your load balancer
</h4>
 <p>Install and configure HAproxy on your <code>lb-01</code> server.</p>

<p>Requirements:</p>

<ul>
<li>Configure HAproxy with version equal or greater than 1.5 so that it send traffic to <code>web-01</code> and <code>web-02</code></li>
<li>Distribute requests using a roundrobin algorithm</li>
<li>Make sure that HAproxy can be managed via an init script</li>
<li>Make sure that your servers are configured with the right hostnames: <code>[STUDENT_ID]-web-01</code> and <code>[STUDENT_ID]-web-02</code>. If not, follow this <a href="/rltoken/Tb9qeqRrtrO_b2uFpet9rw" title="tutorial" target="_blank">tutorial</a>.</li>
<li>For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements</li>
</ul>

