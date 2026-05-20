# CCNA COMMANDS CHEATSHEET

## General
- show ip interface brief
- show running-config
- show version

## Switch
- show mac address-table
- show vlan brief

## Router
- show ip route
- show ip protocols

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

## Working Environment (name lookup, history, exec-timeout and logging behaviour)
- SW1(config)#no ip domain-lookup
- SW1(config)#line vty 0 4
- SW1(config-line)#history size 15
- SW1(config-line)#exec-timemout 10 30
- SW1(config-line)#logging synchronous

## Configuring switch to use SSH
- Configure DNS domain name: | The size of the key modulus in range of 360 to 2048
- SW1(config)#ip domain-name example.com



```markdown
# Cisco CCNA Commands Cheatsheet

## Switch Basic Configuration

### Changing switch hostname
```ios
Switch(config)# hostname SW1

```

### Configuring passwords

```ios
SW1(config)# enable secret cisco          ; MD5 hash
SW1(config)# enable password notcisco    ; Clear text

```

### Securing console port

```ios
SW1(config)# line con 0
SW1(config-line)# password cisco
SW1(config-line)# login

```

### Securing terminal lines

```ios
SW1(config)# line vty 0 4
SW1(config-line)# password cisco
SW1(config-line)# login

```

### Encrypting passwords

```ios
SW1(config)# service password-encryption

```

### Configuring banners

```ios
SW1(config)# banner motd $
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
UNAUTHORIZED ACCESS IS PROHIBITED
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
$

```

### Giving the switch an IP address

```ios
SW1(config)# interface vlan 1
SW1(config-if)# ip address 172.16.1.11 255.255.255.0  ; (or dhcp)
SW1(config-if)# no shutdown

```

### Setting the default gateway

```ios
SW1(config)# ip default-gateway 172.16.1.1

```

### Saving Configuration

```ios
SW1# copy running-config startup-config  ; Press enter to confirm file name
SW1# wr                                  ; Short for write memory

```

---

## Working Environment & SSH

### Working environment management

*(Name lookup, history, exec-timeout and logging behavior)*

```ios
SW1(config)# no ip domain-lookup
SW1(config)# line vty 0 4                 ; Also valid for line con 0
SW1(config-line)# history size 15
SW1(config-line)# exec-timeout 10 30
SW1(config-line)# logging synchronous

```

### Configuring switch to use SSH

* **Configure DNS domain name:**
```ios
SW1(config)# ip domain-name example.com

```


* **Configure a username and password:**
```ios
SW1(config)# username admin password cisco

```


* **Generate encryption keys:**
```ios
SW1(config)# crypto key generate rsa
; How many bits in the modulus [512]: 1024 (Size range: 360 to 2048)

```


* **Define SSH version to use:**
```ios
SW1(config)# ip ssh version 2

```


* **Enable vty lines to use SSH:**
```ios
SW1(config)# line vty 0 4
SW1(config-line)# login local
SW1(config-line)# transport input telnet ssh  ; Allows telnet, ssh, or both

```



---

## Aliases & Interface Management

### Aliases (Shortcuts for long commands)

```ios
SW1(config)# alias exec c configure terminal
SW1(config)# alias exec s show ip interface brief
SW1(config)# alias exec sr show running-config

```

### Interface Configuration

```ios
SW1(config)# interface fastEthernet 0/1
SW1(config-if)# description LINK TO INTERNET ROUTER
SW1(config-if)# speed 100                             ; Options: 10, 100, auto
SW1(config)# interface range fastEthernet 0/5 - 10     ; Sets a group of interfaces at once
SW1(config-if-range)# duplex full                      ; Options: half, full, auto

```

---

## Verify Basic Configuration

| Command | Description |
| --- | --- |
| `SW1# show version` | Shows information about the switch and its interfaces, RAM, NVRAM, flash, IOS, etc. |
| `SW1# show running-config` | Shows the current configuration file stored in DRAM. |
| `SW1# show startup-config` | Shows the configuration file stored in NVRAM which is used at first boot process. |
| `SW1# show history` | Lists the commands currently held in the history buffer. |
| `SW1# show ip interface brief` | Shows an overview of all interfaces, their physical status, protocol status, and assigned IP addresses. |
| `SW1# show interface vlan 1` | Shows detailed information about the specified interface, its status, protocol, duplex, speed, encapsulation, and last 5 min traffic. |
| `SW1# show interfaces description` | Shows the description of all interfaces. |
| `SW1# show interfaces status` | Shows the status of all interfaces like connected or not, speed, duplex, trunk, or access vlan. |
| `SW1# show crypto key mypubkey rsa` | Shows the public encryption key used for SSH. |
| `SW1# show dhcp lease` | Shows information about the leased IP address (when an interface is configured via a DHCP server). |

---

## Port Security

### Configuring port Security

* **Make the switch interface an access port:**
```ios
SW1(config-if)# switchport mode access

```


* **Enable port security on the interface:**
```ios
SW1(config-if)# switchport port-security

```


* **Specify the maximum number of allowed MAC addresses:**
```ios
SW1(config-if)# switchport port-security maximum 1

```


* **Define the action to take when a violation occurs:**
```ios
SW1(config-if)# switchport port-security violation shutdown  ; Options: shutdown, protect, restrict

```


* **Specify the allowed MAC addresses:**
```ios
SW1(config-if)# switchport port-security mac-address 68b5.9965.1195  ; Options: H.H.H, sticky

```


*(Note: The sticky keyword lets the interface dynamically learn and configure the MAC addresses of connected hosts)*

### Verify and troubleshoot port security

```ios
SW1# show mac-address-table                ; Shows the entries of the mac address table
SW1# show port-security                   ; Overview of port security of all interfaces
SW1# show port-security interface fa0/5   ; Shows detailed info about port security on specified interface

```

---

## VLANs & Trunking

### Configuring VLANs

* **Create a new VLAN and give it a name:**
```ios
SW1(config)# vlan 10
SW1(config-vlan)# name SALES

```


* **Assign an access interface to a specific VLAN:**
```ios
SW1(config)# interface fastEthernet 0/5
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 10

```



### Configuring an auxiliary WLAN for Cisco IP phones

```ios
SW1(config)# interface fastEthernet 0/5
SW1(config-if)# switchport access vlan 10    ; Accessing vlan 10 (data)
SW1(config-if)# switchport voice vlan 12     ; Accessing vlan 12 (voip)

```

### Configuring Trunks

```ios
SW1(config)# interface fastEthernet 0/1
SW1(config-if)# switchport mode trunk                   ; Options: access, trunk, dynamic auto, dynamic desirable
SW1(config-if)# switchport trunk allowed vlan 10        ; Options: add, remove, all, except

```

### Securing VLANs and Trunking

* **Administratively disable unused interfaces:**
```ios
SW1(config-if)# shutdown

```


* **Prevent trunking by disabling auto-negotiation on the interface:**
```ios
SW1(config-if)# nonegotiate   ; Or hardcode the port as an access port
SW1(config-if)# switchport mode access

```


* **Assign the port to an unused VLAN:**
```ios
SW1(config-if)# switchport access vlan 22

```



### Configuring VTP

```ios
SW1(config)# vtp mode server                 ; Options: server, client, transparent
SW1(config)# vtp domain EXAMPLE              ; Case-sensitive
SW1(config)# vtp password cisco              ; Optional, case-sensitive
SW1(config)# vtp pruning                     ; Optional, only works on VTP servers
SW1(config)# vtp version 2                   ; Optional

```

*(Note: VTP mode transparent is used when an engineer wants to deactivate VTP on a particular switch)*

### Verify and troubleshoot VLANs and VTP

```ios
SW1# show interfaces if switchport           ; Lists info about administrative setting & operation status
SW1# show interfaces trunk                   ; Lists all Trunk ports and their allowed VLANs
SW1# show vlan {brief| id| name| summary}   ; Lists information about the VLAN
SW1# show vtp status                        ; Lists VTP configuration (mode, domain, version, revision)
SW1# show vtp password                      ; Shows the VTP password

```

---

## STP Optimization

### Hard coding the root bridge (changing bridge priority)

```ios
SW1(config)# spanning-tree vlan 1 root primary
SW1(config)# spanning-tree vlan 1 root secondary
SW1(config)# spanning-tree [vlan 1] priority 8129     ; Priority must be a multiple of 4096

```

### Changing the STP mode

```ios
SW1(config)# spanning-tree mode rapid-pvst             ; Options: mst, pvst, rapid-pvst

```

### Enabling PortFast and BPDU Guard on an interface

```ios
SW1(config-if)# spanning-tree portfast                 ; Portfast/BPDU Guard are enabled only on interfaces
SW1(config-if)# spanning-tree bpduguard enable         ; connected to end-user hosts

```

### Changing port cost

```ios
SW1(config-if)# spanning-tree [vlan 1] cost 25

```

### Bundling interfaces into an EtherChannel

```ios
SW1(config-if)# channel-group 1 mode on                ; Options: auto, desirable, on

```

### STP verification and troubleshooting

```ios
SW1# show spanning-tree                                ; Detailed info about STP state
SW1# show spanning-tree interface fa0/2                ; STP Info only on a specific port
SW1# show spanning-tree vlan 1                         ; STP info only for a specific VLAN
SW1# show spanning-tree [vlan1] root                   ; Info about the root switch
SW1# show spanning-tree [vlan1] bridge                 ; Info about the local switch
SW1# show etherchannel 1                               ; Show the state of the etherchannels
SW1# debug spanning-tree events                        ; Informational messages about topology changes

```

---

## Discovery Protocols (CDP)

### Enabling or disabling CDP

```ios
SW1(config)# cdp run                                   ; Enabling CDP globally on a switch
SW1(config-if)# no cdp enable                          ; Disabling CDP on a given interface

```

### Using CDP for network verification and troubleshooting

```ios
SW1# show cdp                                          ; Shows global information about CDP itself
SW1# show cdp interface fa0/2                          ; Shows information about CDP on a specific interface
SW1# show cdp neighbors                                ; Shows directly connected cisco devices and capabilities
SW1# show cdp neighbors detail                         ; Shows detailed info including device address and IOS version
SW1# show cdp entry * ; Same as show cdp neighbor detail
SW1# show cdp entry sw2                                ; Shows detailed information about specified entry only

```

---

## Router Configuration

### Router Basic Configuration

```ios
Router(config)# hostname R1
R1(config)# enable secret cisco
R1(config)# line con 0
R1(config-line)# password cisco
R1(config-line)# login
R1(config-line)# logging synchronous
R1(config-line)# exec-timeout 30 0
R1(config-line)# exit

R1(config)# line vty 0 4
R1(config-line)# password cisco
R1(config-line)# login
R1(config-line)# logging synchronous
R1(config-line)# exec-timeout 30 0
R1(config-line)# exit

R1(config)# line aux 0
R1(config-line)# password cisco
R1(config-line)# login
R1(config-line)# logging synchronous
R1(config-line)# exec-timeout 30 0
R1(config-line)# exit

R1(config)# banner motd $
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
UNAUTHORIZED ACCESS IS PROHIBITED
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
$
R1(config)# alias exec c configure terminal
R1(config)# alias exec s show ip interface brief
R1(config)# alias exec sr show running-config
R1(config)# no ip domain-lookup

```

*(Note: These commands are identical to switches, except routers include `line aux 0` as switches do not have an auxiliary port).*

### Configuring Router Interfaces

```ios
R1(config)# interface fastEthernet 0/0
R1(config-if)# description LINK_TO_LOCAL_LAN_THROUGH_SW1
R1(config-if)# ip add 172.16.1.1 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# exit

R1(config)# interface serial 0/1/0
R1(config-if)# description WAN_CONNECTION_TO_R2
R1(config-if)# ip address 10.1.1.1 255.255.255.252
R1(config-if)# clock rate 128000                     ; Clock rate is set only on the DCE side
R1(config-if)# no shutdown                             ; On DTE you don't need to configure clocking

```

### Configuring Router-on-Stick for VLAN routing

```ios
R1(config)# interface fastEthernet 0/0
R1(config-if)# no shutdown

R1(config-if)# interface fastEthernet 0/0.10
R1(config-subif)# encapsulation dot1q 10
R1(config-subif)# ip add 192.168.10.1 255.255.255.0

R1(config-subif)# interface fastEthernet 0/0.20
R1(config-subif)# encapsulation dot1q 20
R1(config-subif)# ip address 192.168.20.1 255.255.255.0

```

---

## Static & Dynamic Routing

### Static & Default Routes

```ios
R1(config)# ip route 10.1.2.0 255.255.255.0 10.1.128.1  ; Using next hop
R1(config)# ip route 10.1.2.0 255.255.255.0 serial 0/0  ; Using exit interface
R1(config)# ip route 0.0.0.0 0.0.0.0 199.1.1.1         ; Default Route

```

### RIPv2 Configuration

```ios
R1(config)# router rip
R1(config-router)# version 2
R1(config-router)# network 10.0.0.0                    ; Written as an original classful A network
R1(config-router)# no autosummary
R1(config-router)# passive-interface serial 0/0

```

### RIPv2 Verification

```ios
R1# show ip protocols                                  ; Info about running routing process
R1# show ip route                                      ; Shows the entire routing table
R1# show ip routing rip                                ; Shows routes learned via RIP only
R1# show ip route 10.1.1.1                             ; Detailed information about specific route

```

---

## OSPF Configuration

### OSPF Setup commands

* **Enter OSPF router configuration mode:**
```ios
R1(config)# router ospf 10                           ; process ID

```


* **Configure network commands to identify OSPF interfaces:**
```ios
R1(config-router)# network 10.0.0.0 0.255.255.255 area 0
R1(config-router)# network 172.16.8.0 0.0.7.255 area 0
R1(config-router)# network 192.168.1.254 0.0.0.0 area 1

```


* **Configure router ID either by: (Optional)**
```ios
R1(config-router)# router-id 1.1.1.1                ; Using router-id command

; Or configuring an IP address on a loopback interface:
R1(config)# interface loopback 0
R1(config-if)# ip address 1.1.1.1 255.255.255.255

```


* **Change Hello and Dead intervals per interface: (Optional)**
```ios
R1(config-if)# ip ospf hello-interval 2
R1(config-if)# ip ospf dead-interval 6

```


* **Impact routing choices by tuning interface cost: (Optional)**
```ios
R1(config-if)# ip ospf cost 55                      ; Changing interface cost
R1(config-if)# bandwidth 128                        ; Changing interface bandwidth (kbps)
R1(config-router)# auto-cost reference-bandwidth 1000 ; Changing the reference bandwidth (Mbps)

```


* **Disabling OSPF on a certain interface: (Optional)**
```ios
R1(config-router)# passive-interface serial 0/0

```



### Configuring OSPF authentication: (Optional)

* **Type 0 authentication (none):**
```ios
R1(config-if)# ip ospf authentication null

```


* **Type 1 authentication (Clear text):**
```ios
R1(config-if)# ip ospf authentication
R1(config-if)# ip ospf authentication-key cisco

```


* **Type 2 authentication (md5):**
```ios
R1(config-if)# ip ospf authentication message-digest
R1(config-if)# ip ospf message-digest-key 1 md5 cisco

```


* **Configure maximum equal-cost paths: (Optional)**
```ios
R1(config-router)# maxmum path 6

```



### OSPF verification

```ios
R1# show ip protocols                                  ; Show information about the running routing process
R1# show ip route                                      ; Shows the entire routing table
R1# show ip route ospf                                 ; Shows routes learned via OSPF only
R1# show ip ospf neighbors                             ; Shows all neighboring routers along with adjacency state
R1# show ip ospf database                              ; Shows detailed information contained in the LSDB
R1# show ip ospf interfaces serial 0/0                 ; Shows detailed information about OSPF running on interface

```

---

## EIGRP Configuration

### EIGRP Setup commands

* **Enter EIGRP configuration mode and define AS number:**
```ios
R1(config)# router eigrp 121                         ; AS number

```


* **Configure one or more network commands to enable EIGRP:**
```ios
R1(config-router)# network 10.0.0.0
R1(config-router)# network 172.16.0.0 0.0.3.255
R1(config-router)# network 192.168.1.1 0.0.0.0
R1(config-router)# network 0.0.0.0 255.255.255.255

```


* **Disable auto summarization: (Optional)**
```ios
R1(config-router)# no autosummary

```


* **Disable EIGRP on a specific interface: (Optional)**
```ios
R1(config-router)# passive-interface serial 0/0

```


* **Configure load balancing parameters: (Optional)**
```ios
R1(config-router)# maximum-paths 6
R1(config-router)# variance 4

```


* **Change interface Hello and Hold timers: (Optional)**
```ios
R1(config-if)# ip hello-interval eigrp 121 3
R1(config-if)# ip hold-time eigrp 121 10

```


* **Impacting metric calculations by tuning BW and delay: (Optional)**
```ios
R1(config-if)# bandwidth 265                         ; (kbps)
R1(config-if)# delay 120                             ; (tens of microseconds)

```



### EIGRP Authentication

* **Create an authentication key chain:**
```ios
R1(config)# key chain MY_KEYS
R1(config-keychain)# key 1
R1(config-keychain-key)# key-string 1stKEY           ; Must match on both routers

; Define life time of the keys (optional):
R1(config-keychain-key)# send-lifetime [start time] [end time]
R1(config-keychain-key)# accept-lifetime [start time] [end time]

```


* **Enable md5 authentication mode for EIGRP on the interface:**
```ios
R1(config-if)# ip authentication mode eigrp 121 md5

```


* **Refer to the correct key chain to be used on the interface:**
```ios
R1(config-if)# ip authentication key-chain eigrp 121 MY_KEYS

```



*(Note: Key authentication requires synchronized router clocks. Utilize NTP to avoid issues).*

### EIGRP Verification

```ios
R1# show ip route eigrp                                ; Shows routes learned via EIGRP only
R1# show ip eigrp neighbors                            ; Shows EIGRP neighbors and status
R1# show ip eigrp topology                             ; Shows EIGRP topology table (successors/feasible successors)
R1# show ip eigrp interfaces                           ; Shows Interfaces that run EIGRP
R1# show ip eigrp traffic                              ; Lists statistics on EIGRP messages sent and received

```

---

## Access Control Lists (ACLs)

### Standard ACL

*Numbered range: 1–99 and 1300–1999.*

* **Use a remark to describe the ACL (Optional):**
```ios
R1(config)# access-list 1 remark ACL TO DENY ACCESS FROM SALES VLAN

```


* **Create the ACL (Remember implicit deny any at the end):**
```ios
R1(config)# access-list 2 deny 192.168.1.77
R1(config)# access-list 2 deny 192.168.1.64 0.0.0.31
R1(config)# access-list 2 permit 10.1.0.0 0.0.255.255
R1(config)# access-list 2 deny 10.0.0.0 0.255.255.255
R1(config)# access-list 2 permit any

```


* **Enable the ACL on the chosen router interface:**
```ios
R1(config-if)# ip access-group 2 out

```


* **Using standard ACL to limit telnet and SSH access to a router:**
```ios
R1(config)# access-list 99 remark ALLOWED TELNET CLIENTS
R1(config)# access-list 99 permit 192.168.1.128 0.0.0.15
R1(config)# line vty 0 4
R1(config-line)# access-class 99 in

```



### Extended ACL

*Numbered range: 100–199 and 2000–2699.*

```ios
R1(config)# access-list 101 remark MY_ACCESS_LIST
R1(config)# access-list 101 deny ip host 10.1.1.1 host 10.2.2.2
R1(config)# access-list 101 deny tcp 10.1.1.0 0.0.0.255 any eq 23
R1(config)# access-list 101 deny icmp 10.1.1.1 0.0.0.0 any
R1(config)# access-list 101 deny tcp host 10.1.1.0 host 10.0.0.1 eq 80
R1(config)# access-list 101 deny udp host 10.1.1.7 eq 53 any
R1(config)# access-list 101 permit ip any any
R1(config)# interface fastEthernet 0/0
R1(config-if)# ip access-group 101 in

```

### Named ACL

* **Named standard ACL:**
```ios
R1(config)# ip access-list standard MY_STANDARD_ACL
R1(config-std-nacl)# permit 10.1.1.0 0.0.0.255
R1(config-std-nacl)# deny 10.2.2.2
R1(config-std-nacl)# permit any
R1(config)# interface fastEthernet 0/1
R1(config-if)# ip access-group MY_STANDARD_ACL out

```


* **Named extended ACL:**
```ios
R1(config)# ip access-list extended MY_EXTENDED_ACL
R1(config-ext-nacl)# deny icmp 10.1.1.1 0.0.0.0 any
R1(config-ext-nacl)# deny tcp host 10.1.1.0 host 10.0.0.1 eq 80
R1(config-ext-nacl)# permit ip any any
R1(config)# interface fastEthernet 0/1
R1(config-if)# ip access-group MY_EXTENDED_ACL in

```


* **Editing ACL using sequence numbers:**
```ios
R1(config)# ip access-list extended MY_EXTENDED_ACL
R1(config-ext-nacl)# no 20                       ; Deletes statement at sequence 20

R1(config)# ip access-list standard 99
R1(config-std-nacl)# 5 deny 1.1.1.1              ; Inserts a statement at sequence 5

```



### Verifying ACLs

```ios
R1# show access-lists                                  ; Shows all ACLs configured with counters
R1# show ip access-list                                ; Same as previous command
R1# show ip access-list 101                            ; Shows only specified ACL
R1# show ip interface f0/0                             ; Confirms if ACL is enabled inbound or outbound

```

---

## DHCP Server

### Define a DHCP pool and settings

```ios
R1(config)# ip dhcp pool MY_POOL
R1(dhcp-config)# network 192.168.1.0 255.255.255.0
R1(dhcp-config)# default-router 192.168.1.1
R1(dhcp-config)# dns-server 213.131.65.20 8.8.8.8      ; Optional
R1(dhcp-config)# lease 2                               ; Optional (days)

```

### Define scopes of excluded addresses (Optional)

```ios
R1(config)# ip dhcp excluded-address 192.168.1.1 192.168.1.100
R1(config)# ip dhcp excluded-address 192.168.1.200 192.168.1.254

```

### DHCP Verification and Troubleshooting

```ios
R1# show ip dhcp pool POOL_1                           ; Status of specified pool and leased addresses
R1# show ip dhcp binding                              ; All leased IP addresses from all pools
R1# show ip dhcp conflict                             ; Shows any IP conflicts that occurred

```

---

## WAN Configurations (PPP & Frame Relay)

### PPP Configuration

```ios
R1(config)# interface serial 0/0
R1(config-if)# encapsulation ppp

```

### PPP Authentication Configurations

* **CHAP Configuration:**
```ios
R1(config)# hostname ALPHA
ALPHA(config)# username BETA password XYZ            ; Shared password must be same on both sides
ALPHA(config)# interface serial 0/0
ALPHA(config-if)# ppp authentication chap

```


* **PAP Configuration:**
```ios
R1(config)# hostname ALPHA
ALPHA(config)# username BETA password XYZ
ALPHA(config)# interface serial 0/0
ALPHA(config-if)# ppp authentication pap
ALPHA(config-if)# ppp pap sent-username ALPHA password XYZ

```



### PPP Verification and troubleshoot

```ios
R1# show interface s0/0                                ; Shows encapsulation type and control protocols
R1# show run                                           ; View configuration of usernames and passwords
R1# debug ppp authentication                          ; Displays authentication process in real time

```

### Frame Relay Configurations

* **Multipoint (one subnet):**
```ios
R1(config)# interface serial 0/0
R1(config-if)# ip address 1.1.1.1 255.255.255.0
R1(config-if)# encapsulation frame-relay (ietf)
R1(config-if)# frame-relay lmi-type ansi             ; Options: ansi, cisco, q933a
R1(config-if)# frame-relay map 1.1.1.2 102 broadcast (ietf)
R1(config-if)# frame-relay map 1.1.1.3 103 broadcast

R2(config)# interface serial 0/0
R2(config-if)# ip address 1.1.1.2 255.255.255.0
R2(config-if)# encapsulation frame-relay
R2(config-if)# frame-relay map 1.1.1.1 201 broadcast
R2(config-if)# frame-relay map 1.1.1.3 201 broadcast

R3(config)# interface serial 0/0
R3(config-if)# ip address 1.1.1.3 255.255.255.0
R3(config-if)# encapsulation frame-relay
R3(config-if)# frame-relay map 1.1.1.1 301 broadcast
R3(config-if)# frame-relay map 1.1.1.2 301 broadcast

```


* **Point-to-point (different subnets; one subnet per subinterface):**
```ios
R1(config)# interface serial 0/0
R1(config-if)# encapsulation frame-relay
R1(config)# interface serial 0/0.102 point-to-point
R1(config-subif)# ip address 1.1.1.1 255.255.255.0
R1(config-subif)# frame-relay interface-dlci 102
R1(config)# interface serial 0/0.103 point-to-point
R1(config-subif)# ip address 2.2.2.1 255.255.255.0
R1(config-subif)# frame-relay interface-dlci 103

R2(config)# interface serial 0/0
R2(config-if)# encapsulation frame-relay
R2(config)# interface serial 0/0.201 point-to-point
R2(config-subif)# ip address 1.1.1.2 255.255.255.0
R2(config-subif)# frame-relay interface-dlci 201

R3(config)# interface serial 0/0
R3(config-if)# encapsulation frame-relay
R3(config)# interface serial 0/0.301 point-to-point
R3(config-subif)# ip address 2.2.2.2 255.255.255.0
R3(config-subif)# frame-relay interface-dlci 301

```



### Frame Relay Verification and troubleshoot

```ios
R1# show interfaces serial 0/0                         ; Shows encapsulation type
R1# show frame-relay pvc                               ; Lists PVC status information
R1# show frame-relay map                               ; Lists DLCI to IP mapping
R1# show frame-relay lmi                               ; Lists LMI status information
R1# debug frame-relay lmi                              ; Displays content of LMI messages
R1# debug frame-relay events                           ; Lists messages about Frame Relay events/Inverse ARP

```

---

## Network Address Translation (NAT)

### Static NAT

```ios
R1(config)# interface serial 0/0
R1(config-if)# ip nat outside
R1(config)# interface FastEthernet 1/1
R1(config-if)# ip nat inside
R1(config)# ip nat inside source static 192.168.1.10 200.1.1.1

```

### Dynamic NAT

```ios
R1(config)# interface serial 0/0
R1(config-if)# ip nat outside
R1(config)# interface FastEthernet 1/1
R1(config-if)# ip nat inside
R1(config)# access-list 3 permit 192.168.1.0 0.0.0.255 ; ACL for allowed translation IP pool
R1(config)# ip nat pool PUB 200.1.1.1 200.1.1.6 netmask 255.255.255.248
R1(config)# ip nat inside source list 3 pool PUB

```

### NAT Overload (PAT)

```ios
; Same configuration as dynamic NAT but appended with the overload keyword
R1(config)# ip nat inside source list 3 pool PUB overload

```

### NAT Verification and troubleshoot

```ios
R1# show run                                           ; View configuration of NAT pools and interfaces
R1# show access-lists                                  ; Displays ACLs, including those used for NAT
R1# show ip nat statistics                             ; Shows counters for packets, NAT table entries, etc.
R1# show ip nat translations                           ; Displays the active NAT table
R1# clear ip nat translations* ; Clears all dynamic entries from the NAT table
R1# debug ip nat                                       ; Issues a log message describing translated packets

```

```

```