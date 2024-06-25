```sh
#!/bin/sh
#
# To download this script directly from freeBSD:
# $ pkg install curl
# $ curl -LO https://raw.githubusercontent.com/dkmcgrath/sysadmin/main/freebsd_setup.sh
#
#The following features are added:
# - switching (internal to the network) via FreeBSD pf
# - DHCP server, DNS server via dnsmasq
# - firewall via FreeBSD pf
# - NAT layer via FreeBSD pf
#

# Set your network interfaces names; set these as they appear in ifconfig
# they will not be renamed during the course of installation
WAN="em0"
LAN="em1"

# Install dnsmasq
pkg install -y dnsmasq

# Enable forwarding
sysrc gateway_enable="YES"
# Enable immediately
sysctl net.inet.ip.forwarding=1

# Set LAN IP
ifconfig ${LAN} inet 192.168.33.1 netmask 255.255.255.0
# Make IP setting persistent
sysrc "ifconfig_${LAN}=inet 192.168.33.1 netmask 255.255.255.0"

ifconfig ${LAN} up
ifconfig ${LAN} promisc

# Enable dnsmasq on boot
sysrc dnsmasq_enable="YES"

# Edit dnsmasq configuration
echo "interface=${LAN}" >> /usr/local/etc/dnsmasq.conf
echo "dhcp-range=192.168.33.50,192.168.33.150,12h" >> /usr/local/etc/dnsmasq.conf
echo "dhcp-option=option:router,192.168.33.1" >> /usr/local/etc/dnsmasq.conf

# Configure PF for NAT
echo "
ext_if=\"${WAN}\"
int_if=\"${LAN}\"

icmp_types = \"{ echoreq, unreach }\"
services = \"{ ssh, domain, http, ntp, https }\"
server = \"192.168.33.63\"
ssh_rdr = \"2222\"
table <rfc6890> { 0.0.0.0/8 10.0.0.0/8 100.64.0.0/10 127.0.0.0/8 169.254.0.0/16          \\
                  172.16.0.0/12 192.0.0.0/24 192.0.0.0/29 192.0.2.0/24 192.88.99.0/24    \\
                  192.168.0.0/16 198.18.0.0/15 198.51.100.0/24 203.0.113.0/24            \\
                  240.0.0.0/4 255.255.255.255/32 }
table <bruteforce> persist


#options                                                                                                                         
set skip on lo0

#normalization
scrub in all fragment reassemble max-mss 1440

#NAT rules
nat on \$ext_if from \$int_if:network to any -> (\$ext_if)

#blocking rules
antispoof quick for \$ext_if
block in quick on egress from <rfc6890>
block return out quick on egress to <rfc6890>
block log all

#pass rules
pass in quick on \$int_if inet proto udp from any port = bootpc to 255.255.255.255 port = bootps keep state label \"allow access to DHCP server\"
pass in quick on \$int_if inet proto udp from any port = bootpc to \$int_if:network port = bootps keep state label \"allow access to DHCP server\"
pass out quick on \$int_if inet proto udp from \$int_if:0 port = bootps to any port = bootpc keep state label \"allow access to DHCP server\"

pass in quick on \$ext_if inet proto udp from any port = bootps to \$ext_if:0 port = bootpc keep state label \"allow access to DHCP client\"
pass out quick on \$ext_if inet proto udp from \$ext_if:0 port = bootpc to any port = bootps keep state label \"allow access to DHCP client\"

pass in on \$ext_if proto tcp to port { ssh } keep state (max-src-conn 15, max-src-conn-rate 3/1, overload <bruteforce> flush global)
pass out on \$ext_if proto { tcp, udp } to port \$services
pass out on \$ext_if inet proto icmp icmp-type \$icmp_types
pass in on \$int_if from \$int_if:network to any
" >> /etc/pf.conf

# Start dnsmasq
service dnsmasq start

# Enable PF on boot
sysrc pf_enable="YES"
sysrc pflog_enable="YES"

# Start PF
service pf start

# Load PF rules
pfctl -f /etc/pf.conf
```
