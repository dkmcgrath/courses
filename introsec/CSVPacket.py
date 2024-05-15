import csv

pktLENGTH=0
pktPROTO=1
pktIPSRC=2
pktIPDST=3
pktTCPFLAGS=4
pktTCPSPORT=5
pktTCPDPORT=6
pktUDPSPORT=7
pktUDPDPORT=8
pktICMPCODE=9
pktICMPTYPE=10

class Packet:

    def __init__(self,pkt,pn):
        self.length = self.proto = self.ipsrc = self.ipdst = None
        self.tcpsport = self.tcpdport = self.tcpflags = None
        self.udpsport = self.udpdport = None
        self.icmptype = self.icmpcode = None
        self.packetNum = pn
        try:
            self.length = int(pkt[pktLENGTH])
            self.proto = int(pkt[pktPROTO])
            self.ipsrc = pkt[pktIPSRC]
            self.ipdst = pkt[pktIPDST]
            self.tcpsport = self.tcpdport = self.tcpflags = None
            self.udpsport = self.udpdport = None
            self.icmptype = self.icmpcode = None
            if self.proto == 1:
                if len(pkt[pktICMPTYPE]) == 0 or len(pkt[pktICMPCODE]) == 0:
                    self.icmptype = self.icmpcode = -1
                else:
                    self.icmptype = int(pkt[pktICMPTYPE])
                    self.icmpcode = int(pkt[pktICMPCODE])
            elif self.proto == 6:
                if len(pkt[pktTCPSPORT]) == 0 or len(pkt[pktTCPDPORT]) == 0 or len(pkt[pktTCPFLAGS]) == 0:
                    self.tcpsport = self.tcpdport = self.tcpflags = 0
                else:
                    self.tcpsport = int(pkt[pktTCPSPORT])
                    self.tcpdport = int(pkt[pktTCPDPORT])
                    self.tcpflags = int(pkt[pktTCPFLAGS],16)
            elif self.proto == 17:
                if len(pkt[pktUDPSPORT]) == 0 or len(pkt[pktUDPDPORT]) == 0:
                    self.udpsport = self.udpdport = 0
                else:
                    self.udpsport = int(pkt[pktUDPSPORT])
                    self.udpdport = int(pkt[pktUDPDPORT])
        except ValueError:
            #print 'ValueError at packet ',pn,': ',(','.join(pkt))
            self.length = -1

    def __str__(self):
        r = ['Num:%4u length:%5u ' % (self.packetNum, self.length)]
        if self.proto == 1:
            r.append("ICMP type:%3u code:%3u" % (self.icmptype,self.icmpcode))
        elif self.proto == 6:
            r.append('TCP: %s:%-5u => %s:%-5u flags:%3u' % (self.ipsrc,self.tcpsport,self.ipdst,self.tcpdport,self.tcpflags))
        elif self.proto == 17:
            r.append('UDP: %s:%-5u => %s:%-5u' % (self.ipsrc,self.udpsport,self.ipdst,self.udpdport))
        else:
            r.append('Proto:%u %s => %s' % (self.proto,self.ipsrc,self.ipdst))
        return ''.join(r)

def CSVPackets(fh):
    packetNum = 1
    csvreader = csv.reader(fh)

    for p in csvreader:
        pkt = Packet(p, packetNum)
        if pkt.length <= 0:
            continue
        packetNum += 1
        yield pkt


#csvfile = open('O-fixed.csv','r')
#i = 0
#for pkt in CSVPackets(csvfile):
#    i = i + 1
#    if i == 100:
#        break
#    print "Packet %4u len %5u " % (pkt.packetNum, pkt.length),
#    if pkt.proto == 1:
#        print "ICMP type:",pkt.icmptype,' code:',pkt.icmpcode
#    elif pkt.proto == 6:
#        print 'TCP: %s:%u => %s:%u flags:%u' % (pkt.ipsrc,pkt.tcpsport,pkt.ipdst,pkt.tcpdport,pkt.tcpflags)
#    elif pkt.proto == 17:
#        print 'UDP: %s:%u => %s:%u' % (pkt.ipsrc,pkt.udpsport,pkt.ipdst,pkt.udpdport)
#    else:
#        print 'Proto:%u %s => %s' % (pkt.proto,pkt.ipsrc,pkt.ipdst)
#
