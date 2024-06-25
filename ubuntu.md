Ubuntu Configuration

* auto-gen TOC:
{:toc}

At this point, you should have an Ubuntu Server VM running. If you don't, go back and do that. I'll wait. If you do, then you're ready to start configuring it. 

## Connectivity

### Getting an IP address

If you set up the firewall correctly, it should all just automagically work. The Ubuntu installer defaults the single NIC to using DHCP. Assuming you have access to the system, you obviously have networking configured correctly.

Verify that you have a proper address using:

```sh
$ ip address show #for the lazy: ip a s
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 76:6d:65:10:9e:a1 brd ff:ff:ff:ff:ff:ff
    inet 192.168.33.63/24 metric 100 brd 192.168.33.255 scope global dynamic enp0s1
       valid_lft 42206sec preferred_lft 42206sec
    inet6 fe80::746d:65ff:fe10:9ea1/64 scope link
       valid_lft forever preferred_lft forever
```

`lo` is your link-local loopback interface. `enp0s1` is your first ethernet interface. In both cases, you can see the characteristics of the interface, including the IP address. If you don't see an IP address, then you need to go back and fix your freeBSD VM. If you do see an IP address, then you're good to go. If you are on Windows, you may have `eth0` rather than `enp0s1`. Different hypervisors use different naming conventions. The important thing is that you have an IP address.

### Connecting via SSH from your host system

OK, now that we have some connectivity, we need to be able to leverage it! Let's enable make use of SSH. "But wait!", you say, "The Ubuntu system is behind a NAT!" And yes, you are correct. But why should that stop us?

You have a few options here. You could cobble together some sort of SSH port forwarding, or set up port forwards on the freeBSD firewall. But that's...work. And we are professionally lazy, right? So let's do this the easy way (don't worry, you get to do other things the hard way later). SSH supports what are sometimes called bastion hosts or jump hosts. Basically, you will use the freeBSD system as a transparent stepping stone to get to the Ubuntu SSH server. This is a very common configuration in the real world, so it's good to get used to it now.

Now, on your host system, you need to configure your SSH client to make use of the bastion server that is your freeBSD VM. You can do this by adding the something like the following to your `~/.ssh/config` file:

```sh
Host ubuntu
    Hostname 192.168.33.133
    ProxyJump sq3.cs.pdx.edu
```

Your IP address may differ, and obviously replace the `sq3` address with your actual server. The key ingredient is the use of the `ProxyJump` directive. This tells SSH to use the specified host as the bastion/jump host. Completely transparently after the initial connection.

As long as you have your SSH keys configured on all 3 systems (host and 2 guests), connecting to your Ubuntu VM is as simple as typing `ssh ubuntu`. Or, you know, whatever you chose to name your systems.

And really, this is how we want to do it right now. We'll get to port forwarding, but it's a major topic of conversation that we'll cover in detail later. For now, just use the bastion host.

## System configuration

First, let's make sure it's up to date:

```sh
$ sudo apt update
$ sudo apt upgrade -y
```

You may have seen these commands before, but if you haven't, here is what's happening. `apt update` pulls down new package index files for any and all repositories that you have defined. If you haven't added any yet, it will just update the default set. `apt upgrade` will then upgrade any packages that have updates available. The `-y` flag tells it to apply the upgrades without awaiting confirmation. This is useful for scripting, but not so much for interactive use. If you want to see what it's going to do before it does it, just leave off the `-y`.

### Expand the filesystem (if necessary)

For reasons that escape me (yes, yes, I know it's "for snapshots" but really?), when you accept the default disk configuration in the Ubuntu installer (which uses LVM), it doesn't use all the physical disk space for the root logical volume. To fix this, run:

```sh
$ sudo lvextend --extents +100%FREE /dev/ubuntu-vg/ubuntu-lv --resizefs
```

This will extend the root logical volume to use the entire physical volume space available to it. The `-r` flag tells it to resize the file system as well. If you get an error about the volume not existing, run `sudo lvscan` and use the volume labeled `ACTIVE`.

### Install useful tools

OK, so we're likely still sitting on a barebones Ubuntu Server installation. We should fix that. Let's start with some useful tools:

```sh
$ sudo apt install podman docker.io zsh tmux ruby-dev fonts-inconsolata autojump bat emacs build-essential cowsay figlet filters fortunes dos2unix containerd python3-pip cargo cmake
```

We will install more as we go, but this is a good start.
