# OSPF Cheatsheet

## Process
Dynamic routing protocol

## Neighbor States
Down → Init → 2-Way → ExStart → Exchange → Full

## DR/BDR
- Election based on priority + router ID

## Config
router ospf 1
network 192.168.1.0 0.0.0.255 area 0

## Verify
show ip ospf neighbor
show ip route ospf