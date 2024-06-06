#Final Project CS596

Due Date: Friday of Finals Week 23:59:59

* auto-gen TOC:
{:toc}

## Introduction

Don't want to do the suricata work, eh? Well, that's fine. Let's do something else then. Let's do a little bit of network MiTM (monster in the middle). But let's do it via hardware! The inspiration for this idea is the Hak5 Packet Squirrel.

## What you must do

Take the platform of your choice, and ensure you have multiple NICs available on it. You will be creating this MiTM as a transparent network tap, with optional packet modification. You will need to perform the following tasks:

1. Create a network tap that will passively monitor traffic on a network. This should be able to handle at least 100Mbps of traffic without noticeable latency. The packets should be stored on the local device for later analysis, with optionally the ability to forward them to a remove device via the WiFi interface (if available).
1. Create a proof of concept "attack" that will modify all TTL values in packets passing through the device. Set them all to 65.
1. Create 2 additional proof of concept attacks that do some other active packet modification.
1. Write it all up and document it.


## What to turn in

You will be submitting this via your gitlab repo, in a markdown file called `final/final.md`. This should contain the high level description of how you went about the setup of the device, as well as the proof of concept attacks. You should also include a pcap file that demonstrates the rule in action. This pcap file should be named `final_x.pcap` (where x is an integer that maps to attack descriptions in your document) and should be in the `final` directory of your repo.
