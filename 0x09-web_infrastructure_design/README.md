<h1 class="gap">Project 0x09. Web infrastructure design</h1>
  <div class="gap formatted-content">
      <p style="margin-bottom: 0"><em>For this project, we are expected to look at these concepts:</em></p>
      <ul style="margin-top: 5px">
          <li>
            <em><a href="/concepts/12">DNS</a></em>
          </li>
          <li>
            <em><a href="/concepts/13">Monitoring</a></em>
          </li>
          <li>
            <em><a href="/concepts/17">Web Server</a></em>
          </li>
          <li>
            <em><a href="/concepts/33">Network basics</a></em>
          </li>
          <li>
            <em><a href="/concepts/46">Load balancer</a></em>
          </li>
          <li>
            <em><a href="/concepts/67">Server</a></em>
          </li>
      </ul>
    </div>

<h2>Learning Objectives</h2>
<p> At the end of this project I should be able to explain the following</p>
<h3>General</h3>

<ul>
<li>You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects</li>
<li>You must be able to explain what each component is doing</li>
<li>You must be able to explain system redundancy</li>
<li>Know all the mentioned acronyms: LAMP, SPOF, QPS</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>For each task, once you are done whiteboarding (on a whiteboard, piece of paper or software or your choice), take a picture/screenshot of your diagram</li>
<li>This project will be manually reviewed:</li>
<li>As each task is completed, the name of that task will turn green</li>
<li>Upload a screenshot, showing that you completed the required levels, to any image hosting service (I personally use <a href="/rltoken/QorG0rvw1PzqWBVrqWW6Sg" title="imgur" target="_blank">imgur</a> but feel free to use anything you want). </li>
<li>For the following tasks, insert the link from of your screenshot into the answer file </li>
<li>After pushing your answer file to Github, insert the Github file link into the URL box</li>
<li>You will also have to whiteboard each task in front of a mentor, staff or student - no computer or notes will be allowed during the whiteboarding session</li>
<li>Focus on what you are being asked: </li>
<li>Cover what the requirements mention, we will explore details in a later project</li>
<li>Keep in mind that you will have 30 minutes to perform the exercise, you will get points for what is asked in requirements</li>
<li>Similarly in a job interview, you should answer what the interviewer asked for, be careful about being too verbose - always ask the interviewer if going into details is necessary - speaking too much can play against you</li>
<li>In this project, again, avoid going in details if not asked</li>
</ul>

<hr class="gap">
<h2 class="gap">Tasks</h2>

 <h4 class="task">
    0. Simple web stack
</h4>
  <p>A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a <a href="/rltoken/lBFrw_pTU3_sMuYFptFFsw" title="LAMP stack" target="_blank">LAMP stack</a>.</p>

<p>On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via <code>www.foobar.com</code>. Start your explanation by having a user wanting to access your website.</p>

<p>Requirements:</p>

<ul>
<li> You must use:

<ul>
<li>1 server</li>
<li>1 web server (Nginx)</li>
<li>1 application server</li>
<li>1 application files (your code base)</li>
<li>1 database (MySQL)</li>
<li>1 domain name <code>foobar.com</code> configured with a <code>www</code> record that points to your server IP <code>8.8.8.8</code></li>
</ul></li>
<li>You must be able to explain some specifics about this infrastructure:

<ul>
<li>What is a server</li>
<li>What is the role of the domain name</li>
<li>What type of DNS record <code>www</code> is in <code>www.foobar.com</code></li>
<li>What is the role of the web server</li>
<li>What is the role of the application server</li>
<li>What is the role of the database</li>
<li>What is the server using to communicate with the computer of the user requesting the website</li>
</ul></li>
<li>You must be able to explain what the issues are with this infrastructure:

<ul>
<li>SPOF</li>
<li>Downtime when maintenance needed (like deploying new code web server needs to be restarted)</li>
<li>Cannot scale if too much incoming traffic</li>
</ul></li>
</ul>

  <h4 class="task">
    1. Distributed web infrastructure
</h4>
 <p>On a whiteboard, design a three server web infrastructure that hosts the website <code>www.foobar.com</code>.</p>

<p>Requirements:</p>

<ul>
<li> You must add:

<ul>
<li>2 servers</li>
<li>1 web server (Nginx)</li>
<li>1 application server</li>
<li>1 load-balancer (HAproxy)</li>
<li>1 set of application files (your code base)</li>
<li>1 database (MySQL)</li>
</ul></li>
<li>You must be able to explain some specifics about this infrastructure:

<ul>
<li>For every additional element, why you are adding it</li>
<li>What distribution algorithm your load balancer is configured with and how it works</li>
<li>Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both</li>
<li>How a database Primary-Replica (Master-Slave) cluster works</li>
<li>What is the difference between the Primary node and the Replica node in regard to the application</li>
</ul></li>
<li>You must be able to explain what the issues are with this infrastructure:

<ul>
<li>Where are SPOF</li>
<li>Security issues (no firewall, no HTTPS)</li>
<li>No monitoring</li>
</ul></li>
</ul>

 <h4 class="task">
    2. Secured and monitored web infrastructure
</h4>
 <p>On a whiteboard, design a three server web infrastructure that hosts the website <code>www.foobar.com</code>, it must be secured, serve encrypted traffic, and be monitored.</p>

<p>Requirements:</p>

<ul>
<li> You must add:

<ul>
<li>3 firewalls </li>
<li>1 SSL certificate to serve <code>www.foobar.com</code> over HTTPS</li>
<li>3 monitoring clients (data collector for Sumologic or other monitoring services)</li>
</ul></li>
<li>You must be able to explain some specifics about this infrastructure:

<ul>
<li>For every additional element, why you are adding it</li>
<li>What are firewalls for</li>
<li>Why is the traffic served over HTTPS</li>
<li>What monitoring is used for</li>
<li>How the monitoring tool is collecting data</li>
<li>Explain what to do if you want to monitor your web server QPS</li>
</ul></li>
<li>You must be able to explain what the issues are with this infrastructure:

<ul>
<li>Why terminating SSL at the load balancer level is an issue</li>
<li>Why having only one MySQL server capable of accepting writes is an issue</li>
<li>Why having servers with all the same components (database, web server and application server) might be a problem</li>
</ul></li>
</ul>