# Hacking WiFi!

Due Date: 2024-05-20 23:59:59

* auto-gen TOC:
{:toc}

## Introduction

So you've followed the instructions to break into WiFi networks. Now, what should we do with that?

## What you must do

1. Using the `bettercap` tool, crack the NetSec WiFi network password. This is a WPA2 network, and is currently living in FAB 88-03. It is accessible for various points in the near vicinity of that room. You have already used the `aircrack` suite to do this, so you know the password. But let's pretend we don't.
   1. Use `bettercap` to find the BSSID and connected clients of the NetSec network.
   1. Use `bettercap` to perform a deauth attack on the network and capture the 4-way handshake.
   1. Use the `hcx` toolsuite to convert the captured handshake to a format that `hashcat` can understand.
   1. Crack the password using `hashcat`. You should use the `rockyou.txt` wordlist.

1. Once you have documented all of the above (commands, output, everything you would need to walk through it again) in your `hw3.md` file, connect your workstation to the wireless network. You should be able to do this with the password you just cracked. Take a screenshot showing the connection to the network. The easiest way is to the use the `nmtui` tool.
1. Now that you have access to the network, use the `nmap` tool to scan the network. You should be able to find the IP address of the router and the IP addresses of the associated clients. Document this in your `hw3.md` file.
1. For each associated client, use the `nmap` tool to scan the client. You should be able to find the open ports and services running on the client. Document this in your `hw3.md` file.
1. There is an RTSP stream active on the network. Find it, access it, and take a screenshot of what it's looking at. What is it? What is its capacity? When was it manufactured? Document this in your `hw3.md` file.

## Submission

Everything above should be documented in a markdown file in your repo called `hw3/hw3.md`. Commit and push this to your repo. Once you have done this, you can consider the assignment submitted.
