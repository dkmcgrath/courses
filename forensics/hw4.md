# Timeline analysis and Network Forensics

Due Date: 2024-03-17 23:59:59

* auto-gen TOC:
{:toc}

## Timeline Analysis

### Introduction

Kelly Copy is a researcher at the University of Illinois studying water tables. She submitted a proposal to a federal funding agency. Allison Origin is a graduate student in another lab at the university. Allison claims that Kelly stole her data and writing and used the results to produce the proposal. Allison submitted the USB drive she kept her research on, which was imaged (obtain `tim.dd` via `scp <ODIN username>@linux.cs.pdx.edu:/disk/scratch/dmcgrath/tim.dd .` from your VM) though all the data has been deleted. Kelly's computer was also imaged as a part of the investigation (obtain `tim2.dd` via `scp <ODIN username>@linux.cs.pdx.edu:/disk/scratch/dmcgrath/tim2.dd .` from your VM). You’ve been hired by the university to investigate Allison’s claims.

### File system forensics
Let's begin by looking at the file system of the thumb drive (tim.dd.)

`mmls tim.dd`

There's a FAT32 partition on the thumb drive. We'll use Sleuthkit, a classic file system forensics tool, to examine the file system on this disk image.

```sh
❯ sudo apt-get install sleuthkit
❯ fls -o 2 tim.dd
```

`fls​` is intended to be analogous to the Unix ​ls​ command, but for a file system. The `​-o`​ argument indicates the offset of the partition, which we can get from the `​mmls​` command.

### File system timeline

The raw output of `​fls​` shows some interesting data relevant to our case, but we'd ideally like to view what happened to the file system chronologically. We can do this by creating a timeline.

```
❯ fls -l -m "/" -z CST6CDT -f fat32 -r -o 2 tim.dd > body.txt
❯ mactime -b body.txt -d > tim.csv
```

You can view the csv file produced by `mactime` in a text editor or Excel. Alison says she was working in Microsoft Word. Search through the timeline for a "docx" file. When was this file deleted?

### Deleted file recovery

The "meta" column in the `mactime` output contains the inode address of the deleted file. Let's recover it using another `sleuthkit` command. `icat` works similar to `cat`, but based on inode numbers.

```sh
❯ icat -f fat32 -o 2 tim.dd ​inode​ > recovered.docx
```

Do the contents of this file look familiar? Using what you already know, you should be able to view the metadata from this file to recover more clues. Who created the file? When? What software were they using?

### Super timeline/plaso

Plaso is a powerful, integrated tool and Python backend for doing timeline forensics that incorporates Sleuth Kit. Using this tool, we can integrate artifacts from the file system, registry, log files and much more into a comprehensive timeline. Running the program produces a binary .dump file, which is not human-readable. The default behavior is to use all the parsers available in plaso (e.g. file system events, registry changes, and event logs.)

If you haven't been able to make plaso work, install it from source via

```sh
❯ sudo apt remove python3-plaso plaso
❯ git clone https://github.com/log2timeline/plaso
❯ cd plaso
❯ sudo -H python3 -m pip install -r requirements.txt
❯ sudo -H python3 setup.py build
❯ sudo -H python3 setup.py install
```

There may be some complaints about not wanting to use pip because `externally-managed-environment`. This just means you have to either use a virtual environment or pass the `--break-system-packages` flag to the `pip` command. I prefer the latter, personally.

Installing plaso takes a chunk of time.

The below command will take a LONG LONG time. ​Even the image for this simple scenario contains hundreds of thousands of events.

```sh
❯ log2timeline.py --vss_stores 3 --volumes all --hashers all --parsers webhist,win7,win7_slow,win_gen --storage-file tim2.plaso tim2.dd
```

We can use the dump file to build a human-readable csv format using psort.py. It's also possible to output in other formats, including SQL databases. ​This will take a LONG LONG time.

```sh
❯ psort.py --output_time_zone "CST6CDT" -w tim2.csv -o dynamic tim2.plaso
```

Suggestions to help make a smaller file: cat tim2.dd | grep .docx > new.txt

Look at the `new.txt` file.

As you might imagine, a full timeline of all the events that happened on the system is a bit much for a human to read. To pare down our search, you can take a time slice around the time the documents were deleted from the USB device we examined earlier or search for interesting strings in the timeline.

Use this final timeline to complete your investigation. What was the sequence of events that lead to the creation of ​proposal.pdf​ and the deletion of the contents of the USB drive? Can you establish who is responsible?

### Report
Write a 1-2 page comprehensive forensic report of your findings with the following sections:

* Summary - a brief summary of the report
* Purpose - explain the purpose of your investigation
* Methodology - describe the tools and methods you used to investigate the evidence
* Findings - clearly state the facts you uncovered from your investigation in an unbiased way
* Conclusions - summarize your findings and describe how they relate to the overall case.

### Reference Material

* http://blog.kiddaland.net
* http://plaso.kiddaland.net

### Submission

This report should go in your repo in a file called `hw4/hw4_1.md`.

## Network Forensics

### Introduction

John wakes up in the morning and found that his MacBook Pro, Android phone, and iPhone are missing. He thinks he must have lost them at the bar last night. Later that day, he calls the bar, and the bartender confirms that they found no iPhone last night. John rushed to the campus cops and files a missing device case.  However, he could not provide the MAC address of the devices. He was able to give his netid: `jschmo`.

As a forensics investigator you are called in to investigate the case. You have been given two log files:

* [radius.csv](radius1.3.csv): Contains authentication logs. One of the fields in this file contains the Wireless Access Point numbers ( in the form of ‘id 216’, ‘id 164’ etc)
* [dhcp.csv](dhcp1.1.csv): This is the DHCP log containing only the relevant data

You can use any of the commonly available tools/scripting languages (e.g. grep, cat, awk/python/bash scripts etc) to answer the following questions.

### Questions:

* List the MAC addresses that belong to John’s devices.  Also find the manufacturer’s of the devices. There are online MAC address lookup tools you can use.
* What is the MAC address for the missing Mac Book Pro (MBP) and Android Phone?
* What are the IP addressed of John’s devices?
* List the Access Points with which the MBP connected at different times.
* What is the MAC address of the iPhone?
* What evidence shows that the user ‘jerk’ stole the MBP?
* There are quite a few login failures from jschmo’s side. Will it be reasonable to think that these are attempts to break into jschmo’s account?

### Submission

Please answer all the above questions in a file called `hw4/hw4_2.md` in your repo. Please list the questions and then provide the answers in the same order. It will just make my life easier.