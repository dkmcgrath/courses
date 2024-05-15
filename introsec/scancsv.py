from CSVPacket import Packet, CSVPackets
import sys

IPProtos = [0 for x in range(256)]
numBytes = 0
numPackets = 0

csvfile = open(sys.argv[1],'r')

for pkt in CSVPackets(csvfile):
    # pkt.__str__ is defined...
    #print pkt
    numBytes += pkt.length
    numPackets += 1
    proto = pkt.proto & 0xff
    IPProtos[proto] += 1


print "numPackets:%u numBytes:%u" % (numPackets,numBytes)
for i in range(256):
    if IPProtos[i] != 0:
        print "%3u: %9u" % (i, IPProtos[i])

