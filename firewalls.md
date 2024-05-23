# Defensive Measures

* auto-gen TOC:
{:toc}

## Firewalls
Firewalls are a classic defensive measure. Designed as a tool to limit inbound or outbound connections, firewalls are traditionally rule based. We will primarily be discussing the Linux iptables instantiation of a firewall, mainly due to the ease of access -- it's on the Kali VM we have been using all term.

At the end of the day, firewalls are nothing but sets of rules. These rules govern which packets are kept, and which packets get dropped like a bad habit. One of the most important things to keep in mind is that order matters!

### Firewall rules
As mentioned above, firewalls are simply a set of rules. If you'd like to see the current rule-set, execute the below

```zsh
┌─(ROOT@kali478-0:pts/4)───────────────────────────────────────────────────────────────────(~/cs478)─┐
└─(2:12:43:#)── iptables --list                                                        ──(Fri,Feb14)─┘
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
```

As you can see, within Kali, the defaults are empty. If you want to know what else iptables can do, take a look at the help:

```zsh
┌─(ROOT@kali478-0:pts/4)───────────────────────────────────────────────────────────────────(~/cs478)─┐
└─(2:12:43:#)── iptables --help                                                        ──(Fri,Feb14)─┘
iptables v1.8.3

Usage: iptables -[ACD] chain rule-specification [options]
	iptables -I chain [rulenum] rule-specification [options]
	iptables -R chain rulenum rule-specification [options]
	iptables -D chain rulenum [options]
	iptables -[LS] [chain [rulenum]] [options]
	iptables -[FZ] [chain] [options]
	iptables -[NX] chain
	iptables -E old-chain-name new-chain-name
	iptables -P chain target [options]
	iptables -h (print this help information)

Commands:
Either long or short options are allowed.
  --append  -A chain		Append to chain
  --check   -C chain		Check for the existence of a rule
  --delete  -D chain		Delete matching rule from chain
  --delete  -D chain rulenum
				Delete rule rulenum (1 = first) from chain
  --insert  -I chain [rulenum]
				Insert in chain as rulenum (default 1=first)
  --replace -R chain rulenum
				Replace rule rulenum (1 = first) in chain
  --list    -L [chain [rulenum]]
				List the rules in a chain or all chains
  --list-rules -S [chain [rulenum]]
				Print the rules in a chain or all chains
  --flush   -F [chain]		Delete all rules in  chain or all chains
  --zero    -Z [chain [rulenum]]
				Zero counters in chain or all chains
  --new     -N chain		Create a new user-defined chain
  --delete-chain
	     -X [chain]		Delete a user-defined chain
  --policy  -P chain target
				Change policy on chain to target
  --rename-chain
	     -E old-chain new-chain
				Change chain name, (moving any references)
Options:
    --ipv4	-4		Nothing (line is ignored by ip6tables-restore)
    --ipv6	-6		Error (line is ignored by iptables-restore)
[!] --proto	-p proto	protocol: by number or name, eg. `tcp'
[!] --source	-s address[/mask][...]
				source specification
[!] --destination -d address[/mask][...]
				destination specification
[!] --in-interface -i input name[+]
				network interface name ([+] for wildcard)
 --jump	-j target
				target for rule (may load target extension)
  --goto      -g chain
			       jump to chain with no return
  --match	-m match
				extended match (may load extension)
  --numeric	-n		numeric output of addresses and ports
[!] --out-interface -o output name[+]
				network interface name ([+] for wildcard)
  --table	-t table	table to manipulate (default: `filter')
  --verbose	-v		verbose mode
  --wait	-w [seconds]	maximum wait to acquire xtables lock before give up
  --wait-interval -W [usecs]	wait time to try to acquire xtables lock
				default is 1 second
  --line-numbers		print line numbers when listing
  --exact	-x		expand numbers (display exact values)
[!] --fragment	-f		match second or further fragments only
  --modprobe=<command>		try to insert modules using this command
  --set-counters PKTS BYTES	set the counter during insert/append
[!] --version	-V		print package version.
```
So let's add some rules:

```zsh
❯ iptables -A OUTPUT -p tcp -d ubuntu.com -j ACCEPT
❯ iptables -A OUTPUT -p tcp -d ca.archive.ubuntu.com -j ACCEPT
❯ iptables -A OUTPUT -p tcp --dport 80 -j DROP
❯ iptables -A OUTPUT -p tcp --dport 443 -j DROP
❯ iptables -A INPUT -p tcp -s 172.16.0.45 --dport 22 -j ACCEPT
❯ iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport 22 -j DROP
```

What do these rules do? Let's break them down:

1. Allow all traffic to `ubuntu.com`
1. Allow all traffic to `ca.archive.ubuntu.com`
1. Drop all traffic destined for port 80
1. Drop all traffic destined for port 443
1. Allow traffic from `172.16.0.45` to port 22
1. Drop all traffic from any other source to port 22

So we can SSH in, we can update the system, but we can't browse the web. This is a very basic example of how iptables can be used to control traffic.

### Rule processing

Rules are processed in numerical order, from first to last. Processing stops as soon as a rule is matched -- ORDER MATTERS! There are ways to move rules around in the ipchains, but it's better to just enter them in the correct order.

## Intrusion Detection/Prevention Systems

Suricata is an open source (with commercial support) network based intrusion detection/prevention system (NIDS/NIPS). Much like the Snort tool, it is a production grade NIPS that has significant community support. For our purposes, Suricata is the example used due to its support of rule expansions via the Lua scripting language. Snortv3 also now supports Lua scripts in rules, but is not well documented (to my knowledge).

## Suricata rules

From the Suricata manual:

    A rule/signature consists of the following:

    * The action, that determines what happens when the signature matches
    * The header, defining the protocol, IP addresses, ports and direction of the rule.
    * The rule options, defining the specifics of the rule.

```lua
#action protocol IPs ports -> IPs ports (trigger conditions)

drop tcp 10.0.0.0/8 any -> $HOME_NET any (msg:"dropping all traffic from non-routable IPs"; sid:20201234; rev:2;)
```

The above has both the general format, as well as an example rule. `sid` is required, while `rev` is recommended.

### Built-in rules

Suricata comes with a significant batch of pre-built rules for a lot of the common network packets you might want to filter out. These include unwanted pings, network scan requests, ICMP traffic at all, filtering for known exploit traffic, etc. Further, there are some packet "classes" you can use in rules that encapsulate fairly complex rule logic.

### Custom rules

Sometimes though, the built in rules just won't cut it. Maybe there's a new exploit in the wild. Maybe you want to alert on specific actions from smb. Maybe you just want to explore. There are several ways to add custom rules:

* You can build them with the packet classes mentioned above
* You can filter on specific content
* You can filter on basic packet structure
* You can filter on either header or body of the packet, including re-assembled or not fragmented traffic
* You can write a Lua script to work on the packet to analyze it in a more in-depth fashion.

The above list is not exhaustive, and I want us to focus primarily on the final point. Lua gives us the ability to perform complex logic on our packet structure or the content of the packet. It allows for things like detecting a mismatch between reported and actual length (remember that, it'll be useful soon). The below verifies that reported length is the same as actual length.

```lua=
function init (args)
    local needs = {}
    needs["payload"] = tostring(true)
    return needs
end

function string.tohex(str)
    return (str:gsub('.', function (c)
        return string.format('%02X ', string.byte(c))
    end))  
end

function match(args)
    local b = args['payload']
    if b == nil then
        print ("Payload buffer empty! Aborting...")
        return 0
    end
    print (string.tohex(b))
    -- DNS RFC specifies length is reported in the first two bytes.
    dns_size_high_byte = b:byte(1)
    dns_size_low_byte = b:byte(2)
    dns_size = tonumber(dns_size_high_byte) * 256 + tonumber(dns_size_low_byte)
    -- check to ensure reported lenghth is same as actual length.  Subtract 2 for length field
    if dns_size ~= string.len(b)-2 then
            return 1
    end
    return 0
end
```

Lines 1-5 are required, while lines 7-11 are useful for debugging purposes. On a failed test, return 1 to trigger the rule. On a passing test, return 0 to skip this rule. Pay attention to lines 21-23 -- this is how you pull out bytes and combine into a 16-bit int.

### Optional Additional Resources

If this topic interests you, then you might find the following optional resources useful.

* [Suricata manual](https://suricata.readthedocs.io/en/suricata-6.0.0/)
* [Lua reference manual](https://www.lua.org/manual/5.4/)
* [Suricata home page](https://suricata-ids.org/)
* [Snort home page](https://www.snort.org/)