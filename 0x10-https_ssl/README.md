<h1 class="gap">Project 0x10. HTTPS SSL</h1>

<h2>Learning Objectives</h2>
<h3>General</h3>

<ul>
<li>What is HTTPS SSL 2 main roles</li>
<li>What is the purpose encrypting traffic</li>
<li>What SSL termination means</li>
</ul>

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
    0. HTTPS ABC
</h4>
  <p>As for project <a href="/rltoken/yZFuXOcQDP7ceusbLCr3Dw" title="0x07" target="_blank">0x07</a>, use numbers in your answer file.</p>

<p>What is HTTPS?</p>

<ol>
<li>A secure version of HTTP</li>
<li>A faster version of HTTP</li>
<li>A superior version of HTTP</li>
</ol>

<p>Why do you need HTTPS?</p>

<ol>
<li>To encrypt credit card and social security number information going between the client and the website servers</li>
<li>To encrypt all communication between the client and the website servers</li>
<li>To accelerate the communication between the client and the website servers</li>
</ol>

<p>You want to setup HTTPS on your website, where shall you place the certificate?</p>

<ol>
<li>In a secure location where nobody can access it</li>
<li>You can host it anywhere but you have to share the link to it on your website</li>
<li>On your website web server(s)</li>
</ol>

  <h4 class="task">
    1. World wide web
</h4>
  <p>Configure your domain zone so that the subdomain <code>www</code> points to your load-balancer IP (<code>lb-01</code>).
Let&rsquo;s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.</p>

<p>Requirements:</p>

<ul>
<li>Add the subdomain <code>www</code> to your domain, point it to your <code>lb-01</code> IP (your domain name might  be configured with default subdomains, feel free to remove them)</li>
<li>Add the subdomain <code>lb-01</code> to your domain, point it to your <code>lb-01</code> IP</li>
<li>Add the subdomain <code>web-01</code> to your domain, point it to your <code>web-01</code> IP</li>
<li>Add the subdomain <code>web-02</code> to your domain, point it to your <code>web-02</code> IP</li>
<li>Your Bash script must accept 2 arguments:

<ol>
<li><code>domain</code>:

<ul>
<li> type: string</li>
<li> what: domain name to audit</li>
<li>mandatory: yes</li>
</ul></li>
<li><code>subdomain</code>:

<ul>
<li>type: string</li>
<li>what: specific subdomain to audit</li>
<li>mandatory: no</li>
</ul></li>
</ol></li>
<li>Output:  <code>The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]</code></li>
<li>When only the parameter <code>domain</code> is provided, display information for its subdomains <code>www</code>, <code>lb-01</code>, <code>web-01</code> and <code>web-02</code> - in this specific order</li>
<li>When passing <code>domain</code> and <code>subdomain</code> parameters, display information for the specified subdomain</li>
<li>Ignore <code>shellcheck</code> case <code>SC2086</code></li>
<li>Must use: 

<ul>
<li><code>awk</code></li>
<li>at least one Bash function</li>
</ul></li>
<li>You do not need to handle edge cases such as:

<ul>
<li>Empty parameters </li>
<li>Nonexistent domain names</li>
<li>Nonexistent subdomains</li>
</ul></li>
</ul>

 <h4 class="task">
    2. HAproxy SSL termination
</h4>
<p>&ldquo;Terminating SSL on HAproxy&rdquo; means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.</p>

<p>Create a certificate using <code>certbot</code> and configure <code>HAproxy</code> to accept encrypted traffic for your subdomain <code>www.</code>.</p>

<p>Requirements:</p>

<ul>
<li>HAproxy must be listening on port TCP 443</li>
<li>HAproxy must be accepting SSL traffic</li>
<li>HAproxy must serve encrypted traffic that will return the <code>/</code> of your web server</li>
<li>When querying the root of your domain name, the page returned must contain <code>Holberton School</code></li>
<li>Share your HAproxy config as an answer file (<code>/etc/haproxy/haproxy.cfg</code>)</li>
</ul>

<p>The file <code>2-haproxy_ssl_termination</code> must be your HAproxy configuration file</p>

<p>Make sure to install HAproxy 1.5 or higher, <a href="/rltoken/VFq2MQ9qHXw2Nb11tnWF6Q" title="SSL termination" target="_blank">SSL termination</a> is not available before v1.5.</p>