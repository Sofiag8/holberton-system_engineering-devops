<h1 class="gap">Project 0x14. MySQL</h1>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.7-5~ubuntu16.04.1</code> via <code>apt-get</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

<hr class="gap">
<h2 class="gap">Tasks</h2>

 <h4 class="task">
    0. Install MySQL
</h4>
 <p>First things first, let&rsquo;s get MySQL installed on <strong>both</strong> your web-01 and web-02 servers.</p>

<ul>
<li>MySQL distribution must be 5.7.x</li>
<li>Make sure that <a href="https://intranet.hbtn.io/tasks/1372" title="task #3" target="_blank">task #3</a> of your <a href="/rltoken/haLXhL5svnmrgskFpFHmyA" title="SSH project" target="_blank">SSH project</a> is completed for <code>web-01</code> and <code>web-02</code>.  The checker will connect to your servers to check MySQL status</li>
<li>Please make sure you have your <code>README.md</code> pushed to Github.</li>
</ul>

<h4 class="task">
    1. Let us in!
 </h4>
<p>In order for us to verify that your servers are properly configured, we need you to create a user and password for <strong>both</strong> MySQL databases which will allow the checker access to them.</p>

<ul>
<li>Create a MySQL user named <code>holberton_user</code>  on both <code>web-01</code> and <code>web-02</code> with the host name set to <code>localhost</code> and the password <code>projectcorrection280hbtn</code>. This will allow us to access the replication status on both servers.</li>
<li>Make sure that <code>holberton_user</code> has permission to check the primary/replica status of your databases.</li>
<li>In addition to that, make sure that <a href="https://intranet.hbtn.io/tasks/1372" title="task #3" target="_blank">task #3</a> of your <a href="https://intranet.hbtn.io/projects/244" title="SSH project" target="_blank">SSH project</a> is completed for <code>web-01</code> and <code>web-02</code>.  <strong>You will likely need to add the public key to web-02 as you only added it to web-01 for this project.</strong> The checker will connect to your servers to check MySQL status</li>
</ul>

 <h4 class="task">
    2. If only you could see what I&#39;ve seen with your eyes
</h4>
<p>In order for you to set up replication, you&rsquo;ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.</p>

<ul>
<li>Create a database named <code>tyrell_corp</code>.</li>
<li>Within the <code>tyrell_corp</code> database create a table named <code>nexus6</code> and add at least one entry to it.</li>
<li>Make sure that <code>holberton_user</code> has <code>SELECT</code> permissions on your table so that we can check that the table exists and is not empty.</li>
</ul>


  <h4 class="task">
    3. Quite an experience to live in fear, isn&#39;t it?
</h4>
 <p>Before you get started with your primary-replica synchronization, you need one more thing in place. On your <strong>primary</strong> MySQL server (web-01), create a new user for the replica server.</p>

<ul>
<li>The name of the new user should be <code>replica_user</code>, with the host name set to <code>%</code>, and can have whatever password you&rsquo;d like.</li>
<li><code>replica_user</code> must have the appropriate permissions to replicate your primary MySQL server.</li>
<li><code>holberton_user</code> will need SELECT privileges on the <code>mysql.user</code> table in order to check that <code>replica_user</code> was created with the correct permissions.</li>
</ul>

 <h4 class="task">
    4. Setup a Primary-Replica infrastructure using MySQL
</h4>
<p>Having a replica member on for your MySQL database has 2 advantages:</p>

<ul>
<li>Redundancy: If you lose one of the database servers, you will still have another working one and a copy of your data</li>
<li>Load distribution: You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed</li>
</ul>

<h3>Requirements:</h3>

<ul>
<li>MySQL primary must be hosted on <code>web-01</code> - do not use the <code>bind-address</code>,  just comment out this parameter</li>
<li>MySQL replica must be hosted on <code>web-02</code></li>
<li>Setup replication for the MySQL database named <code>tyrell_corp</code></li>
<li>Provide your MySQL primary configuration as answer file(<code>my.cnf</code> or <code>mysqld.cnf</code>) with the name <code>4-mysql_configuration_primary</code></li>
<li>Provide your MySQL replica configuration as an answer file with the name <code>4-mysql_configuration_replica</code></li>
</ul>

<h3>Tips:</h3>

<ul>
<li>Once MySQL replication is setup, add a new record in your table via MySQL on <code>web-01</code> and check if the record has been replicated in MySQL <code>web-02</code>. If you see it, it means your replication is working!</li>
<li><strong>Make sure that UFW is allowing connections on port 3306 (default MySQL port) otherwise replication will not work</strong>.</li>
</ul>

  <h4 class="task">
    5. MySQL backup
</h4>
<p>What if the data center where both your primary and replica database servers are hosted are down because of a power outage or even worse: flooding, fire? Then all your data would inaccessible or lost. That&rsquo;s why you want to backup and store them in a different system in another physical location. This can be achieved by dumping your MySQL data, compressing them and storing them in a different data center.</p>

<p>Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.</p>

<p>Requirements:</p>

<ul>
<li>The MySQL dump must contain all your MySQL databases</li>
<li> The MySQL dump must be named <code>backup.sql</code></li>
<li>The MySQL dump file has to be compressed to a <code>tar.gz</code> archive</li>
<li>This archive must have the following name format: <code>day-month-year.tar.gz</code></li>
<li>The user to connect to the MySQL database must be <code>root</code></li>
<li>The Bash script accepts one argument that is the password used to connect to the MySQL database</li>
</ul>
