# CCNA COMMANDS CHEATSHEET

## General
- show ip interface brief
- show running-config
- show version

---

## Switch
- show mac address-table
- show vlan brief

---

## Router
- show ip route
- show ip protocols

---

## Troubleshooting
- ping
- traceroute

---

## Changing Switch Hostname
- Switch(config)#hostname SW1

## Configuring Passwords
- SW1(config)#enable secret cisco | MD5 hash. |
- SW1(config)#enable password notcisco | Clear text. |

## Securing Console Port
- SW1(config)#line con 0
- SW1(config-line)#password cisco
- SW1(config-line)#login

## Securing Terminal Lines
- SW1(config)#line vty 0 4
- SW1(config-line)#password cisco
- SW1(config-line)#login

## Encrypting Password
- SW1(config)#service password-encryption

## Configuring Banners
- SW1(config)#banner motd $ UNAUTHORIZED ACCESS IS PROHIBITED $

## Giving the switch an IP Address
- SW1(config)#interface vlan 1
- SW1(config-if)#ip address 172.16.1.11 255.255.255.0 (or dhcp)
- SW1(config-if)#shutdown

## Setting the default gateway
- SW1(config)#ip default-gateway 172.16.1.1

## Saving Configuration
- SW1#copy running-config startup-config | Press enter to confirm file name.
- Destination filename [startup-config]?
- Building configuration_
- [OK]
- //
- SW1#wr | Short for write memory
- Building configuration_
- [OK]