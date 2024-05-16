#Final Project CS596

Due Date: Friday of Finals Week 23:59:59

* auto-gen TOC:
{:toc}

## Introduction

So you have suricata installed. Now what? In mid-2020, JSOF released a series of vulnerabilities dubbed [Ripple20](https://www.jsof-tech.com/ripple20/). In late 2020, MS released a CVE dubbed Bad Neighbor, which is basically the Ping of Death but for IPv6. Fixing these vulnerabilities is difficult given the install base, variants of Treck used, and mission-criticality of some of the devices in question. In other words, this becomes a network filtering problem. Enter suricata!

## What you must do

Pick one of the following CVEs: CVE-2020-11901 (Variant 1), CVE-2020-11901 (Variant 2), CVE-2020-11897, CVE-2020-11896, or CVE-2020-16898.

1. Write a high level description of the vulnerability.
1. Write a suricata rule to detect it. Most of these will actually require a script written in Lua to be part of the rule.
1. Write up a document detailing your rule, your script, and why you believe that it will work.

OK, so it's worth pointing out here that I helped write the commonly used rules for 4 of these 5 vulnerabilities, and logic checked the 5th -- in other words, they are out there, publicly available. Try to do this on your own, but feel free to get a hint here or there as you need it. Just remember, you need to be able to explain it in your write-up!

## Resources

[Suricata rules description](https://suricata.readthedocs.io/en/suricata-5.0.3/rules/index.html).
[Suricata Lua support](https://suricata.readthedocs.io/en/suricata-5.0.3/lua/index.html).


## What to turn in

You will be submitting this via your gitlab repo, in a markdown file called `final/final.md`. This should contain the high level description of the vulnerability, the suricata rule, and the Lua script. You should also include a pcap file that demonstrates the rule in action. This pcap file should be named `final.pcap` and should be in the `final` directory of your repo.