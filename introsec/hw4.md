# Homework 4

Due Date: 2024-05-27 23:59:59

* auto-gen TOC:
{:toc}

## Introduction

This homework covers the general topic of network security. You will be looking at packet capture filters, packet traces in `wireshark`, and some basic network identification tasks.

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

1. Complete the following `tcpdump`/BPF practice exercises.
   1. Perform a tcpdump capture where you only capture DNS packets.
   1. Perform a tcpdump capture where you capture TCP packets that are destined for either port 443 or 8080, and originate from your computer.
   1. Perform a tcpdump capture where traffic is either UDP or TCP, is inbound to your computer, and destined for a port between 20000 and 35000.

    All dumps should have full data dumps without link layer headers, in hex and ascii, with Unix epoch style timestamps. Something like this:

   ```
   1585339575.038549 IP (tos 0x0, ttl 64, id 37629, offset 0, flags [DF], proto UDP (17), length 60)
        kali478-0.38378 > _gateway.domain: [bad udp cksum 0x6ede -> 0x96ae!] 54659+ A? www.google.com. (32)
      	0x0000:  4500 003c 92fd 4000 4011 390f ac10 8b81  E..<..@.@.9.....
      	0x0010:  ac10 8b02 95ea 0035 0028 6ede d583 0100  .......5.(n.....
      	0x0020:  0001 0000 0000 0000 0377 7777 0667 6f6f  .........www.goo
      	0x0030:  676c 6503 636f 6d00 0001 0001            gle.com.....
   ```

   Captures can be included in your markdown file by enclosing them in triple backticks, like so:

   ````
   ```
   1585339575.038549 IP (tos 0x0, ttl 64, id 37629, offset 0, flags [DF], proto UDP (17), length 60)
        kali478-0.38378 > _gateway.domain: [bad udp cksum 0x6ede -> 0x96ae!] 54659+ A? www.google.com. (32)
      	0x0000:  4500 003c 92fd 4000 4011 390f ac10 8b81  E..<..@.@.9.....
      	0x0010:  ac10 8b02 95ea 0035 0028 6ede d583 0100  .......5.(n.....
      	0x0020:  0001 0000 0000 0000 0377 7777 0667 6f6f  .........www.goo
      	0x0030:  676c 6503 636f 6d00 0001 0001            gle.com.....
   ```
   ````

   A minimum of 10 packets, as requested, should be included for each capture. You can use the `-c` flag to limit the number of packets captured.

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

   The R data (100k packets) is a lot smaller than the O data (1M packets).  Prototype your scripts using R data, then switch to O data to apply the concepts on a larger data set.

   The ultimate goal of this exercise is to understand the function of the networks monitored in the R and O data sets.  What is their function?  We will choose among: work, home, data center, ISP.  On the way, we’ll learn as much as we can about these networks from the scanty data that we have.

   The starter scripts collect statistics based on IP protocol numbers:

    ```sh
    user@kali:~/Lab2$ python scancsv.py R.csv
    Num packets: 99142, Num bytes: 71683046
    IP Protocols:
     1:          7
     2:          2
     6:      39138
    17:      59995
    ```

   You can look the IP numbers up in `/etc/protocols` to find out that IP protocol `1=icmp`; `2=igmp`; `6=tcp`; `17=udp`.  For example, ICMP (IP Protocol 1) occurs in 7 packets.  You will have learned a little of these protocols from the advance reading.  If not, google them now!

   Each protocol has its own uses.  For example, IGMP (proto=2) is used for router-to-router communications.  So we could find the addresses of routers by looking at flows that use this protocol.  Without writing a script to do this, we could just use the grep command:
   
   ```sh
   user@kali:~/Lab2$ grep -e len -e '^[0-9][0-9]*,2,' R.csv
   len,proto,ipsrc,ipdst,tcpflags,tcpsport,tcpdport,udpsport,udpdport,icmpcode,icmptype
   28,2,10.5.63.36,234.42.42.42,,,,,,,
   28,2,10.5.63.36,234.142.142.142,,,,,,,
   ```
   
   We can now infer that 10.5.63.36 is a router IP address.  The other addresses that start with 234.*.*.* are multicast addresses (put them into google to see this).
   
   1. Find Statistics on TCP and UDP Services
        Most interesting user protocols run on TCP although a few run on UDP. This usually works as follows:
        * A server process listens on a given TCP or UDP port number.  By convention, these “well known ports” are allocated from 1-1024 (some are outside that range by now).  A well-known port is often called a service.
    	* Clients connect in to the server using this as the TCP or UDP destination port. 
   The file /etc/services contains a listing of well-known port numbers for TCP and UDP.  
   
   1. Extend your script’s statistics gathering to count the use of all well-known destination port numbers for TCP and UDP (ports  1-1024).  For example, you should be able to look up in your output how many TCP packets have destination port 80 and how many UDP packets have destination port 53.  Run your new script on R and O data.  Enable this function using a ‘-stats’ flag (i.e., the script should have no output unless there is a -stats flag in the command line).
   1. Based on this information, characterize the main functions on each network.  What kind of network is it? (e.g., work, home, data center, ISP)

   1. Add to your script an option called `--countip` which creates list of distinct IP addresses with their usage counts.  Sort the list by the usage count, not by the IP address.
   1. Run your `countip` script on R and O data.  Does this inform your answer in [2]?
   1. Attempt to determine the network number (network prefix) that seems to dominate the traffic.
   There are some IP protocols that are typically used between routers or other special networking devices.  Traffic from these protocols can identify the infrastructure of the network under observation.
   1. Generate sorted output from `--countip` for the IP protocols to identify all the IP addresses that use:
        * GRE (Generic Routing Encapsulation) – this is used to create tunnels between networks with overlapping address spaces.  It is also the base protocol for PPTP, a remote access mechanism.
        * IPSEC – this is the protocol that creates virtual private networks, creating an overlay network structure on top of the Internet.  Most IPSEC is router-router these days.
        * OSPF – Open Shortest Path First routing protocol.  This is the ‘standard’ routing protocol for Internet routers, allowing them to discover the topology and choose the best routing paths as connections between routers appear and disappear.
        * Hint: create a new protocol argument to filter the data to `--countip` to just include lines for these protocols.  Alternately, use the GREP pipeline in the example above, for IGMP traffic, and change ‘2’ to the right protocol number.
   1. Find another network prefix that also seems to be associated with this traffic.
   1. Does the OSPF information inform your answer to question 2 above?

   The server machines are the main assets of each site.  Can we find them?

   Imagine drawing a diagram for each service, with a line from each client machine that uses the service to the server that provides it.  Then the servers look like stars, with clients around each server.  Important servers will stick out as stars with lots of spokes.

   To find the ‘stars’ in the diagram, we want to find IP addresses that are the destination of many transactions.

   1. Add an option to your script `--connto`, which counts the number of packets sent to each service (ports 1-1024) on the network.  For example, a dictionary maps each ipdst to the tuple `<proto, dport>`, where `proto` is `tcp` or `udp`, based on the IP protocol (6  or 17) and `dport` is the value of `tcpdport` or `udpdport`.
   1. Sort the output by the number of distinct source IP address – source port combinations, so that servers which serve a lot of different connections all cluster at one end of the output.  
   1. For output, generate a summary line that shows, for each destination IP address, how many distinct source IP addresses accessed it, and what ports were referenced:

      ```
      ipdst 1.2.3.4 has 334 distinct ipsrc on ports: udp/53, tcp/80, tcp/443
      ipdst 5.6.7.8 has 335 distinct ipsrc on ports: tcp/22, tcp/25
      ```
    Include your script, the output of your script, and your analysis of the output in your `hw4.md` file. Include any graphs, images, or other artifacts you generate as part of this analysis.

## Submission

Once you have completed the above, you should have a markdown file in your repo called `hw4/hw4.md` that contains all the requested information. Commit and push this to your repo. Also commit and include any requested screenshots. Once you have done this, you can consider the assignment submitted.

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