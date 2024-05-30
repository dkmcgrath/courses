# Write Out-of-Bounds Using Routing Header Type 0
---

**CVE**: CVE-2020-11897<br>
**CVSS**: 10<br>
**Protocol(s)**: IPv6<br>
**Port(s)**: N/A

## Vulnerability description:

When processing IPv6 incoming packets, an inconsistency parsing the IPv6 routing header can be triggered where the header length is checked against the total packet and not against the fragment length. This means that if we send fragmented packets with the overall size greater than or equal to the specified routing header length, then we process the routing header under the assumption that we have enough bytes in our current fragment (where we have enough bytes in the overall reassembled packet only). Thus, using routing header type 0 (RH0) we can force read and write into out-of-bounds memory location.

There is also a secondary side effect where we can get an info leak in a source IPv6 address in an ICMP parameter returned from the device.

## Limitations or special considerations for detection:

The RFC for RH0 defines the length field as equal to "two times the number of addresses in the header." For example, if the routing header length is six, then there are three IPv6 addresses expected in the header. Upon reconstruction of the fragmented packets, the reported number of addresses is filled with data from the fragments that follow. This creates "invalid" IPv6 addresses in the header and potentially malforms the next layer of the packet. During exploitation, it would also be likely for the next layer of the packet to be malformed. Although ICMP can be used to perform an information leak, it is possible for the next layer to be any type and therefore vary in length. Verification of the length of this layer could therefore be very expensive and non-deterministic.

## Recommended detection criteria:

* The device must be capable of processing fragmented IPv6 traffic
* The device should inspect fragmented packets containing Routing Header type 0 (RH0). If a RH0 IPv6 packet is fragmented, then the vulnerability is likely being exploited
* If the length of the IPv6 layer of a packet fragment containing the RH0 header is less than the length reported in the routing header, then the vulnerability is likely being exploited
* Upon reconstruction of the fragmented packets, if the header of the layer following IPv6 is malformed, the vulnerability may be being exploited

## Notes:

The routing header type 0 was deprecated in IPv6 traffic in RFC 5095 as of December 2007. As a result, it may be feasible simply to detect packets using this criterion. False positives may be possible in this scenario for legacy devices or platforms. Suricata already provides a default rule for this scenario which has been added below. According to the RFC, routers are not supposed to fragment IPv6 packets and must support an MTU of 1280, which would always contain all of the RH0 header, unless an unusual amount of header extensions or an unusually large header is used. If this is followed, then a packet using the RH0 header should never be fragmented across the RH0 extension header bounds and any RH0 packet fragmented in this manner should be treated as potentially malicious. Treating any fragmented RH0 packet as potentially malicious may be sufficient. Furthermore, treating any fragmented RH0 packet with fragments size below a threshold as well as IPv6 packets with multiple extension headers or an unusually large header above a threshold may provide high accuracy detection.

## False positive conditions (signatures detecting non-malicious traffic):

If all detection criteria outlined above are used, false positives should be minimal since the reported length of a packet should match its actual length and the next header should never contain malformed data. If only routing header type 0 is checked, false positives are more likely to occur. In the additional provided rule, false positives should be minimal since RH0 is deprecated and the ICMP header should never have invalid checksums or unknown codes.

## False negative conditions (signatures failing to detect vulnerability/exploitation):

False negatives may occur if the signature is developed overly specific to the layer following IPv6, for example, ICMP. An attacker could potentially leverage another layer and still exploit the vulnerability without the information leak; however, this would still trigger the default RH0 rule. In the second rule below, false negatives are likely to occur if:

* An attacker uses a non-ICMP layer following the IPv6 layer
* A valid ICMP code is used
* The checksum is valid, and the payload is less than or equal to 5 bytes (this value can be tuned in the signature)