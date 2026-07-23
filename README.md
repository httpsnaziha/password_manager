<h2 align="center"><u>Password_manager</u></h2>

<h4 align="center"> Generate beautiful Repository Readme </h4>

<p align="center">
<br>
    <img src="https://img.shields.io/badge/Author-NAZiha-magenta?style=flat-square">
    <img src="https://img.shields.io/badge/Written%20In-Python-blue?style=flat-square">
</p>

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Password Manager - README</title>
<style>
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    max-width: 820px;
    margin: 40px auto;
    padding: 0 20px;
    line-height: 1.6;
    color: #24292f;
  }
  h1 { border-bottom: 1px solid #d0d7de; padding-bottom: 0.3em; }
  h2 { border-bottom: 1px solid #d0d7de; padding-bottom: 0.3em; margin-top: 2em; }
  code {
    background: #f6f8fa;
    padding: 0.2em 0.4em;
    border-radius: 6px;
    font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
    font-size: 85%;
  }
  pre {
    background: #f6f8fa;
    padding: 16px;
    border-radius: 6px;
    overflow-x: auto;
  }
  pre code { background: none; padding: 0; }
  blockquote {
    border-left: 4px solid #d0d7de;
    margin: 0;
    padding: 0 1em;
    color: #57606a;
  }
  img { max-width: 100%; border-radius: 6px; }
  table { border-collapse: collapse; }
  .warning {
    background: #fff8c5;
    border: 1px solid #d4a72c;
    border-radius: 6px;
    padding: 12px 16px;
    margin: 1em 0;
  }
</style>
</head>
<body>

<h1>🔐 Password Manager</h1>

<p>A simple desktop password manager built with <strong>Python</strong> and <strong>Tkinter</strong>, featuring a random password generator and encrypted storage using the <code>cryptography</code> library's Fernet symmetric encryption.</p>

<img width="449" height="308" alt="password manager" src="https://github.com/user-attachments/assets/50585daa-7160-48cd-96fe-3597c063e586" />

<h2>Features</h2>
<ul>
  <li>🖥️ <strong>Simple GUI</strong> — clean Tkinter interface for adding new logins</li>
  <li>🎲 <strong>Password generator</strong> — creates strong random passwords using a mix of uppercase/lowercase letters, digits, and symbols</li>
  <li>🔒 <strong>Encrypted storage</strong> — passwords are encrypted with <code>Fernet</code> before being saved to disk</li>
  <li>📄 <strong>Local file storage</strong> — saved entries are appended to a plain text file (<code>passwordManager.txt</code>), with only the password field encrypted</li>
  <li>✅ <strong>Input validation</strong> — warns if any field (website, username, password) is left empty</li>
  <li>🔑 <strong>Auto-generated encryption key</strong> — a <code>secret.key</code> file is created automatically on first run and reused afterward</li>
</ul>

<h2>How It Works</h2>
<ol>
  <li>Enter a <strong>website</strong>, <strong>username</strong>, and <strong>password</strong> in the input fields.</li>
  <li>Optionally click <strong>Generate Password</strong> to auto-fill a strong random password.</li>
  <li>Click <strong>Add</strong> to save the entry — you'll get a confirmation prompt showing the details before saving.</li>
  <li>The entry is appended to <code>passwordManager.txt</code> in the format:
    <pre><code>-&gt; website: example.com |-&gt; Email: user@example.com |-&gt; Password(encrypted): &lt;encrypted_string&gt;</code></pre>
  </li>
  <li>The password is encrypted using a key stored in <code>secret.key</code> (auto-generated the first time you run the app).</li>
</ol>

<h2>Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li><a href="https://pypi.org/project/Pillow/">Pillow</a> (<code>PIL</code>)</li>
  <li><a href="https://pypi.org/project/cryptography/">cryptography</a></li>
</ul>

<p>Install dependencies with:</p>
<pre><code>pip install pillow cryptography</code></pre>

<blockquote>Note: <code>tkinter</code> usually ships with Python by default. On Linux, you may need to install it separately (e.g. <code>sudo apt install python3-tk</code>).</blockquote>

<h2>Usage</h2>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/httpsnaziha/password_manager.git
cd password_manager</code></pre>
  </li>
  <li>Make sure <code>logo.png</code> is in the same directory as <code>main.py</code>.</li>
  <li>Run the app:
    <pre><code>python main.py</code></pre>
  </li>
</ol>

<h2>Project Structure</h2>
<pre><code>password_manager/
├── main.py               # Main application (GUI + logic)
├── logo.png              # App logo shown in the UI
├── passwordManager.txt   # Stores saved entries (created on first save)
└── secret.key            # Encryption key (auto-generated on first run)</code></pre>

<h2>⚠️ Security Notes</h2>
<div class="warning">
  <ul>
    <li><code>secret.key</code> is the only thing standing between an attacker and your saved passwords — <strong>never commit it or <code>passwordManager.txt</code> to version control or share them publicly.</strong></li>
    <li>Website names and usernames are stored <strong>in plain text</strong>; only the password field is encrypted.</li>
    <li>This project is intended as a learning/demo tool for GUI development and basic encryption, not as a production-grade password manager.</li>
  </ul>
</div>

</body>
</html>
