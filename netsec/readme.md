# CS496/596: Network Security

**Location**: FAB 10 (MW 14:00-15:50)

**Instructor**: D. Kevin McGrath

* PDX username: dmcgrath
* Office hours:
    * Location: FAB 120-15 and [Zoom](https://pdx.zoom.us/j/84716901228) (PW: PSUSecure)
    * Times:
        * Monday: 10:00 - 11:30 (FAB 120-15 only)
        * Tuesday: 11:00 - 12:00 (Zoom only)
        * Tuesday: Code Party! 18:30 - 22:00 (FAB 86-01/88-03)
        * Wednesday: 10:00 - 11:30 (FAB 120-15 only) -- except first and third Wednesdays of the month due to faculty meetings.
        * Thursday: 09:30 - 11:30 (Zoom only)

**[Syllabus](syllabus.md)**

**Recorded Lectures**: These will be made available via [MediaSpace](https://media.pdx.edu/channel/channelid/328503742). Login required.

<!-- **Zulip Org**: [Zulip](https://netsec.zulip.cs.pdx.edu/) -->

---

## Homework

Each homework will build in some fashion on the previous homework. This may be conceptually, but may be directly. These aren't your typical "write answers to questions" type assignments, but rather are intended to be more hands-on. Nearly all the work I'm asking you to do is taken from tasks I had to perform professionally as a security vulnerability engineer. The first assignment will be to get the VM environment set up and configured. Subsequent assignments will build on this.

### Submission

All work will be submitted via MarkDown documents within an internal [gitlab](https://gitlab.cecs.pdx.edu) repo. You will be using this repo for the rest of the term. This repo exists on the CECS intranet. You will need to add myself and the TA to this repo as Developers. Grades and feedback will be done via a merge request from the TA.

The grader for this class is Teo Coffman. His PDX username is `theodos`.

### Assignments

* [Homework 1](hw1.md)
<!-- * [Homework 2](hw2.md)
* [Homework 3](hw3.md)
* [Homework 4](hw4.md)
* [Final Paper: CS496](final-496.md)
* [Final Project: CS596](final.md) -- this can be done by 496 students in place of the paper. -->

---
## To install Kali Linux through WSL:

```
wsl --install -d kali-linux
```

### A nice GUI
Should you want a GUI for any reason, you can get a nice one with the following commands run from within the Kali session:

```sh
$ sudo apt install 
$ sudo apt upgrade
$ sudo apt install -y kali-win-kex
```

Then, to start the GUI, run (f8 will exit fullscreen mode):

```sh
$ kex --win -s
```

## Pages

* [Software configuration](../software.md) -- not required, but possibly useful information on environment setup
* [tmux config](../.tmux.conf.md) -- configuration file for tmux from the Software Configuration page
* [Powershell profile](../powershell_profile.md) -- powershell profile from the Software Configuration page
* [Technical Writing](../technical_writing.md) -- if unfamiliar with markdown or LaTeX, this page will help
* [VM Setup on Windows](hyper-v.md)
* [VM Setup on macOS](vms_on_macos.md)
* [Kali configuration](linux_setup.md)
* [SSH Tunnel for Windows RDP](../SSH_Tunnel_XRDP.md) -- SSH tunneling trick we will be using in various places through the term
* [Introduction to Networking](../networking.md) -- a brief introduction to networking concepts
* [Introduction to network reconnaissance](recon.md) -- a brief introduction to network reconnaissance and using nmap
* [Cracking WiFi](crack_wifi.md) -- a brief introduction to cracking WiFi

## Useful links for learning

* [tmux cheatsheet](https://tmuxcheatsheet.com/)
* [Linux Handbook on tmux](https://linuxhandbook.com/tmux/)
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
