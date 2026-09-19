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

```

## Interfaces

```cisco
show ip interface brief
show interfaces
show interfaces description
show interfaces status

```

## VLANs

```cisco
show vlan brief
show interfaces switchport

```

## Trunks

```cisco
show interfaces trunk

```

## MAC Address Table

```cisco
show mac address-table
show mac address-table dynamic
show mac address-table address <mac-address>
show mac address-table interface <interface>
show mac address-table vlan <vlan-id>

```

## STP

```cisco
show spanning-tree
show spanning-tree root
show spanning-tree vlan <vlan-id>

```

## EtherChannel

```cisco
show etherchannel summary
show etherchannel detail
show interfaces port-channel

```

## Routing

```cisco
show ip route
show ip route <destination>
show ip protocols

```

## ARP

```cisco
show arp

```

## CDP

```cisco
show cdp neighbors
show cdp neighbors detail

```

## LLDP

```cisco
show lldp neighbors
show lldp neighbors detail

```

## DHCP

```cisco
show ip dhcp pool
show ip dhcp binding
show ip dhcp conflict

```

## NAT

```cisco
show ip nat translations
show ip nat statistics

```

## Port Security

```cisco
show port-security
show port-security interface <interface>
show port-security address

```

## SSH

```cisco
show ip ssh
show users

```

## OSPF

```cisco
show ip ospf
show ip ospf neighbor
show ip ospf interface
show ip ospf database

```

## Debugging

Use debugging carefully.

```cisco
debug ip icmp
debug ip ospf events
debug ip ospf adj

```

Disable debugging afterward:

```cisco
undebug all

```

---

## Troubleshooting Rule

Start with show commands.

Use debug only when normal verification does not provide enough information.

```

```