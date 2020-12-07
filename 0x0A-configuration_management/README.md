<h1 class="gap">Project 0x0A Configuration management</h1>
<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file at the root of the folder of the project is mandatory</li>
<li>Your Puppet manifests must pass <code>puppet-lint</code> version 2.1.1 without any errors</li>
<li>Your Puppet manifests must run without error</li>
<li>Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about</li>
<li>Your Puppet manifests files must end with the extension <code>.pp</code> </li>
</ul>

<h2>Note on Versioning</h2>

<p>Your Ubuntu 14.04 VM should have Puppet 3.4 preinstalled. </p>

<h3>Install <code>puppet-lint</code></h3>

<pre><code>$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
</code></pre>


<hr class="gap">
<h2 class="gap">Tasks</h2>

  <h4 class="task">
    0. Create a file
</h4>
 <p>Using Puppet, create a file in <code>/tmp</code>.</p>

<p>Requirements:</p>

<ul>
<li>File path is <code>/tmp/holberton</code></li>
<li>File permission is <code>0744</code></li>
<li>File owner is <code>www-data</code></li>
<li>File group is <code>www-data</code></li>
<li>File contains <code>I love Puppet</code></li>
</ul>

<h4 class="task">
    1. Install a package
</h4>
<p>Using Puppet, install <code>puppet-lint</code>.</p>

<p>Requirements:</p>

<ul>
<li>Install <code>puppet-lint</code></li>
<li>Version must be <code>2.1.1</code></li>
</ul>

  <h4 class="task">
    2. Execute a command
</h4>
 <p>Using Puppet, create a manifest that kills a process named <code>killmenow</code>.</p>

<p>Requirements:</p>

<ul>
<li>Must use the <code>exec</code> Puppet resource</li>
<li>Must use <code>pkill</code> </li>
</ul>


