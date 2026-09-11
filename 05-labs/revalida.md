# Production Cisco IOS Configuration Plan & Scripts

**Scope:** Static IP, VLANs, Trunking, Router-on-a-Stick, Rapid-PVST+, OSPF, NAT/PAT, Switch Security, Inter-VLAN ACLs

**Target Platform:** Cisco IOS / IOS-XE / Cisco Packet Tracer Topology

---

## Part A: Complete IP Addressing Table

### Router & Switch Management Infrastructure

| Device | Interface / SVI | IP Address | Subnet Mask | Purpose / Connection |
| --- | --- | --- | --- | --- |
| **R-ISP** | G0/0 | `203.0.113.1` | `255.255.255.252` | Connection to R-EDGE G0/2 |
| **R-EDGE** | G0/2 | `203.0.113.2` | `255.255.255.252` | WAN Link to R-ISP G0/0 |
| **R-EDGE** | G0/1 | `10.0.0.1` | `255.255.255.252` | Link to R-CORE1 G0/1 |
| **R-EDGE** | G0/0 | `10.0.0.5` | `255.255.255.252` | Link to R-CORE2 G0/0 |
| **R-CORE1** | G0/1 | `10.0.0.2` | `255.255.255.252` | Link to R-EDGE G0/1 |
| **R-CORE1** | G0/0 | `10.0.0.9` | `255.255.255.252` | Link to R-CORE2 G0/1 |
| **R-CORE1** | G0/2 | `10.0.0.13` | `255.255.255.252` | Link to SW-DIST1 G0/1 (Routed transit) |
| **R-CORE2** | G0/0 | `10.0.0.6` | `255.255.255.252` | Link to R-EDGE G0/0 |
| **R-CORE2** | G0/1 | `10.0.0.10` | `255.255.255.252` | Link to R-CORE1 G0/0 |
| **R-CORE2** | G0/2 | `10.0.0.14` | `255.255.255.252` | Base interface for ROAS |
| **SW-DIST1** | VLAN 93 SVI | `172.20.0.2` | `255.255.255.240` | Switch Management |
| **SW-DIST2** | VLAN 93 SVI | `172.20.0.3` | `255.255.255.240` | Switch Management |
| **SW-ACCESS1** | VLAN 93 SVI | `172.20.0.4` | `255.255.255.240` | Switch Management |
| **SW-ACCESS2** | VLAN 93 SVI | `172.20.0.5` | `255.255.255.240` | Switch Management |

---

## Part B: Complete Port & VLAN Assignment Table

| Local Device | Interface | Remote Device | Remote Interface | Port Mode | Assigned / Allowed VLANs |
| --- | --- | --- | --- | --- | --- |
| **R-CORE2** | G0/2 | SW-DIST2 | G0/1 | Trunk (802.1Q) | `10, 20, 93` |
| **SW-DIST1** | G0/1 | R-CORE1 | G0/2 | Trunk / L3 Link | `10, 20, 93` |
| **SW-DIST1** | Fa0/2 | SW-DIST2 | Fa0/2 | Trunk | `10, 20, 93` |
| **SW-DIST1** | Fa0/1 | SW-ACCESS1 | Fa0/1 | Trunk | `10, 20, 93` |
| **SW-DIST2** | G0/1 | R-CORE2 | G0/2 | Trunk | `10, 20, 93` |
| **SW-DIST2** | Fa0/2 | SW-DIST1 | Fa0/2 | Trunk | `10, 20, 93` |
| **SW-DIST2** | Fa0/4 | SW-ACCESS2 | Fa0/4 | Trunk | `10, 20, 93` |
| **SW-ACCESS1** | Fa0/1 | SW-DIST1 | Fa0/1 | Trunk | `10, 20, 93` |
| **SW-ACCESS1** | Fa0/3 | SW-ACCESS2 | Fa0/3 | Trunk | `10, 20, 93` |
| **SW-ACCESS1** | Fa0/21 | PC0 | Fa0 | Access | `VLAN 10 (SALES)` |
| **SW-ACCESS1** | Fa0/22 | PC1 | Fa0 | Access | `VLAN 10 (SALES)` |
| **SW-ACCESS1** | Fa0/23 | PC2 | Fa0 | Access | `VLAN 20 (IT-ADMIN)` |
| **SW-ACCESS1** | Fa0/24 | PC3 | Fa0 | Access | `VLAN 20 (IT-ADMIN)` |
| **SW-ACCESS2** | Fa0/4 | SW-DIST2 | Fa0/4 | Trunk | `10, 20, 93` |
| **SW-ACCESS2** | Fa0/3 | SW-ACCESS1 | Fa0/3 | Trunk | `10, 20, 93` |
| **SW-ACCESS2** | Fa0/11 | PC5 | Fa0 | Access | `VLAN 93 (MANAGEMENT)` |
| **SW-ACCESS2** | Fa0/12 | PC4 | Fa0 | Access | `VLAN 93 (MANAGEMENT)` |

---

## Router Configurations

### 1. R-ISP Configuration

```cisconetworking
enable
configure terminal

hostname R-ISP
no ip domain-lookup

username admin privilege 15 secret AdminPass123!

interface Loopback0
 description Simulated Internet Target
 ip address 8.8.8.8 255.255.255.255
 no shutdown

interface GigabitEthernet0/0
 description Link to R-EDGE G0/2
 ip address 203.0.113.1 255.255.255.252
 no shutdown

line con 0
 logging synchronous
 login local
line vty 0 4
 login local

end
write memory

```

---

### 2. R-EDGE Configuration

```cisconetworking
enable
configure terminal

hostname R-EDGE
no ip domain-lookup

username admin privilege 15 secret AdminPass123!

interface Loopback0
 description OSPF Router ID
 ip address 1.1.1.1 255.255.255.255
 no shutdown

interface GigabitEthernet0/0
 description Link to R-CORE2 G0/0
 ip address 10.0.0.5 255.255.255.252
 ip nat inside
 no shutdown

interface GigabitEthernet0/1
 description Link to R-CORE1 G0/1
 ip address 10.0.0.1 255.255.255.252
 ip nat inside
 no shutdown

interface GigabitEthernet0/2
 description WAN Link to R-ISP G0/0
 ip address 203.0.113.2 255.255.255.252
 ip nat outside
 no shutdown

router ospf 1
 router-id 1.1.1.1
 network 1.1.1.1 0.0.0.0 area 0
 network 10.0.0.0 0.0.0.3 area 0
 network 10.0.0.4 0.0.0.3 area 0
 default-information originate

ip route 0.0.0.0 0.0.0.0 203.0.113.1

ip access-list standard NAT-ACL
 permit 192.168.10.0 0.0.0.255
 permit 172.16.20.0 0.0.0.255
 permit 172.20.0.0 0.0.0.15

ip nat inside source list NAT-ACL interface GigabitEthernet0/2 overload

line con 0
 logging synchronous
 login local
line vty 0 4
 login local

end
write memory

```

---

### 3. R-CORE1 Configuration

```cisconetworking
enable
configure terminal

hostname R-CORE1
no ip domain-lookup

username admin privilege 15 secret AdminPass123!

interface Loopback0
 description OSPF Router ID
 ip address 2.2.2.2 255.255.255.255
 no shutdown

interface GigabitEthernet0/0
 description Link to R-CORE2 G0/1
 ip address 10.0.0.9 255.255.255.252
 no shutdown

interface GigabitEthernet0/1
 description Link to R-EDGE G0/1
 ip address 10.0.0.2 255.255.255.252
 no shutdown

interface GigabitEthernet0/2
 description Link to SW-DIST1 G0/1
 ip address 10.0.0.13 255.255.255.252
 no shutdown

router ospf 1
 router-id 2.2.2.2
 network 2.2.2.2 0.0.0.0 area 0
 network 10.0.0.0 0.0.0.3 area 0
 network 10.0.0.8 0.0.0.3 area 0
 network 10.0.0.12 0.0.0.3 area 0

line con 0
 logging synchronous
 login local
line vty 0 4
 login local

end
write memory

```

---

### 4. R-CORE2 Configuration

```cisconetworking
enable
configure terminal

hostname R-CORE2
no ip domain-lookup

username admin privilege 15 secret AdminPass123!

! --- Inter-VLAN Access Control List ---
ip access-list extended BLOCK-SALES-TO-IT-MGMT
 permit tcp 192.168.10.0 0.0.0.255 172.16.20.0 0.0.0.255 established
 permit tcp 192.168.10.0 0.0.0.255 172.20.0.0 0.0.0.15 established
 deny ip 192.168.10.0 0.0.0.255 172.16.20.0 0.0.0.255
 deny ip 192.168.10.0 0.0.0.255 172.20.0.0 0.0.0.15
 permit ip 192.168.10.0 0.0.0.255 any

interface Loopback0
 description OSPF Router ID
 ip address 3.3.3.3 255.255.255.255
 no shutdown

interface GigabitEthernet0/0
 description Link to R-EDGE G0/0
 ip address 10.0.0.6 255.255.255.252
 no shutdown

interface GigabitEthernet0/1
 description Link to R-CORE1 G0/0
 ip address 10.0.0.10 255.255.255.252
 no shutdown

! --- Router-on-a-Stick Subinterfaces ---
interface GigabitEthernet0/2
 description ROAS Base Link to SW-DIST2 G0/1
 no shutdown

interface GigabitEthernet0/2.10
 description Gateway - VLAN 10 (SALES)
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 ip access-group BLOCK-SALES-TO-IT-MGMT in

interface GigabitEthernet0/2.20
 description Gateway - VLAN 20 (IT-ADMIN)
 encapsulation dot1Q 20
 ip address 172.16.20.1 255.255.255.0

interface GigabitEthernet0/2.93
 description Gateway - VLAN 93 (MANAGEMENT)
 encapsulation dot1Q 93
 ip address 172.20.0.1 255.255.255.240

router ospf 1
 router-id 3.3.3.3
 network 3.3.3.3 0.0.0.0 area 0
 network 10.0.0.4 0.0.0.3 area 0
 network 10.0.0.8 0.0.0.3 area 0
 network 192.168.10.0 0.0.0.255 area 0
 network 172.16.20.0 0.0.0.255 area 0
 network 172.20.0.0 0.0.0.15 area 0
 passive-interface GigabitEthernet0/2.10
 passive-interface GigabitEthernet0/2.20
 passive-interface GigabitEthernet0/2.93

line con 0
 logging synchronous
 login local
line vty 0 4
 login local

end
write memory

```

---

## Switch Configurations

### 5. SW-DIST1 Configuration

```cisconetworking
enable
configure terminal

hostname SW-DIST1
no ip domain-lookup

username admin privilege 15 secret AdminPass123!

vlan 10
 name SALES
vlan 20
 name IT-ADMIN
vlan 93
 name MANAGEMENT
exit

spanning-tree mode rapid-pvst
spanning-tree vlan 10,20,93 root primary

interface GigabitEthernet0/1
 description Link to R-CORE1 G0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,20,93
 no shutdown

interface FastEthernet0/1
 description Trunk to SW-ACCESS1 Fa0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,20,93
 no shutdown

interface FastEthernet0/2
 description Trunk to SW-DIST2 Fa0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,20,93
 no shutdown

interface vlan 93
 description Management SVI
 ip address 172.20.0.2 255.255.255.240
 no shutdown

ip default-gateway 172.20.0.1

interface range FastEthernet0/3-24, GigabitEthernet0/2
 shutdown

line con 0
 logging synchronous
 login local
line vty 0 4
 login local

end
write memory

```

---

### 6. SW-DIST2 Configuration

```cisconetworking
enable
configure terminal

hostname SW-DIST2
no ip domain-lookup

username admin privilege 15 secret AdminPass123!

vlan 10
 name SALES
vlan 20
 name IT-ADMIN
vlan 93
 name MANAGEMENT
exit

spanning-tree mode rapid-pvst
spanning-tree vlan 10,20,93 root secondary

interface GigabitEthernet0/1
 description Link to R-CORE2 G0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,20,93
 no shutdown

interface FastEthernet0/2
 description Trunk to SW-DIST1 Fa0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,20,93
 no shutdown

interface FastEthernet0/4
 description Trunk to SW-ACCESS2 Fa0/4
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,20,93
 no shutdown

interface vlan 93
 description Management SVI
 ip address 172.20.0.3 255.255.255.240
 no shutdown

ip default-gateway 172.20.0.1

interface range FastEthernet0/1, FastEthernet0/3, FastEthernet0/5-24, GigabitEthernet0/2
 shutdown

line con 0
 logging synchronous
 login local
line vty 0 4
 login local

end
write memory

```

---

### 7. SW-ACCESS1 Configuration

```cisconetworking
enable
configure terminal

hostname SW-ACCESS1
no ip domain-lookup

username admin privilege 15 secret AdminPass123!

vlan 10
 name SALES
vlan 20
 name IT-ADMIN
vlan 93
 name MANAGEMENT
exit

spanning-tree mode rapid-pvst

interface FastEthernet0/1
 description Trunk to SW-DIST1 Fa0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,93
 no shutdown

interface FastEthernet0/3
 description Trunk to SW-ACCESS2 Fa0/3
 switchport mode trunk
 switchport trunk allowed vlan 10,20,93
 no shutdown

interface range FastEthernet0/21 - 22
 description Access Ports - SALES (VLAN 10)
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown

interface range FastEthernet0/23 - 24
 description Access Ports - IT-ADMIN (VLAN 20)
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown

interface vlan 93
 description Management SVI
 ip address 172.20.0.4 255.255.255.240
 no shutdown

ip default-gateway 172.20.0.1

interface range FastEthernet0/2, FastEthernet0/4-20, GigabitEthernet0/1-2
 shutdown

line con 0
 logging synchronous
 login local
line vty 0 4
 login local

end
write memory

```

---

### 8. SW-ACCESS2 Configuration

```cisconetworking
enable
configure terminal

hostname SW-ACCESS2
no ip domain-lookup

username admin privilege 15 secret AdminPass123!

vlan 10
 name SALES
vlan 20
 name IT-ADMIN
vlan 93
 name MANAGEMENT
exit

spanning-tree mode rapid-pvst

interface FastEthernet0/4
 description Trunk to SW-DIST2 Fa0/4
 switchport mode trunk
 switchport trunk allowed vlan 10,20,93
 no shutdown

interface FastEthernet0/3
 description Trunk to SW-ACCESS1 Fa0/3
 switchport mode trunk
 switchport trunk allowed vlan 10,20,93
 no shutdown

interface range FastEthernet0/11 - 12
 description Access Ports - MANAGEMENT (VLAN 93)
 switchport mode access
 switchport access vlan 93
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown

interface vlan 93
 description Management SVI
 ip address 172.20.0.5 255.255.255.240
 no shutdown

ip default-gateway 172.20.0.1

interface range FastEthernet0/1-2, FastEthernet0/5-10, FastEthernet0/13-24, GigabitEthernet0/1-2
 shutdown

line con 0
 logging synchronous
 login local
line vty 0 4
 login local

end
write memory

```

---

## Part C: Static End-Device Configuration Table

| Host | Connected Switch / Port | VLAN ID | IP Address | Subnet Mask | Default Gateway | DNS |
| --- | --- | --- | --- | --- | --- | --- |
| **PC0** | SW-ACCESS1 / Fa0/21 | 10 | `192.168.10.11` | `255.255.255.0` | `192.168.10.1` | `8.8.8.8` |
| **PC1** | SW-ACCESS1 / Fa0/22 | 10 | `192.168.10.12` | `255.255.255.0` | `192.168.10.1` | `8.8.8.8` |
| **PC2** | SW-ACCESS1 / Fa0/23 | 20 | `172.16.20.11` | `255.255.255.0` | `172.16.20.1` | `8.8.8.8` |
| **PC3** | SW-ACCESS1 / Fa0/24 | 20 | `172.16.20.12` | `255.255.255.0` | `172.16.20.1` | `8.8.8.8` |
| **PC5** | SW-ACCESS2 / Fa0/11 | 93 | `172.20.0.11` | `255.255.255.240` | `172.20.0.1` | `8.8.8.8` |
| **PC4** | SW-ACCESS2 / Fa0/12 | 93 | `172.20.0.12` | `255.255.255.240` | `172.20.0.1` | `8.8.8.8` |

---

## Part D: Essential Verification Checklist

```cisconetworking
! --- Layer 2 Checking on Switches ---
show vlan brief
show interfaces trunk
show spanning-tree

! --- Layer 3 & OSPF Checking on Routers ---
show ip interface brief
show ip route ospf
show ip ospf neighbor

! --- Security & NAT Checking on R-CORE2 & R-EDGE ---
show access-lists BLOCK-SALES-TO-IT-MGMT
show ip nat translations

```