# Homework 4

Due Date: 2024-06-09 23:59:59

* auto-gen TOC:
{:toc}

## Introduction

This last exercise is a bit of a hodgepodge. Your primary task is to reverse engineer a binary bomb. You will also work with Snort, a popular open-source intrusion detection system. This will give you a taste of what it's like to work with a real-world IDS.

## What you must do

1. This exercise will introduce the concepts of reverse engineering through the use of a "binary bomb." This is an executable which requires specific input from the user, but has no external indications as to what the input should be. Similar in concept to so-called "crackme" files, binary bombs were developed specifically for an academic environment at CMU. Obtain the bomb file [here](bomb).

    Reverse engineering (RE) is the process of taking an object, program, doohickey, what-have-you and figuring out the ways in which it functions. Within the context of this class, reverse engineering refers to the use of tools, techniques, and experience to determine the ways in which a program functions, the input it wants, and typically ways in which it can be exploited.

    While many tools exist to aid in the process of software reversing -- think [IDA](https://hex-rays.com/products/ida/index.shtml), [ghidra](https://www.nsa.gov/resources/everyone/ghidra/), [Cutter](https://cutter.re/), etc. -- we will be going old-school and just using gdb. At least, that's the suggested approach, primarily due (again) to familiarity. Most RE tools have extensive and steep learning curves, and frankly aren't the point of this class.

    The typical process of reverse engineering using a tool like GDB involves obtaining the binary, loading it in to GDB, setting some breakpoints, and then stepping through it. Some additional tools that may make this easier include `objdump`, `strings`, `man`, `rasm2`, the [`GEF`](https://hugsy.github.io/gef/) GDB extension (or [`PEDA`](https://github.com/longld/peda) or [`pwndbg`](https://github.com/pwndbg/pwndbg)), `tmux`,`zsh`, etc. Some of those may be more useful than others...

    Your goal for this RE challenge is to determine the inputs to defuse each of the 6 phases of the bomb. Incorrect input will result in the bomb exploding.

    Record what you did, how you did it, and include lots of screenshots. Document it in you hw5.md file.

    Hints:
    * If you go with `pwndbg`, and you are using ada or babbage, you will need to modify the install script to dummy out the `apt` installation step. The rest will work just fine. You'll also want to install [splitmind](https://github.com/jerdna-regeiz/splitmind) in order to have useful split context windows.
    * You could also do all of this with `lldb` and something like [lldbinit](https://github.com/peternguyen93/lldbinit) or [voltron](https://github.com/snare/voltron). But I'll leave that up to you.
    * Phase 2 is historically the most difficult phase for folks.

1. Complete the following two rooms on TryHackMe:
    * [Snort](https://tryhackme.com/r/room/snort)
    * [Snort Challenges](https://tryhackme.com/r/room/snortchallenges2)

    Document your progress in your hw5.md file.

1. Static application security testing (SAST) is a method of testing an application for security vulnerabilities by examining the source code. Some of the most popular tools for this are [SonarQube](https://www.sonarqube.org/), [Snyk](https://github.com/snyk/cli), and [SemGrep](https://github.com/semgrep/semgrep). Install one of the SAST tools on your VM and run it against a project of your choosing. Document your progress in your hw5.md file.

1. Dynamic application security testing (DAST) is a method of testing an application for security vulnerabilities by examining the application in its running state. [GVM](https://github.com/greenbone/openvas-scanner) is a popular tool for this. Install GVM on your VM and run it against a project of your choosing. Document your progress in your hw5.md file.

## Submission

Once you have completed the above, you should have a markdown file in your repo called `hw5/hw5.md` that contains all the requested information. Commit and push this to your repo. Also commit and include any requested screenshots. Once you have done this, you can consider the assignment submitted.

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