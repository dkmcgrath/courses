# Homework 2

Due Date: 2024-04-29 23:59:59

* auto-gen TOC:
{:toc}

## Introduction

This lab is all about Linux. We'll start with some basic tutorials on TryHackMe to get you familiar with the Linux command line. Then we'll move on to some more advanced topics.

1. Download the following free ebooks:
   * [_The Linux Command Line_](http://linuxcommand.org/tlcl.php) (Direct [PDF link](https://sourceforge.net/projects/linuxcommand/files/TLCL/19.01/TLCL-19.01.pdf/download))
   * [_Adventures with the Linux Command Line_](https://sourceforge.net/projects/linuxcommand/files/AWTLCL/21.10/AWTLCL-21.10.pdf/download)
   * [_The Linux Development Platform_](https://archive.org/details/ost-computer-science-0130091154/mode/1up)
   * 

1. Join the following room on TryHackMe: [https://tryhackme.com/room/linuxfundamentalspart1](https://tryhackme.com/room/linuxfundamentalspart1) . The room covers basic Linux commands for navigating directories and files (`echo`, `whoami`, `cd`, `ls`, `cat`, `pwd`, `find`, `grep`, `wc`, as well as operators`&`, `&&`, `>`, and `>>`). Complete the exercise.

    Take a screenshot showing completion of the room
1. Join the following room on TryHackMe: [https://tryhackme.com/r/room/linuxmodules](https://tryhackme.com/r/room/linuxmodules). This covers lots of useful linux commands! Complete the exercise.

    Take a screenshot showing completion of the room.
1. `grep` is a tool which allows for regular expression matching of contents of a line or file. It is commonly known as a filter -- it removes unwanted cruft and only allows the display or further processing of data that matches (or doesn't match, in the case of an inverted search).

    `grep` has multiple modes, which can be invoked with an alternative name or a specific flag. For instance, to use extended regular expression syntax, you can invoke as `egrep` or call as `grep -E`. Both operate identically. The different modes are

    * Extended regular expressions: -E
    * PERL compatible regular expressions: -P
    * Fixed string matching: -F
    * Default behavior, if you want to specify it as a flag (scripts and the like): -G

    `grep` is a tool you will likely make a ton of use of. That will require both a knowledge of regular expressions and an understanding of how `grep` works and is controlled by its flags. See the `man` page for `grep` for the latter, and you're on your own for anything beyond very basic regular expressions. I'm a firm believer that if you try to solve a problem with regular expressions, you now have many problems, rather than just the one.

    Use `grep` to find the following things in the `/usr/share/wordlists/rockyou.txt` file (you may have to decompress it or use `zgrep`):

   * All lines that contain the word "password" (case-sensitive)
   * All lines that contain "password" (case-insensitive)
   * All lines that end with exactly 3 numerical digits
       * with an anchor
       * without an anchor
   * All lines that contain exactly 3 numerical digits, in any position (do not have to be adjacent, just 3 total)

    For each of the above, also provide the number of lines that match the criteria.
1. `sed` is the stream editor. Please look up the `sed` manpage, and provide a command to do the following:
   1. Replace all instances of `from this.that import something` to `from that import something` in all python files in the current directory tree. Remember that `sed` can be used to edit files in place, so you don't need to worry about redirection. Remember the `find` tool I mentioned in class?
   1. Print lines 312-345 of a file (inclusive). This is a common use of `sed` to print a range of lines from a file. Use any file you like for this, as long as it has enough lines.
   1. In the `/etc/ssh/sshd_config` file, replace the line `#PasswordAuthentication yes` with `PasswordAuthentication no`. This is a common security practice to disable password authentication for SSH. Use `sed` to do this in place, as well.
1. Run each of `objdump`, `nm`, and `readelf` on `/bin/ls`. 
   * What do each of these tools do?
   * What information do they provide?
   * How do they differ from each other?

   Give examples of each tool's output.
1. Virtual environments are a common feature in today's python development ecosystem. Each environment must be activated in order to be used, by sourcing the `activate` script in the environment's `bin` directory. Typically, this file exists in a `.env` subdirectory, but not always. Write a command which will activate the virtual environment in the current directory, regardless of where the `activate` script is located. Ensure that it is in `bin` directory (immediately), and it is named (exactly) `activate`.

    Now write a shell function you can use to perform this action from anywhere in the filesystem. This should be a `zsh` function (as that's the default on Kali).

1. Take a look at the following pipeline (you can run this on ada for real results)

   ```sh
   $ ps -efH --no-header | awk '{print $1}' | grep -Ev $(python3 -c 'import sys; print("|"s.join(sys.argv[1:]))' $(cut -f1 -d':' /etc/passwd)) | sort | uniq -c | sort -n
   ```
    No, I don't type that every time. I have it as an alias in my startup script, since it's how I print out a list of users who are causing excessive load on the server. Play with it, see if you can improve on it. You can also see the use of immediate python combined with the use of `awk`, `cut`, and `grep`.

    Questions to answer:

    1. What do you think the `grep` portion does? Why is that useful?
    1. What is an alias?
    1. Can you replace the `awk` pipeline component with a `cut`? What about the reverse?
    1. Take a look at a tool called `paste`. How might you use it to replace the use of `python` in this pipeline?

1. Join the following room on TryHackMe:https://tryhackme.com/room/linuxfundamentalspart3 .

   The room covers utilities for editing files and downloading content via the command line interface (`nano`, `wget`, `scp`). It also covers basic process commands (`ps`, `kill`), system management commands (`systemctl`), and timed commands (`cron`). Complete the exercise.

   Take a screenshot showing completion of the room

## Submission

Once you have completed the above, you should have a markdown file in your repo called `hw2/hw2.md` that contains all the requested information. Commit and push this to your repo. Also commit and include any requested screenshots. Once you have done this, you can consider the assignment submitted.

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