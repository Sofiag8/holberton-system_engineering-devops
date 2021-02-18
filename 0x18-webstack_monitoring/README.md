<h1 class="gap">Project 0x18. Webstack monitoring</h1>

<h2>Background Context</h2>

<p>&ldquo;You cannot fix or improve what you cannot measure&rdquo; is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.</p>

<p>Web stack monitoring can be broken down into 2 categories:</p>

<ul>
<li>Application monitoring: getting data about your running software and making sure it is behaving as expected</li>
<li>Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)</li>
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


<h2 class="gap">Tasks</h2>

<h4 class="task">
    0. Sign up for Datadog and install datadog-agent
</h4>
<p> Fot this task I must create an account on datadog, install datadog agent, generate a datadog API key and datadog application key and set up web-server1 to be visible on Datadog with the host name XX-web-01 </p>


<h4 class="task">
    1. Monitor some metrics
</h4>
 <p>Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some <code>monitors</code> within the <code>Datadog</code> dashboard to monitor and alert you of a few.</p>
<ul>
<li>Set up a monitor that checks the number of read requests issued to the device per second.</li>
<li>Set up a monitor that checks the number of write requests issued to the device per second.</li>
</ul>

<h4 class="task">
    2. Create a dashboard
</h4>
  <p>Now create a dashboard with different metrics displayed in order to get a few different visualizations.</p>

<ul>
<li>Create a new <code>dashboard</code></li>
<li>Add at least 4 <code>widgets</code> to your dashboard. They can be of any type and monitor whatever you&rsquo;d like</li>
<li>Create the answer file <code>2-setup_datadog</code> which has the <code>dashboard_id</code> on the first line. <strong>Note</strong>: in order to get the id of your dashboard, you may need to use <a href="https://docs.datadoghq.com/api/latest/dashboards/#get-all-dashboards" title="Datadog&#39;s API" target="_blank">Datadog&rsquo;s API</a></li>
</ul>