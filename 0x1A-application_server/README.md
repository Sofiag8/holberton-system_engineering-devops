<h1 class="gap">0x1A. Application server</h1>

<h2>Background Context</h2>
<p>Your web infrastructure is already serving web pages via <code>Nginx</code> that you installed in your <a href="https://intranet.hbtn.io/projects/266" title="first web stack project" target="_blank">first web stack project</a>. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your <code>Nginx</code> and make is serve your Airbnb clone project.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/RerpYBxsgrpIorHjbDgulw" title="Application server vs web server" target="_blank">Application server vs web server</a> </li>
<li><a href="/rltoken/uosy5QXdMbDPA1tFTR1eoA" title="How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04" target="_blank">How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04</a> (As mentioned in the video, do <strong>not</strong> install Gunicorn using <code>virtualenv</code>, just install everything globally)</li>
<li><a href="/rltoken/QTnnkj6vfQV9ovW_eYWWDQ" title="Running Gunicorn" target="_blank">Running Gunicorn</a> </li>
<li><a href="/rltoken/whE8do28ZiJJoJLyb1ACwA" title="Be careful with the way Flask manages slash" target="_blank">Be careful with the way Flask manages slash</a> in <a href="/rltoken/JLjrXD4MLS3rUkQr5QyxtA" title="route" target="_blank">route</a>  - <code>strict_slashes</code></li>
<li><a href="/rltoken/oQPs-o5UUcZkxOw5sNIM0g" title="Upstart documentation" target="_blank">Upstart documentation</a> </li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Everything Python-related must be done using <code>python3</code></li>
<li>All config files must have comments</li>
</ul>

<h3>Bash Scripts</h3>

<ul>
<li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
<li>All your files should end with a new line</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.7-5~ubuntu16.04.1</code> via <code>apt-get</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

<hr class="gap">
<h2 class="gap">Tasks</h2>

<h4 class="task">
    0. Set up development with Python
</h4>

<p>Let&rsquo;s serve what you built for <a href="https://intranet.hbtn.io/projects/290" title="AirBnB clone v2 - Web framework" target="_blank">AirBnB clone v2 - Web framework</a> on <code>web-01</code>. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.</p>

<p>Requirements:</p>

<ul>
<li>Make sure that <a href="https://intranet.hbtn.io/tasks/1372" title="task #3" target="_blank">task #3</a> of your <a href="https://intranet.hbtn.io/projects/244" title="SSH project" target="_blank">SSH project</a> is completed for <code>web-01</code>.  The checker will connect to your servers.</li>
<li>Git clone your <code>AirBnB_clone_v2</code> on your <code>web-01</code> server.</li>
<li>Configure the file <code>web_flask/0-hello_route.py</code> to serve its content from the route <code>/airbnb-onepage/</code> on port <code>5000</code>.</li>
<li>Your Flask application object must be named <code>app</code> (This will allow us to run and check your code).</li>
</ul>

<h4 class="task">
    1. Set up production with Gunicorn
</h4>
 <p>Now that you have your development environment set up, let&rsquo;s get your production application server set up with <code>Gunicorn</code> on <code>web-01</code>, port <code>5000</code>. You&rsquo;ll need to install <code>Gunicorn</code> and any libraries required by your application. Your <code>Flask</code> application object will serve as a <a href="https://www.fullstackpython.com/wsgi-servers.html" title="WSGI" target="_blank">WSGI</a> entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.</p>

<p>Requirements:</p>

<ul>
<li>Install <code>Gunicorn</code> and any other libraries required by your application.</li>
<li>The Flask application object should be called <code>app</code>. (This will allow us to run and check your code)</li>
<li>You will serve the same content from the same route as in the previous task. You can verify that it&rsquo;s working by binding a <code>Gunicorn</code> instance to localhost listening on port <code>5000</code> with your application object as the entry point.</li>
<li>In order to check your code, the checker will bind a <code>Gunicorn</code> instance to port <code>6000</code>, so make sure nothing is listening on that port.</li>
</ul>


<h4 class="task">
    2. Serve a page with Nginx
</h4>
 <p>Building on your work in the previous tasks, configure <code>Nginx</code> to serve your page from the route <code>/airbnb-onepage/</code></p>

<p>Requirements:</p>

<ul>
<li><code>Nginx</code> must serve this page both locally and on its public IP on port <code>80</code>.</li>
<li><code>Nginx</code> should proxy requests to the process listening on port <code>5000</code>.</li>
<li>Include your <code>Nginx</code> config file as <code>2-app_server-nginx_config</code>.</li>
</ul>

<p>Notes:</p>

<ul>
<li>In order to test this you&rsquo;ll have to spin up either your production or development application server (listening on port <code>5000</code>)</li>
<li>In an actual production environment the application server will be configured to start upon startup in a system initialization script. This will be covered in the advanced tasks.</li>
<li>You will probably need to <code>reboot</code> your server (by using the command <code>$ sudo reboot</code>) to have Nginx publicly accessible</li>
</ul>

<h4 class="task">
    3. Add a route with query parameters
</h4>

  <p>Building on what you did in the previous tasks, let&rsquo;s expand our web application by adding another service for <code>Gunicorn</code> to handle. In <code>AirBnB_clone_v2/web_flask/6-number_odd_or_even</code>, the route <code>/number_odd_or_even/&lt;int:n&gt;</code> should already be defined to render a page telling you whether an integer is odd or even. You&rsquo;ll need to configure <code>Nginx</code> to proxy HTTP requests to the route <code>/airbnb-dynamic/number_odd_or_even/(any integer)</code> to a <code>Gunicorn</code> instance listening on port <code>5001</code>. The key to this exercise is getting <code>Nginx</code> configured to proxy requests to processes listening on two different ports. You are not expected to keep your application server processes running. If you want to know how to run multiple instances of <code>Gunicorn</code> without having multiple terminals open, see tips below.</p>

<p>Requirements:</p>

<ul>
<li><code>Nginx</code> must serve this page both locally and on its public IP on port <code>80</code>.</li>
<li><code>Nginx</code> should proxy requests to the route <code>/airbnb-dynamic/number_odd_or_even/(any integer)</code> the process listening on port <code>5001</code>.</li>
<li>Include your <code>Nginx</code> config file as <code>3-app_server-nginx_config</code>.</li>
</ul>

<h4 class="task">
    4. Let&#39;s do this for your API
</h4>
<p>Let&rsquo;s serve what you built for <a href="https://intranet.hbtn.io/projects/301" title="AirBnB clone v3 - RESTful API" target="_blank">AirBnB clone v3 - RESTful API</a> on <code>web-01</code>.</p>

<p>Requirements:</p>

<ul>
<li>Git clone your <code>AirBnB_clone_v3</code></li>
<li>Setup <code>Nginx</code> so that the route <code>/api/</code> points to a <code>Gunicorn</code> instance listening on port <code>5002</code></li>
<li><code>Nginx</code> must serve this page both locally and on its public IP on port <code>80</code></li>
<li>To test your setup you should bind <code>Gunicorn</code> to <code>api/v1/app.py</code></li>
<li>It may be helpful to import your data (and environment variables) from <a href="/rltoken/r3mnHZ7LoLJVF8JNxstDrQ" title="this project" target="_blank">this project</a></li>
<li>Upload your <code>Nginx</code> config file as <code>4-app_server-nginx_config</code></li>
</ul>

<h4 class="task">
    5. Serve your AirBnB clone
</h4>
 <p>Let&rsquo;s serve what you built for <a href="/rltoken/qOjECpMUaEXf4D0uoqHmQw" title="AirBnB clone - Web dynamic" target="_blank">AirBnB clone - Web dynamic</a> on <code>web-01</code>.</p>

<p>Requirements:</p>

<ul>
<li>Git clone your <code>AirBnB_clone_v4</code></li>
<li>Your <code>Gunicorn</code> instance should serve content from <code>web_dynamic/2-hbnb.py</code> on port <code>5003</code></li>
<li>Setup <code>Nginx</code> so that the route <code>/</code> points to your <code>Gunicorn</code> instance</li>
<li>Setup <code>Nginx</code> so that it properly serves the static assets found in <code>web_dynamic/static/</code> (this is essential for your page to render properly)</li>
<li>For your website to be fully functional, you will need to reconfigure <code>web_dynamic/static/scripts/2-hbnb.js</code> to the correct IP</li>
<li><code>Nginx</code> must serve this page both locally and on its public IP and port <code>5003</code></li>
<li>Make sure to pull up your Developer Tools on your favorite browser to verify that you have no errors</li>
<li>Upload your <code>Nginx</code> config  as <code>5-app_server-nginx_config</code></li>
</ul>

