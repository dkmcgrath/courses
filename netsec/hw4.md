# Find the Firmware!

Due Date: 2024-02-26 23:59:59

* auto-gen TOC:
{:toc}

## Introduction

Often, it is possible to tap the communication between a device and its update servers. In this way, you can capture the transfer of the updated firmware. If you are lucky, it's a full firmware that is transmitted, the update is over an unencrypted channel, and it's transmitted as a single HTTP session. Unfortunately, the ideal case is fairly rare. Increasingly, updates are delivered over secured connections, it's often just a delta or patch that is transmitted, and it's even sometimes transmitted in small chunks over multiple sessions.

## What you must do

Using the tools you've learned in this module, dissect the provided packet capture and extract the firmware. You will find the packet capture at `ada.cs.pdx.edu:/disk/scratch/dmcgrath/firmware.pcap`. Simply `scp` it to your VM. It is important to note that HTTP often transmits binary data via BASE64 encoding!

Some useful information regarding the firmware you're after:

```
┌─(dmcgrath@kali:pts/3)─────────────────────────────────────────────────────────────────────────(~)─┐
└─(14:43:%)── binwalk download.bin #what it should look like                          ──(Wed,Sep23)─┘

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
48            0x30            Unix path: /dev/mtdblock/2
96            0x60            LZMA compressed data, properties: 0x6D, dictionary size: 8388608 bytes, uncompressed size: 4438276 bytes
302958        0x49F6E         MySQL MISAM index file Version 4
1441888       0x160060        Squashfs filesystem, little endian, version 4.0, compression:xz, size: 2208988 bytes, 1159 inodes, blocksize: 262144 bytes, created: 2019-08-06 21:20:37

┌─(dmcgrath@kali:pts/3)─────────────────────────────────────────────────────────────────────────(~)─┐
└─(14:43:%)── md5sum download.bin                                                     ──(Wed,Sep23)─┘
7aa6a7ebcbd98ce19539b668ff790655  download.bin
┌─(dmcgrath@kali:pts/3)─────────────────────────────────────────────────────────────────────────(~)─┐
└─(14:44:%)── sha512sum download.bin                                                  ──(Wed,Sep23)─┘
2a7719719aa4f869586a7043f532e01ed4985e5c25b9a54979ac7d50c67820ec61c2805d6169b9c95a98104b8fb1d4f9ec698d23881360e99f5232a4f3cf12d4  download.bin
┌─(dmcgrath@kali:pts/3)─────────────────────────────────────────────────────────────────────────(~)─┐
└─(14:44:%)──                                                                         ──(Wed,Sep23)─┘
```

Once you have a firmware extracted that matches the above, use a tool called binwalk to extract the contents (this isn't a reverse engineering class, use the -M and -e options), then answer a few questions:

1. What architecture is the firmware intended to run on?
1. What OS is the firmware running?
1. What users are present on the system?

Write a document detailing how you extracted the firmware, how you investigated the firmware, and answers to the above questions. Please make sure to include any code you wrote or commands you executed.

## Submission

Everything above should be documented in a markdown file in your repo called `hw3/hw3.md`. Commit and push this to your repo. Once you have done this, you can consider the assignment submitted.
