# CS 491/591: Introduction to Security

**Location**: FMA 204 (TR 12:00-13:50)

**Instructor**: D. Kevin McGrath

* PDX username: dmcgrath
* Office hours:
    * [Zoom link](https://pdx.zoom.us/j/84716901228)
    * Location: FAB 120-15
    * Times:
      * Tuesday: 14:30 - 16:15
      * Wednesday: Code Party (19:00-22:00, FAB 86-01/88-03)
      * Thursday: 14:30 - 16:15

**TA**: Juliette Simonds

* PDX username: jsimonds
* Office hours (in-person only):
  * Monday: 14:00 - 16:00 (Fishbowl)
  * Tuesday: 14:00 - 16:00 (Fishbowl)

## FINAL PROJECT:

[Final Project](final.md) -- Please submit topics by Friday of Week 9.

## Course Description

This class provides an overview of computer security intended for a broad audience. Topics covered include basic security principles, access control, cryptography, authentication, network security, host security, application security, and privacy and anonymity with a focus on how they are embodied in actual systems.

### Course objectives

1. Explain the concepts of confidentiality, availability and integrity.
1. Explain standard access control mechanisms (mandatory, discretionary, originator controlled) and how they can be used in conjunction with security models.
1. Describe use of cryptographic algorithms in various secure protocols including digital signatures, hash functions, symmetric key, and public key cryptography.
1. Explain various forms of authentication and identify social engineering attacks.
1. Explain security issues in networks, hosts, and applications and how they can be addressed
1. Identify privacy issues in computing systems and how they can be addressed

### Policies

|-|-|-|-|
|Grading|Attendance and participation|Academic Misconduct|
|Attendance&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5%<br>Lab&nbsp;notebooks&nbsp;&nbsp;&nbsp;65%<br>Final&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;30%|Attendance is required and will be taken each class. If you miss class, extra credit will be given back for outside communication that indicates you are keeping up with the material. You are expected to follow this [code of conduct](https://www.mozilla.org/en-US/about/governance/policies/participation/) when communicating.| * Includes allowing another student to copy your work unless specifically allowed by the instructor.<br>* Results in a grade of 0 for the assignment or exam.<br>* Results in the initiation of disciplinary action at the [university level](https://www.pdx.edu/dos/academic-misconduct).

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
* [Software setup](../software.md) -- tmux, ssh, git, etc.
* [Technical Writing](../technical_writing.md) -- if unfamiliar with markdown or LaTeX, this page will help
* [SSH tunneling tricks](../SSH_Tunnel_XRDP.md) -- SSH tunneling trick we will be using in various places through the term
* [Cracking Wifi](../netsec/crack_wifi.md) -- a brief introduction to cracking WiFi
* [Defensive measures](../firewalls.md) -- a brief introduction to firewalls and IPS/IDS
* [TunnelVision exploit against VPNs](https://github.com/leviathansecurity/TunnelVision) -- an exploit a malicious network admin could use to render most VPNs useless.

## Schedule (SUBJECT TO CHANGE -- CHECK REGULARLY)

| Week | Topic | Labs | Due on Monday |
| ---- | ----- | ---- | ------------- |
| 1 | Introduction<br>Careers and Roles in Cybersecurity (CyberPDX)<br>Principles and Approaches<br>Access Control and Authorization<br>Linux Basics (files, commands)| [Lab&nbsp;#1](hw1.md)| |
| 2 | Linux basics (command I/O, shell navigation, advanced files)<br>Basics (regex, file utilities, network commands, processes) | |Lab #1|
| 3 | Linux Access Control (permissions, setuid, sudo)<br>Applied cryptography: Encoding, Hash functions, Message Authentication Codes<br>Applied Cryptography: Symmetric, Asymmetric (Public-Key) encryption | [Lab&nbsp;#2](hw2.md)| |
| 4 | Applied Cryptography: Digital signatures, Certificates, Key exchange protocols, Perfect Forward Secrecy, Future Secrecy, Signal protocol<br>Authentication: Password security, Multi-factor authentication | | |
| 5 | Authentication: FIDO/Passkeys (Passwordless authentication), Zero-trust and continuous authentication<br>Social engineering (Spam, Phishing, Business Email Compromise, Scams, Fraud)<br>Network security: Data-link layer (802.11, WPA2)| [Lab&nbsp;#3](hw3.md) | Lab 2 |
| 6 | Network Security: Data-link layer (ARP), Network layer (IP, CIDR, Sniffing, Spoofing, Hijacking)<br>Network Security: Network layer (DDoS, IPSec/VPNs, firewalls and filtering, network segmentation, network intelligence, ICMP) |  |  |
| 7 | Network Security: Transport layer (TCP, TLS, certificate authorities and transparency, certificate revocation), Application layer: DNS security (DNS, DNSSEC) <br> Network Security: Application layer - DNS security (DoH, DoT, Oblivious DNS), E-mail security (SMTP/IMAP/POP over TLS, DKIM, SPF, DMARC)<br>Host Security: Host attacks (Initial access, Privilege escalation)| [Lab 4](hw4.md) | |
| 8 | Host attacks (Internal recon, Lateral movement, Persistence, Impact)<br>Host defenses (IDS/IPS/EDR, signature detection, anomaly detection, blocklisting and allowlisting, Software signing, Virtualization and isolation techniques, File system backup and encryption)<br>Application security: DevSecOps| | |
| 9 | Programming language and CPU security, Memory corruption, Return-oriented Programming, Canaries, ASLR, Control-Flow Integrity | | Lab 4|
| 10 | Supply-chain security <br> Privacy and anonymity security| | |
| Finals week | | | |
| | | | |

We will not be meeting the week of finals, and I will not be holding office hours. I will be available via email, but may not reply immediately, or even the same day.

## Assignments

### Labs and notebook

Lab assignments will be given each class covering the course material. You will perform each one, while maintaining a lab notebook in markdown that documents your progress via screenshots with your OdinID in them. The notebook should also include answers to any questions in the labs. Notebooks should be done in Markdown in their respective folders. Submission will be done via adding, committing and pushing the files to your private [CECS GitLab](https://gitlab.cecs.pdx.edu) repository.

Please add myself (dmcgrath) and your TA (jsimonds) as collaborators to your private repo. You can do this by going to the settings page for your repo, clicking on the "Manage access" tab, and then clicking on the "Invite a collaborator" button. You will need to add both myself and your TA as collaborators.

Always turn in what you have done on-time. Late work throughout the quarter may be compiled into a single submission that will be graded at the end of the last week of class in a file named notebooks/LateLabs.pdf. The notebook will be graded based upon the following rubric:

* Neatness and organization
* Completeness
* Inclusion of OdinID or project identifier in screenshots

## Academic or Student Support Services

### Accommodations

Accommodations for students with disabilities are determined and approved by Disability Resource Center (DRC). If you, as a student, believe you are eligible for accommodations but have not obtained approval please contact DRC immediately at 503-725-4150, drc@pdx.edu, or https://www.pdx.edu/disability-resource-center. DRC notifies students and faculty members of approved academic accommodations and coordinates implementation of those accommodations. If you have accommodations through DRC and wish to take the Midterm or Final Exam in the testing center, I strongly recommend that you schedule it before the end of week 1. If you are not registered with the DRC, you cannot register to take an exam in the testing center.

I want to make this class an open and welcoming environment for all. Your success is my goal.

### Religious Observance

Portland State University strives to respect all religious practices. If you have religious holidays that conflict with any of the requirements of this class, please see me immediately so that we can make alternative arrangements.

### Reach Out for Success

The [PSU Center for Student Health and Counseling](https://www.pdx.edu/health-counseling/) (SHAC) is staffed with folks who care and can help with a wide range of personal challenges. Here at PSU, there is never a need to tough things out alone.  

As a student you may experience a range of issues that can cause barriers to learning, such as strained relationships, increased anxiety, alcohol/drug problems, feeling down, difficulty concentrating and/or lack of motivation. These mental health concerns or stressful events may lead to diminished academic performance or reduce a student’s ability to participate in daily activities. PSU is committed to advancing the mental health and well-being of its students. If you or someone you know is feeling overwhelmed, depressed, and/or in need of support, services are available. You can learn more about the broad range of confidential mental health services available on campus via SHAC https://www.pdx.edu/health-counseling/.

SHAC also has resources for physical health, including flu shots. You can check out their COVID-19 resources page here: https://www.pdx.edu/health-counseling/covid-19-resources (including testing).

[Get Food Now](https://www.pdx.edu/student-access-center/food-assistance) Here at PSU, there is never a need to tough things out alone. Those who can, give, so those who need, have.

[Housing / financial crisis help](https://www.pdx.edu/dean-student-life/student-homelessness-and-economic-crisis). Here at PSU, there is never a need to tough things out alone. Emergency Housing, etc.

### Title IX

As an instructor, students frequently come to me for assistance in matters that are not related to the course material. Please be aware that PSU’s policies require instructors to report any instance of sexual harassment, sexual and relationship violence and/or other forms of prohibited discrimination to University Officials, who keep the information private. If you would rather share information about these experiences with a PSU staff member who does not have these reporting responsibilities and can keep the information confidential, please contact one of the following campus resources.

* Confidential Advocates: 503.894.7982, or by [scheduling on-line](https://www.google.com/url?q=https://psuwrc.youcanbook.me/&sa=D&source=editors&ust=1648503453184575&usg=AOvVaw0RnqMNvCBNc--7kOcXteWW) (for matters regarding sexual harassment and sexual and relationship violence)
* [Center for Student Health and Counseling (SHAC)](https://www.google.com/url?q=https://www.pdx.edu/health-counseling/&sa=D&source=editors&ust=1648503453185086&usg=AOvVaw24rcWJiE2_T6YESnL-eWaF): 1880 SW 6th Ave, 503.725.2800
* [Student Legal Services](https://www.google.com/url?q=https://www.pdx.edu/student-legal-services/&sa=D&source=editors&ust=1648503453185428&usg=AOvVaw0Yfw3-vB8E1gxcjod2WfI6): 1825 SW Broadway, (SMSU) M343, 503.725.4556 For more information, please complete the required student module Understanding Sexual Misconduct and Resources in Canvas.

[PSU Sexual Misconduct Response website](https://www.google.com/url?q=https://www.pdx.edu/sexual-assault/&sa=D&source=editors&ust=1648503453186003&usg=AOvVaw0kjTNvErvB5aNsMon4XKsT) gives you comprehensive information about how to support and/or report an incident.

Please complete the required student module [Understanding Sexual Misconduct and Resources](https://www.google.com/url?q=https://www.pdx.edu/diversity/understanding-sexual-misconduct-and-resources-student-module&sa=D&source=editors&ust=1648503453186548&usg=AOvVaw1QAxgICH1QI4x82uY-d1R0) in Canvas, which provides information about PSU policy and resources.

You may also report sexual and relationship violence to law enforcement on campus with [Campus Public Safety Office (CPSO)](https://www.google.com/url?q=https://www.pdx.edu/campus-safety/&sa=D&source=editors&ust=1648503453187321&usg=AOvVaw3tlkVac2wvw2rNVcAONxzT).

Or you may file an [anonymous report](https://www.google.com/url?q=https://docs.google.com/a/pdx.edu/forms/d/e/1FAIpQLScGJ2EsjqRT9MBkEkQCAuaeLfvZBiRDfHztvIEzMyCqO3DVJg/viewform&sa=D&source=editors&ust=1648503453188378&usg=AOvVaw34vcWBUk49whsysC6vhKX9) with [Campus Public Safety Office](https://www.google.com/url?q=https://www.pdx.edu/campus-safety/make-report&sa=D&source=editors&ust=1648503453188903&usg=AOvVaw3Xmu_iRL_ohJkBE9_wdUkK) or a [Bias Incident report](https://www.google.com/url?q=https://web.imaging.pdx.edu/AppNet/UnityForm.aspx?key%3DUFKey&sa=D&source=editors&ust=1648503453189336&usg=AOvVaw39Py9CfwBcDBS09re3kuCn) with the [Bias Review Team (BRT)](https://www.google.com/url?q=https://www.pdx.edu/diversity/bias-review-team&sa=D&source=editors&ust=1648503453189761&usg=AOvVaw3W0x7iOkMKgmykW6T0ksdn).  PSU does not typically investigate the reports that are made through these two avenues. These reports help PSU understand what students and employees are experiencing on and around campus and provide support where needed.
