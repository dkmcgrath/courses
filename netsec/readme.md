# CS496/596: Network Security

**Location**: EB 103 (TR 16:40-18:30)

**Instructor**: D. Kevin McGrath

* PDX username: dmcgrath
* Office hours:
    * Location: FAB 120-15 and [Zoom](https://pdx.zoom.us/j/84716901228) (PW: PSUSecure)
    * Times:
        * Tuesday: 14:30 - 16:15
        * Wednesday: Code Party (19:00-22:00, FAB 86-01/88-03)
        * Thursday: 14:30 - 16:15

**[Syllabus](syllabus.md)**

**Recorded Lectures**: These will be made available via [MediaSpace](https://media.pdx.edu/channel/channelid/328503742). Login required.

## Homework

Each homework will build in some fashion on the previous homework. This may be conceptually, but may be directly. These aren't your typical "write answers to questions" type assignments, but rather are intended to be more hands-on. Nearly all the work I'm asking you to do is taken from tasks I had to perform professionally as a security vulnerability engineer. The first assignment will be to get the VM environment set up and configured. Subsequent assignments will build on this.

### Submission

All work will be submitted via MarkDown documents within an internal [gitlab](https://gitlab.cecs.pdx.edu) repo. You will be using this repo for the rest of the term. This repo exists on the CECS intranet. You will need to add me to this repo as Developers. Grades and feedback will be done via a merge request from me.


### Assignments

* [Homework 1](hw1.md)
* [Homework 2](hw2.md)
* [Homework 3](hw3.md)
* [Homework 4](hw4.md)
* [Homework 5](hw5.md)
* [Final Paper: CS496](final-496.md)
* [Final Project: CS596](final.md) -- this can be done by 496 students in place of the paper.

## Pages

* [Software configuration](../software.md) -- not required, but possibly useful information on environment setup
* [`tmux` config](../.tmux.conf.md) -- configuration file for `tmux` from the Software Configuration page
* [Powershell profile](../powershell_profile.md) -- powershell profile from the Software Configuration page
* [Technical Writing](../technical_writing.md) -- if unfamiliar with markdown or LaTeX, this page will help
* [VM Setup on Windows](hyper-v.md)
* [VM Setup on macOS](vms_on_macos.md)
* [Kali configuration](linux_setup.md)
* [SSH setup](SSH_setup.md) -- setting up SSH keys for use with the VM
* [SSH Tunnel for Windows RDP](../SSH_Tunnel_XRDP.md) -- SSH tunneling trick we will be using in various places through the term
* [Introduction to Networking](../networking.md) -- a brief introduction to networking concepts
* [Introduction to network reconnaissance](recon.md) -- a brief introduction to network reconnaissance and using nmap
* [Cracking WiFi](crack_wifi.md) -- a brief introduction to cracking WiFi
* [Capturing packets](../tcpdump.md) -- a brief introduction to capturing packets
* [Using `wireshark`](../wireshark.md) -- a brief introduction to using `wireshark`
* [Introduction to `scapy`](scapy.md) -- a brief introduction to `scapy`
* [80 to 0 in Under 5 Seconds: Falsifying a Medical Patient’s Vitals](rwhat.md) -- an article detailing a real-world attack on a medical device, including how he reversed the protocol (RWHAT).
* [Defensive measures](../firewalls.md) -- a brief introduction to firewalls and IPS/IDS
* [TunnelVision exploit against VPNs](https://github.com/leviathansecurity/TunnelVision) -- an exploit a malicious network admin could use to render most VPNs useless.

## Useful links for learning

* [The Art of Packet Crafting with Scapy](https://0xbharath.github.io/art-of-packet-crafting-with-scapy/index.html)
* [`scapy` cheatsheet](ScapyCheatSheet_v0.2.pdf)
* [`nmap` cheatsheet](https://www.stationx.net/nmap-cheat-sheet/)
* [`tmux` cheatsheet](https://tmuxcheatsheet.com/)
* [Linux Handbook on `tmux`](https://linuxhandbook.com/tmux/)
* [Markdown](https://guides.github.com/features/mastering-markdown/)
* [The C Book](https://publications.gbdirect.co.uk/c_book/)
* [The GNU `make` manual](https://www.gnu.org/software/make/manual/make.pdf)
* [Managing projects with `make`](https://github.com/Vauteck/docs_utils/blob/master/autotools/Oreilly%20-%20Managing%20Projects%20With%20Gnu%20Make%203Rd%20Edition.pdf)
* [The `chmod` calculator](https://chmod-calculator.com/)
* [The Python tutor](https://pythontutor.com/)
* [_The Linux Command Line_](http://linuxcommand.org/tlcl.php) (Direct [PDF link](https://sourceforge.net/projects/linuxcommand/files/TLCL/19.01/TLCL-19.01.pdf/download))
* [_Adventures with the Linux Command Line_](https://sourceforge.net/projects/linuxcommand/files/AWTLCL/21.10/AWTLCL-21.10.pdf/download)
* [_The Linux Development Platform_](https://archive.org/details/ost-computer-science-0130091154/mode/1up)
* [gdb tutorial](http://www.cs.cmu.edu/~gilpin/tutorial/)
* [gef manual](https://hugsy.github.io/gef/)
