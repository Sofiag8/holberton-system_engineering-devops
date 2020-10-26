<h1 class="gap">Project 0x05. Processes and signals</h1>

<h2>Learning Objectives</h2>

<h3>General</h3>

<ul>
<li>What is a PID</li>
<li>What is a process</li>
<li>How to find a process&rsquo; PID</li>
<li>How to kill a process</li>
<li>What is a signal</li>
<li>What are the 2 signals that cannot be ignored</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.3-1~ubuntu14.04.1</code> via <code>apt-get</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

  <h2 class="gap">Tasks</h2>
 <h4 class="task">
    0. What is my PID
</h4>
 <p>Write a Bash script that displays its own PID.</p>

<h4 class="task">
    1. List your processes
</h4>
<p>Write a Bash script that displays a list of currently running processes.</p>

<p>Requirements:</p>

<ul>
<li>Must show all processes, for all users, including those which might not have a TTY</li>
<li>Display in a user-oriented format</li>
<li>Show process hierarchy</li>
</ul>

 <h4 class="task">
    2. Show your Bash PID
</h4>
 <p>Using your previous exercise command, write a Bash script that displays lines containing the <code>bash</code> word, thus allowing you to easily get the PID of your Bash process.</p>

<p>Requirements:</p>

<ul>
<li>You cannot use <code>pgrep</code></li>
<li>The third line of your script must be <code># shellcheck disable=SC2009</code> (for more info about ignoring <code>shellcheck</code> error <a href="/rltoken/BYXAGPH5zbPpsqIR84ndFQ" title="here" target="_blank">here</a>)</li>
</ul>

 <h4 class="task">
    3. Show your Bash PID made easy
</h4>
 <p>Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word <code>bash</code>.</p>

<p>Requirements:</p>

<ul>
<li>You cannot use <code>ps</code></li>
</ul>

<pre><code>sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4555 bash
sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4557 bash
sylvain@ubuntu$ 
</code></pre>

<p>Here we can see that: </p>

<ul>
<li>For the first iteration: <code>bash</code> PID is <code>4404</code> and that the <code>3-show_your_bash_pid_made_easy</code> script PID is <code>4555</code></li>
<li>For the second iteration: <code>bash</code> PID is <code>4404</code> and that the <code>3-show_your_bash_pid_made_easy</code> script PID is <code>4557</code></li>
</ul>

 <h4 class="task">
    4. To infinity and beyond
</h4>
 <p>Write a Bash script that displays <code>To infinity and beyond</code> indefinitely. </p>

<p>Requirements:</p>

<ul>
<li>In between each iteration of the loop, add a <code>sleep 2</code></li>
</ul>

 <h4 class="task">
    5. Don&#39;t stop my now!
</h4>
 <p>We stopped our <code>4-to_infinity_and_beyond</code> process using <code>ctrl+c</code> in the previous task, there is actually another way to do this.</p>

<p>Write a Bash script that stops <code>4-to_infinity_and_beyond</code> process.</p>

<p>Requirements:</p>

<ul>
<li>You must use <code>kill</code></li>
</ul>

<p>Terminal #0</p>

<h4 class="task">
    6. Stop me if you can
</h4>
 <p>Write a Bash script that stops <code>4-to_infinity_and_beyond</code> process.</p>

<p>Requirements:</p>

<ul>
<li>You cannot use <code>kill</code> or <code>killall</code></li>
</ul>

 <h4 class="task">
    7. Highlander
</h4>
<p>Write a Bash script that displays: </p>

<ul>
<li><code>To infinity and beyond</code> indefinitely</li>
<li>With a <code>sleep 2</code> in between each iteration</li>
<li><code>I am invincible!!!</code> when receiving a <code>SIGTERM</code> signal</li>
</ul>

<p>Make a copy of your <code>6-stop_me_if_you_can</code> script, name it <code>67-stop_me_if_you_can</code>,  that kills the <code>7-highlander</code> process instead of the <code>4-to_infinity_and_beyond</code> one.</p>


 <h4 class="task">
    8. Beheaded process
</h4>
 <p>Write a Bash script that kills the process <code>7-highlander</code>.</p>



<p> Plus advanced task </p>