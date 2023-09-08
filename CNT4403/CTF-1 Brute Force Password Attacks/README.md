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

![image8](https://github.com/ThurmondGuy/Homework/blob/main/CNT4403/CTF-1%20Brute%20Force%20Password%20Attacks/images/image8.png)

<p>To log into the system, use the username of “<b>ctf</b>” and password of 
“<b>ctf</b>”. This will present you with the login prompt of “ctf@usf-ctf-server:” (note the image above does not reflect the server’s name, but
the default name). It is from here that you can issue the “ifconfig” 
command. Note that the ctf account is a non-privileged account, so you 
will need to use “sudo” to invoke any system commands.</p>

<p>What we want is "ens33 inet addr". This is our "target server". So our target server here is <b>192.168.131.128</b>.</p>

<h2>Wireshark</h2>
<p>Use Wireshark and watch the traffic that is generated on the 
network, you can then filter out unwanted traffic to only give you the 
information you will need to exploit the system. To perform this 
exercise, start your Wireshark tracing for all traffic on the VMnet1 or 
VMnet8 network, or whatever network interface your IP address for 
your DVWA server IP address network is assigned to.</p>

![image4](https://github.com/ThurmondGuy/Homework/blob/main/CNT4403/CTF-1%20Brute%20Force%20Password%20Attacks/images/image4.png)

<p>We are going to need information for our Hydra attack later on:</p>
<ul>
    <li>target server</li>
    <li>cookie</li>
    <li>failure message</li>
</ul>

<p>Analyze the "GET" packet to find the <b>cookie</b>.</p>

![image9](https://github.com/ThurmondGuy/Homework/blob/main/CNT4403/CTF-1%20Brute%20Force%20Password%20Attacks/images/image9.png)

```
Cookie: security=low;
PHPSESSID=n232a3gba8kkd47tai36be0o81
```
