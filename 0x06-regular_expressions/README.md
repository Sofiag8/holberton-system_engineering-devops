<h1 class="gap">0x06. Regular expression</h1>

 <h2>Background Context</h2>
<p>For this project, I have to build my own regular expression using Oniguruma, a regular expression library that which is used by Ruby by default.</p>

<p>Ruby code used in this project:</p>

<pre><code>sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
</code></pre>


<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env ruby</code></li>
<li>All your regex must be built for the Oniguruma library</li>
</ul>


<hr class="gap">
<h2 class="gap">Tasks</h2>
<h4 class="task">
    0. Simply matching Holberton
  </h4>
<p>Requirements:</p>

<ul>
<li>The regular expression must match <code>Holberton</code></li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ./0-simply_match_holberton.rb Holberton | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb &quot;Holberton School&quot; | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb &quot;Holberton School Holberton&quot; | cat -e
HolbertonHolberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb &quot;Grace Hopper&quot; | cat -e
$
</code></pre>

  <h4 class="task">
    1. Repetition Token #0
  </h4>
<p>Requirements:</p>

<ul>
<li>Find the regular expression that will match the above cases</li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
</ul>

 <h4 class="task">
    2. Repetition Token #1
  </h4>
<p>Requirements:</p>

<ul>
<li>Find the regular expression that will match the above cases</li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
</ul>

<h4 class="task">
    3. Repetition Token #2
  </h4>
<p>Requirements:</p>

<ul>
<li>Find the regular expression that will match the above cases</li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
</ul>


<h4 class="task">
    4. Repetition Token #3
  </h4>
<p>Requirements:</p>

<ul>
<li>Find the regular expression that will match the above cases</li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
<li>Your regex should not contain square brackets</li>
</ul>



  <h4 class="task">
    5. Not quite HBTN yet
  </h4>
 <p>Requirements:</p>

<ul>
<li>The regular expression must be exactly matching a string that starts with <code>h</code> ends with <code>n</code> and can have any single character in between</li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ./5-beginning_and_end.rb &#39;hn&#39; | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb &#39;hbn&#39; | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb &#39;hbtn&#39; | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb &#39;h8n&#39; | cat -e
h8n$
sylvain@ubuntu$
$
</code></pre>



  <h4 class="task">
    6. Call me maybe
 </h4>
 <p>This task is brought to you by Holberton professional advisor <a href="/rltoken/V4rEpseJEPRMMnfaZPbkgw" title="Neha Jain" target="_blank">Neha Jain</a>, Senior Software Engineer at LinkedIn.</p>

<p>Requirement:</p>

<ul>
<li>The regular expression must match a 10 digit phone number</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb &quot; 4155049898&quot; | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb &quot;415 504 9898&quot; | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb &quot;415-504-9898&quot; | cat -e
$
sylvain@ubuntu$
</code></pre>

<h4 class="task">
    7. OMG WHY ARE YOU SHOUTING?
  </h4>
<p>Requirement:</p>

<ul>
<li>The regular expression must be only matching: capital letters</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb &quot;I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream&quot; | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb &quot;WHAT do you SAY?&quot; | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb &quot;cannot read you&quot; | cat -e
$
sylvain@ubuntu$
</code></pre>

  <h4 class="task">
    9. Pass LinkedIn technical interview level0
#advanced
  </h4>
<p>One way to get started in getting a Software Engineering job at LinkedIn is to solve their regex puzzle.</p>

<p>Requirements:</p>

<ul>
<li>Solve LinkedIn regex puzzle: <a href="https://engineering.linkedin.com/puzzle" title="https://engineering.linkedin.com/puzzle" target="_blank">https://engineering.linkedin.com/puzzle</a></li>
<li>Provide as an answer file a screenshot of the &ldquo;Congratulations&rdquo; screen with the date and time of completion</li>
</ul>