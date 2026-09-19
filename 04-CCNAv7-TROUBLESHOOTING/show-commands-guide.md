### `show-commands-guide.md`

```markdown
# Cisco Show Commands Guide

A quick reference for Cisco IOS/IOS-XE verification and troubleshooting.

## General

```cisco
show running-config
show startup-config
show version
show inventory
show clock
show users
Interfaces
show ip interface brief
show interfaces
show interfaces description
show interfaces status
VLANs
show vlan brief
show interfaces switchport
Trunks
show interfaces trunk
MAC Address Table
show mac address-table
show mac address-table dynamic
show mac address-table address <mac-address>
show mac address-table interface <interface>
show mac address-table vlan <vlan-id>
STP
show spanning-tree
show spanning-tree root
show spanning-tree vlan <vlan-id>
EtherChannel
show etherchannel summary
show etherchannel detail
show interfaces port-channel
Routing
show ip route
show ip route <destination>
show ip protocols
ARP
show arp
CDP
show cdp neighbors
show cdp neighbors detail
LLDP
show lldp neighbors
show lldp neighbors detail
DHCP
show ip dhcp pool
show ip dhcp binding
show ip dhcp conflict
NAT
show ip nat translations
show ip nat statistics
Port Security
show port-security
show port-security interface <interface>
show port-security address
SSH
show ip ssh
show users
OSPF
show ip ospf
show ip ospf neighbor
show ip ospf interface
show ip ospf database
Debugging

Use debugging carefully.

debug ip icmp
debug ip ospf events
debug ip ospf adj

Disable debugging afterward:

undebug all

Troubleshooting Rule

Start with show commands.

Use debug only when normal verification does not provide enough information.