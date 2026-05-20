# VLAN Cheatsheet

## VLAN Concepts
- Logical segmentation of switches
- Separates broadcast domains

## Port Types
Access Port → single VLAN
Trunk Port → multiple VLANs

## VLAN Commands
vlan 10
name SALES

switchport mode access
switchport access vlan 10

switchport mode trunk
switchport trunk allowed vlan 10,20

## Verification
show vlan brief
show interfaces trunk

## Router-on-a-Stick
- Router subinterfaces
- 802.1Q tagging