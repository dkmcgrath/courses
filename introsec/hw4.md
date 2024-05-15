# Homework 3

Due Date: 2024-05-27 23:59:59

* auto-gen TOC:
{:toc}

## Introduction

This homework covers the general topic of network security. You will be looking at packet capture filters, packet traces in wireshark, and some basic network identification tasks.

## What you must do

1. Join the following room on TryHackMe: [https://tryhackme.com/r/room/whatisnetworking](https://tryhackme.com/r/room/whatisnetworking). This room covers the basics of `wireshark`. Complete the exercise.

    Take a screenshot showing completion of the room. This should be included in your `hw4.md` file.

    Thoughts:
    * I strongly encourage you to make use of the hints.
    * Capturing traffic requires you to be generating traffic. So you may have to do some things involving the network while capturing.

1. Join the following room on TryHackMe: [https://tryhackme.com/r/room/passiverecon](https://tryhackme.com/r/room/passiverecon). This room covers the basics of passive network reconnaissance. Complete the exercise.

    Take a screenshot showing completion of the room. This should be included in your `hw4.md` file.

1. Join the following room on TryHackMe: [https://tryhackme.com/r/room/activerecon](https://tryhackme.com/r/room/activerecon). This room covers the basics of passive network reconnaissance. Complete the exercise.

    Take a screenshot showing completion of the room. This should be included in your `hw4.md` file.

1. Join the following room on TryHackMe: [https://tryhackme.com/r/room/nmap01](hhttps://tryhackme.com/r/room/nmap01). This room covers the basics of `nmap`. Complete the exercise.

    Take a screenshot showing completion of the room. This should be included in your `hw4.md` file.

1. We often wish to examine network traffic to analyze whether a given network is running correctly, is under attack, has secrets in it we would like to reveal or protect, and so on.  There is an engineering trade-off here.  We can’t store and analyze all the data that flies by in the network.  So we would like to use a portion of the total data to decide where to look deeper.

   Often the initial security analysis uses protocol headers or security and application logs.  
   
   * This information is small, so it can be stored for more traffic over a longer period of time
   * This information can be determined from packets flying by with a minimum of processing, so it is possible to get the info without either spending a fortune in monitoring hardware or slowing down the network traffic
   
   There is a perception that the content data is “sensitive” and that header data is “anonymized” or information that people don’t care as much about.  If you have time to read Kieran Healy’s amusing article on [“Using Metadata to Find Paul Revere”](https://kieranhealy.org/blog/archives/2013/06/09/using-metadata-to-find-paul-revere/), you can see that this is not always a valid perception. Side note: there's a deeper article linked from the bottom of that page that is also worth reading if you want a more in-depth analysis.

   Let’s see what we can find from the most basic packet header data. The trick here is to rearrange the data in various ways and look for ‘spikes’ in frequency.  Then, look at what all the frequent items have in common, such as the same protocol, similar IP addresses, etc.  To do this well, you need to know about common TCP and UDP services.  Fortunately, we have Google to help us with that!

   You are provided with two samples of packet data, entitled ‘[R](R.csv)’ and ‘[O](O.csv)’.  The packet data is in order, and covers a brief period of time.  For each packet, you get:
   * Length, IP type, IP Source Address, IP Destination Address
   * TCP: Flags, Source port, Destination Port
   * UDP: Source port, Destination port
   * ICMP: type, code
   
   The data is stored in a textual CSV format (you can even look at it using a terminal or read it into a spreadsheet).  In this assignment, you will write scripts to analyze the data.  We have provided starter scripts in PERL and PYTHON, entitled [scancsv.py](scancsv.py). There is a [packet object library](CSVPacket.py), or you can use `impacket`, `scapy`, or any other ingestion/conversion library you like.

## Submission

Once you have completed the above, you should have a markdown file in your repo called `hw3/hw3.md` that contains all the requested information. Commit and push this to your repo. Also commit and include any requested screenshots. Once you have done this, you can consider the assignment submitted.

In order to include output from your shell, see the [technical writing page](../technical_writing.md) for some basic instructions. For instance:

```sh
❯ ps -efH --no-header | awk '{print $1}' | grep -Ev $(python3 -c 'import sys; print("|".join(sys.argv[1:]))' $(cut -f1 -d':' /etc/passwd)) | sort | uniq -c | sort -rn | head -n 11
     30 USER01
     27 USER02
     24 USER03
     23 USER04
     23 USER05
     22 USER06
     22 USER07
     19 USER08
     19 USER09
     19 USER10
     18 USER11
```

Could be created with the following markdown:

````markdown
```sh
❯ ps -efH --no-header | awk '{print $1}' | grep -Ev $(python3 -c 'import sys; print("|".join(sys.argv[1:]))' $(cut -f1 -d':' /etc/passwd)) | sort | uniq -c | sort -rn | head -n 11
     30 USER01
     27 USER02
     24 USER03
     23 USER04
     23 USER05
     22 USER06
     22 USER07
     19 USER08
     19 USER09
     19 USER10
     18 USER11
```
````