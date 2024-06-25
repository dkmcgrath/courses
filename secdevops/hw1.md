Homework 1
Due Date: 2023-10-09 23:59:59
Submission: via GitLab repo

* auto-gen TOC:
{:toc}

## Introduction

This homework is intended for you to provide verification of a functional mini-lab environment. You will be using this environment for the rest of the term. In theory, you have already completed nearly all of this. However, I want to make sure that you have a working environment before we get too far into the term.

All work will be submitted via MarkDown documents within a gitlab repo. You will be using this repo for the rest of the term. This repo exists on the CECS intranet.

## Tasks

1. Create a private [GitLab repo](https://gitlab.cecs.pdx.edu/) called `secdevops-su24-<CECS>` (replace <CECS> with your actual MCECS username) and clone it to your local machine. You will be using this repo for the rest of the term. This repo exists on the CECS intranet, and uses your CECS credentials for authentication.
1. Add `dmcgrath` as members of your repo. This will allow us to view your repo and provide feedback.
1. Create a folder within the repo called `hw1`. This is where you will add documentation regarding this assignment.
1. Now that you have your repo set up, we'll be turning to the systems. Ensure that your BSD host has a running firewall and that your Ubuntu system is accessible. I would suggest you document everything you did in a markdown file in your repo called `hw1.md`.
   1. Create and store appropriate SSH keys for both hosts. 
      1. While you were given a key for the BSD system, I want you to generate a new one (while leaving the old one in place!). 
      1. Create a key for the ubuntu system.
      1. Ensure that you have Agent forwarding enabled in your local SSH client, and appropriate keys defined for both hosts.
      1. Include the contents of your `~/.ssh/config` file in your `hw1.md` file, to show you have a bastion or jump host configured.
   1. Take a screenshot of your FreeBSD terminal (after logging in) with the output of the command `ifconfig` and `hostname` showing. Add this to your repo and include it in your `hw1.md` file.
   1. Take a screenshot of the Ubuntu terminal with the output of the command `ip a s` showing. Add this to your repo and include it in your `hw1.md` file.
1. Follow the instructions on the [Ubuntu configuration](../ubuntu.md) page to configure the Ubuntu host. Document this in your `hw1.md` file.


## Submission

Once you have completed the above, you should have a markdown file in your repo called `hw1/hw1.md` that contains all the requested information above. Commit and push this to your repo. Also commit and include the requested screenshots. Once you have done this, you can consider the assignment submitted.
