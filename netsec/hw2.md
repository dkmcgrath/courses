# Homework 2

Due Date: 2024-05-13 23:59:59

* auto-gen TOC:
{:toc}

## Introduction

`tcpdump` is a packet capture utility that we will be using extensively throughout the rest of this course. Let's get some practice using it! You've done a couple of practice exercises, let's put them to use!

`tcpdump` (and `wireshark` and `tshark`) use BSD packet filter (BPF) style filters. Let's work a bit with them!

## What you must do

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

You might notice that all the packets you capture either originate or terminate at your computer. There's a reason for this, and we'll go over it in class, as well as some ways to get around it.

## Submission

Once you have completed the above, you should have a markdown file in your repo called `hw2/hw2.md` that contains all the requested information. Commit and push this to your repo. Also commit and include the requested screenshots. Once you have done this, you can consider the assignment submitted.
