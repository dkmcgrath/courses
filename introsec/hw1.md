# Homework 1

Due Date: 2024-04-12 23:59:59

* auto-gen TOC:
{:toc}

## Introduction

This homework is intended for you to provide verification of a functional virtual machine. You will be using this environment for the rest of the term. In theory, you have already completed nearly all of this. However, I want to make sure that you have a working environment before we get too far into the term.

All work will be submitted via MarkDown documents within a gitlab repo. You will be using this repo for the rest of the term. This repo exists on the CECS intranet.

If you aren't familiar with how to use git, please see the [git page](../git.md) for some basic instructions. If you're not familiar with markdown, please see the [technical writing page](../technical_writing.md) for some basic instructions.

## Tasks

1. Create a private [GitLab repo](https://gitlab.cecs.pdx.edu/) called `introsec-<CECS>` (replace \<CECS\> with your actual MCECS username) and clone it to your local machine. You will be using this repo for the rest of the term. This repo exists on the CECS intranet, and uses your CECS credentials for authentication.
1. Add dmcgrath and jsimonds as a member (developer or higher) of your repo. This will allow us to view your repo and provide feedback.
1. Create a folder within the repo called `hw1`. This is where you will add documentation regarding this assignment.
1. Now that you have your repo set up, we'll be turning to the VM. Follow one of the [macOS](../netsec/vms_on_macos.md) or [Windows](../netsec/hyper-v.md) instructions to get a VM setup and configured. I would suggest you document everything you did in a markdown file in your repo called `hw1.md`. And by suggest I mean require. I'm just being nice about it.
1. Take a screenshot of the Kali VM with the output of the command `ip a s` showing. Add this to your repo and include it in your `hw1.md` file.
1. Follow the instructions on the [Kali configuration](../netsec/linux_setup.md) page to configure the Kali VM. Document this in your `hw1.md` file.
1. Include a screenshot of the VM showing the successful output of the setup.sh script from the [Kali configuration](../netsec/linux_setup.md) page. This should be *the second time* you run the script, after you have rebooted the VM. It should mostly fit on the screen.
1. TryHackMe is a widely-used security training site that focuses on developing practical, hands-on skills for its users. The site is organized in "rooms" that contain lab content for users to complete to obtain badges. We will be using several of the site's free rooms as part of the course.

    Visit the site at [https://tryhackme.com/](https://tryhackme.com/) and create an account. If you find the exercises useful, consider a subscription to the site to continue your development after the course.
1. Throughout the course, we will be using the free rooms of TryHackMe to get you started on various security topics. Some of the TryHackMe rooms will launch machines on TryHackMe for you to work with. In order to access these machines easily, TryHackMe provides VPN support. Both Portland State and TryHackMe have support for the freely available OpenVPN client. The OpenVPN client is installed on all MCECS lab machines.

    Visit your first TryHackMe room at [https://tryhackme.com/room/openvpn](https://tryhackme.com/room/openvpn) and complete it using the machine you intend to work from for the course.

1. Join the following room on TryHackMe: [https://tryhackme.com/r/room/principlesofsecurity](https://tryhackme.com/r/room/principlesofsecurity). The room covers the fundamental security principles, terminology, access control models, and threat models. Complete the exercise.

    Take a screenshot showing completion of the room (e.g. all tasks and 100% completion) with your OdinID for your first lab notebook.

## Submission

Once you have completed the above, you should have a markdown file in your repo called `hw1/hw1.md` that contains all the requested information. Commit and push this to your repo. Also commit and include the requested screenshots. Once you have done this, you can consider the assignment submitted.
