<h1 class="gap">Project 0x17. Web stack debugging #3</h1>

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
<li>Files will be checked with Puppet v3.4</li>
</ul> 


<p>Using <code>strace</code>, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).</p>

<p>Hint:</p>

<ul>
<li><code>strace</code> can attach to a current running process</li>
<li>You can use <a href="https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/" title="tmux" target="_blank">tmux</a> to run <a href="https://strace.io/" title="strace" target="_blank">strace</a> in one window and <code>curl</code> in another one</li>
</ul>

<p>Requirements:</p>

<ul>
<li>Your <code>0-strace_is_your_friend.pp</code> file must contain Puppet code</li>
<li>You can use whatever Puppet resource type you want for you fix</li>
</ul>