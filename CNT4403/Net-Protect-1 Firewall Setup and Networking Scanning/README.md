<p>CNT 4403 <i>Network Security and Firewalls</i><p>
<p>University of South Florida</p>

<h1>Net-Protect-1: Firewall Setup and Network Scanning</h1>

<p>The objective of this assignment is to setup a firewall in a virtual network environment to facilitate network operations for clients and servers in a protected private Local Area Network (LAN). For the firewall solution, we will use OPNsense. OPNsense is an open source, easy-to-use and easy-to-build FreeBSD based firewall and routing platform. OPNsense includes most of the features available in expensive commercial firewalls, and more in many cases. It brings the rich feature set of commercial offerings with the benefits of open and verifiable sources. You can learn more about OPNsense, the availability of updates and its history <a href="https://opnsense.org/about/about-opnsense/">here</a>. The OVFs you will use in this lab is OPNsense version 21 (<a href="https://usflearn.instructure.com/courses/1830104/files/155015082?wrap=1">USF-OPNsenseV21</a>). For Local Area Network (LAN) client/server, we will use the <a href="https://usflearn.instructure.com/courses/1830104/files/155015062?wrap=1">DSL OVF</a> solution provided here and also provided in a previous assignment. Follow the <a href="https://usflearn.instructure.com/courses/1830104/files/155014830?wrap=1">Lab Document</a> to help you undersand the details of the assignment, describe the functions of the OPNsense firewall and how to set it up and configure it are located in the chapters "Introduction to Firewalls" from section "Overview" to, but not including the section "Firewall Rules Basics".</p>
<p>The primary goals of this assignment are to:</p>
<ol>
    <li>Learn the different adapters used in a firewall</li>
    <li>Learn how to install and configure a firewall</li>
    <li>Learn how to monitor a firewall</li>
    <li>Learn how to provide DHCP access to clients and servers on a protect LAN environment</li>
    <li>Learn how o configure network device interfaces for a dual-homed system</li>
    <li>Learn network scanning techniques, such as nmap</li>
    <li>Learn how to detect when systems under our protection are being scanned</li>
</ol>

<p>NOTE: It is not a strict goal of this assignment to have connectivity from the DSL server to the internet, through the firewall, that will be required in an upcoming lab and the task defined below will not require it. That being said, the more you complete in this assignment, the less you have to worry about in the up-and-coming assignment where it will be required.</p>

<p>If you have not reviewed the assignment walk-through video, do so now.</p>

<p>It's important to understand how the firewall works. The following diagram shows the relationship between the firewall and the Internet, and internal LAN.</p>

<p align="center">
<img src="https://github.com/ThurmondGuy/Homework/blob/main/CNT4403/Net-Protect-1%20Firewall%20Setup%20and%20Networking%20Scanning/Diagram.png">
</p>
