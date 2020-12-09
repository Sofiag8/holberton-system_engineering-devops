<h1 class="gap"> Project 0x0C. Web server</h1>
<h2>Background Context</h2>
<p>In this project, some of the tasks will be graded on 2 aspects:</p>

<ol>
<li>Is your <code>web-01</code> server configured according to requirements</li>
<li>Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)</li>
</ol>

<p>For example, if I need to create a file <code>/tmp/test</code> containing the string <code>hello world</code> and modify the configuration of Nginx to listen on port <code>8080</code> instead of <code>80</code>, I can use <code>emacs</code> on my server to create the file and to modify the Nginx configuration file <code>/etc/nginx/sites-enabled/default</code>.</p>

<p>But my answer file would contain:</p>

<pre><code>sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world &gt; /tmp/test
sed -i &#39;s/80/8080/g&#39; /etc/nginx/sites-enabled/default
sylvain@ubuntu
</code></pre>

<p>As you can tell, I am not using <code>emacs</code> to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an <a href="/rltoken/Hjv9yJQtW6X7VRa2ByMeEg" title="SRE" target="_blank">SRE</a>, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the <code>root</code> user, you do not need to use the <code>sudo</code> command.</p>

<p>A good Software Engineer is a <a href="/rltoken/y1MX-uAX-0a4bgXfH3uweQ" title="lazy Software Engineer" target="_blank">lazy Software Engineer</a>.
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg" alt="" style="" /></p>

<p>Tips: to test your answer Bash script, feel free to reproduce the checker environment: </p>

<ul>
<li>start an <code>ubuntu:16.04</code> Docker container</li>
<li>run your script on it</li>
<li>see how it behaves</li>
</ul>

<p>Check out the Docker concept page for more info about how to manipulate containers.</p>

<h2>Learning Objectives</h2>
<h3>General</h3>

<ul>
<li>What is the main role of a web server</li>
<li>What is a child process</li>
<li>Why web servers usually have a parent process and child processes</li>
<li>What are the main HTTP requests</li>
</ul>

<h3>DNS</h3>

<ul>
<li>What DNS stands for</li>
<li>What is DNS main role</li>
</ul>

<h3>DNS Record Types</h3>

<ul>
<li><code>A</code></li>
<li><code>CNAME</code></li>
<li><code>TXT</code></li>
<li><code>MX</code></li>
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
<li>You can&rsquo;t use <code>systemctl</code> for restarting a process</li>
</ul>

<hr class="gap">
<h2 class="gap">Tasks</h2>
 <h4 class="task">
    0. Transfer a file to your server
</h4>
 <p>Write a Bash script that transfers a file from our client to a server:</p>

<p>Requirements:</p>

<ul>
<li>Accepts 4 parameters

<ol>
<li>The path to the file to be transferred</li>
<li>The IP of the server we want to transfer the file to</li>
<li>The username <code>scp</code> connects with</li>
<li>The path to the SSH private key that <code>scp</code> uses</li>
</ol></li>
<li>Display <code>Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY</code> if less than 3 parameters passed</li>
<li><code>scp</code> must transfer the file to the user home directory <code>~/</code></li>
<li>Strict host key checking must be disabled when using <code>scp</code> </li>
</ul>

 <h4 class="task">
    1. Install nginx web server
</h4>
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/01cab59e881e31842b8d47a0974e8d3b6f0f2001.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201209%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201209T022039Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=41b847cbdef605e2fbb936bfa5353f200ec2b5591434a38ebad3e4a686447296" alt="" style="" /></p>

<p>Readme:</p>

<ul>
<li><a href="/rltoken/qU2tVilKLygFZcRpEWD3lw" title="-y on apt-get command" target="_blank">-y on apt-get command</a></li>
</ul>

<p>Web servers are the piece of software generating and serving HTML pages, let&rsquo;s install one!</p>

<p>Requirements:</p>

<ul>
<li>Install <code>nginx</code> on your <code>web-01</code> server</li>
<li>Nginx should be listening on port 80</li>
<li>When querying Nginx at its root <code>/</code> with a GET request (requesting a page)  using <code>curl</code>, it must return a page that contains the string <code>Holberton School</code></li>
<li>As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)</li>
<li>You can&rsquo;t use <code>systemctl</code> for restarting <code>nginx</code></li>
</ul>

 <h4 class="task">
    2. Setup a domain name
</h4>
<p><a href="/rltoken/yRrwiHrS15iQQZku72p0aQ" title=".TECH Domains" target="_blank">.TECH Domains</a> is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with .TECH Domains so that you can learn about DNS.</p>

<p>.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your <a href="/rltoken/b-Y81kiPBFJ_6wxJaSmBgQ" title="tools space" target="_blank">tools space</a>. Feel free to drop a thank you tweet for <a href="/rltoken/d9XjYlM-CqTRHJEcaKpcVQ" title=".TECH Domains" target="_blank">.TECH Domains</a>.</p>

<p>Provide the domain name in your answer file.</p>

<p>Requirement:</p>

<ul>
<li>provide the domain name only (example: <code>foobar.tech</code>), no subdomain (example: <code>www.foobar.tech</code>)</li>
<li>configure your DNS records with an A entry so that your root domain points to your <code>web-01</code> IP address <strong>Warning: the propagation of your records can take time (~1-2 hours)</strong></li>
<li>go to <a href="/rltoken/7s2XnwohTKBNE8c_ibAt4g" title="your profile" target="_blank">your profile</a> and enter your domain in the <code>Project website url</code> field</li>
</ul>

 <h4 class="task">
    3. Redirection
</h4>
 <p>Readme:</p>

<ul>
<li><a href="/rltoken/Afg1zCifjmIygL1se0ghhg" title="Replace a line with multiple lines with sed" target="_blank">Replace a line with multiple lines with sed</a></li>
</ul>

<p>Configure your Nginx server so that <code>/redirect_me</code> is redirecting to another page.</p>

<p>Requirements:</p>

<ul>
<li>The redirection must be a &ldquo;301 Moved Permanently&rdquo;</li>
<li>You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements</li>
<li>Using what you did with <code>1-install_nginx_web_server</code>, write <code>3-redirection</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
</ul>

  <h4 class="task">
    4. Not found page 404
</h4>
 <p>Configure your Nginx server to have a custom 404 page that contains the string <code>Ceci n&#39;est pas une page</code>.</p>

<p>Requirements:</p>

<ul>
<li>The page must return an HTTP 404 error code</li>
<li>The page must contain the string <code>Ceci n&#39;est pas une page</code></li>
<li>Using what you did with <code>3-redirection</code>, write <code>4-not_found_page_404</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
</ul>