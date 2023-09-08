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

<p>Notice that the Host Computer has access to both the virtual network (this is selected by you, in the diagram it is VMnet2, but on your system it may be VMnet1 if you don't create a special adapter with the VMware DHCP service disabled, as was performed in VMnet2. The LAN interface can be identified as the "Host-Only" network.). The OPNsense Web base User Interface can only be accessed from the private/internal/LAN network, in the example above, it is located at IP address 192.168.111.100. Both the Host computer and the DSL server can connect and use the OPNsense web-based interface located at this address. The Web UI is NOT accessible from the public (WAN) network.</p>

<p>The assignment is broken up into two phase, Firewall setup and nmap scanning.</p>

<h2>Phase 1</h2>

<p>The following is a list of steps to follow to complete the first phase of the assignment:</p>
<p>Read the instructions from the <a href="https://usflearn.instructure.com/courses/1830104/files/155014830?wrap=1">lab document,</a> chapter "Introduction o Firewalls"</p>
<ul>
    <li>Start at "Overview"</li>
    <li>End at the beginning of "Firewall Rules Basics</li>
</ul>
<p>Setup the Firewall Image using VMware Workstation Pro or Fusion</p>
<ul>
    <li><a href="https://usflearn.instructure.com/courses/1830104/files/155015082?wrap=1">Open OPNsense Firewall</a></li>
    <li>Configure the network adapters required</li>
    <li>Configure the private LAN for Network Only</li>
        <ul>
            <li>NOTE: There is no security configuration required yet</li>
            <li>Firewall contains much of the network functionality</li>
                <ul>
                    <li>DHCP Client/Server</li>
                    <li>NAT</li>
                </ul>
            <li>Configure the WAN - em0 (to ISP using Bridge mode or VMware NAT)</li>
            <li>Configure the LAN - le0</li>
                <ul>
                    <li>This is a Host-Only VMware virtual network</li>
                    <li>This is em1 for OPNsense version 21</li>
                    <li>If you use VMnet1, disable the VMware DHCP service</li>
                    <li>You can create a net interface, VMnet2 with the DHCP service disabled</li>
                        <ul>
                            <li>This allows you to run the DVWA CTF exercises on VMnet1 and Firewall exercises on VMnet2</li>
                        </ul>
                </ul>
            <li>Configure DHCP (for virtual network) as describe in the presentation</li>
        </ul>
    <li>OPNsense Network Setup</li>
        <ul>
            <li>This will be the hardest part of the exercise</li>
            <li>Configure the WAN - Generally performed automatically using ISP or VMware DHCP service, example:192.168.136.100/24</li>
            <li>Configure the LAN – Performed statically in OPNsense firewall console setup, example: 192.168.111.100/24</li>
            <li>Follow the Lab Documentation to determine how to complete the following operations</li>
                <ul>
                    <li>Boot OPNsense</li>
                        <ul>
                            <li>Go to the Vmware console for OPNsense</li>
                                <ul>
                                    <li>Select 1 and configure the Interfaces</li>
                                    <li>Select 2 and configure the IP addresses for each interface</li>
                                        <ul>
                                            <li>The internal interface (LAN/Private) must be a static address</li>
                                            <li>The address must be in the same subnet as the Virtual Adapter you are using, for example VMnet1 or VMnet2</li>
                                            <li>Use ipconfig to find the Host address for this and use that subnet to configure the static LAN address of the firewall</li>
                                        </ul>
                                    <li>Ping the router</li>
                                </ul>
                        </ul>
                </ul>
        </ul>
</ul>

<h2>Phase 2</h2>
<p>In the second phase of the assignment, we will perform network scanning on three individual systems, the “host” computer, the OPNsense Firewall and the DSL Linux server. This will introduce us to the type of information we may obtain from these scans and teach us a valuable lesson on how information may “leak” from simple nmap scans. To implement the second portion of the assignment:</p>
<ul>
    <li>Make sure the Firewall LAN/Private interface is configured for DHCP</li>
    <li>Startup VMware Workstation Pro or Fusion – DSL (Created in Module 1)</li>
        <ul>
            <li>This requires OPNsense-Firewall for DHCP address</li>
            <li>Make sure OPNsense is running first</li>
        </ul>
    <li><a href="https://nmap.org/">Download http://nmap.org for Windows</a></li>
    <li>Install nmap on your Windows Host system</li>
        <ul>
            <li>Windows Host (where you are running NMAP from, if you scan 127.0.0.1 it will result in a scan of this local host)</li>
            <li>The DSL Server (from Module 1)</li>
            <li>The OPNsense Firewall (WAN/LAN) Interfaces</li>
        </ul>
</ul>

<p>Once you have completed the operations in the assignment, take the quiz, which will test our knowledge on the operations that you have performed.</p>
