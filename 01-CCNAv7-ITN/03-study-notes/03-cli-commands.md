# Cisco IOS CLI Commands

## Navigation
enable
configure terminal
exit
end

## Interface Config
interface g0/0
ip address 192.168.1.1 255.255.255.0
no shutdown

## Verification
show ip interface brief
show running-config
show interfaces
show ip route

## Switching
show mac address-table
show vlan brief

## Connectivity
ping 8.8.8.8
traceroute 8.8.8.8

## SSH Setup
hostname R1
ip domain-name cisco.local
crypto key generate rsa
username admin secret cisco123
line vty 0 4
login local
transport input ssh

## Save Config
copy running-config startup-config