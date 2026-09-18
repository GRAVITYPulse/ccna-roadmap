##### IP Address Management (IPAM) Table

| Device | Interface / Sub-interface | IP Address | Subnet Mask | Gateway / Virtual IP | Description / Function |
| --- | --- | --- | --- | --- | --- |
| **PC0 / PC1** | Fa0 | 192.168.10.11 - 12 | 255.255.255.0 | 192.168.10.1 | **VLAN 10**  (SALES Workstations)|
| **PC2 / PC3** | Fa0 | 172.16.20.11 - 12 | 255.255.255.0 | 172.16.20.1 | **VLAN 20**  (IT_ADMIN Workstations)|
| **PC4 / PC5** | Fa0 | 172.20.0.11 - 12 | 255.255.255.240 | 172.20.0.1 | **VLAN 93**  (MANAGEMENT Workstations)|
| **SW-DIST1** | Vlan 10 | 192.168.10.2 | 255.255.255.0 | **VIP:**  192.168.10.1 | Active HSRP Gateway for VLAN 10|
|  | Vlan 20 | 172.16.20.2 | 255.255.255.0 | **VIP:**  172.16.20.1 | Active HSRP Gateway for VLAN 20|
|  | Vlan 93 | 172.20.0.2 | 255.255.255.240 | **VIP:**  172.20.0.1 | Active HSRP Gateway for VLAN 93|
|  | Vlan 99 | 10.0.0.13 | 255.255.255.240 | N/A | Management SVI / Native VLAN|
|  | Gi0/1 | 10.0.0.2 | 255.255.255.252 | N/A | Routed Link to R-EDGE (Gi0/0)|
| **SW-DIST2** | Vlan 10 | 192.168.10.3 | 255.255.255.0 | **VIP:**  192.168.10.1 | Standby HSRP Gateway for VLAN 10|
|  | Vlan 20 | 172.16.20.3 | 255.255.255.0 | **VIP:**  172.16.20.1 | Standby HSRP Gateway for VLAN 20|
|  | Vlan 93 | 172.20.0.3 | 255.255.255.240 | **VIP:**  172.20.0.1 | Standby HSRP Gateway for VLAN 93|
|  | Vlan 99 | 10.0.0.14 | 255.255.255.240 | N/A | Management SVI / Native VLAN|
|  | Gi0/1 | 10.0.0.6 | 255.255.255.252 | N/A | Routed Link to R-EDGE (Gi0/1)|
|  | Fa0/3 | 10.0.0.9 | 255.255.255.252 | N/A | Routed Link to R-DHCP (Gi0/0)|
| **R-EDGE** | Gi0/0 | 10.0.0.1 | 255.255.255.252 | N/A | Point-to-Point Link to SW-DIST1|
|  | Gi0/1 | 10.0.0.5 | 255.255.255.252 | N/A | Point-to-Point Link to SW-DIST2|
|  | Gi0/2 | 203.0.113.2 | 255.255.255.252 | 203.0.113.1 | Public WAN Link to R-ISP|
| **R-DHCP** | Gi0/0 | 10.0.0.10 | 255.255.255.252 | 10.0.0.9 | Link to SW-DIST2|
| **R-ISP** | Gi0/0 | 203.0.113.1 | 255.255.255.252 | N/A | Internet Service Provider Gateway|

---

##### Functions Breakdown

* **VLAN (Virtual Local Area Network):**  Logically segments physical switch infrastructure into separate broadcast domains for security, administrative grouping, and traffic containment.


* **STP (Spanning Tree Protocol):**  Prevents Layer 2 loops and broadcast storms on redundant physical paths by putting redundant links into a logical blocking state.


* **EtherChannel:**  Aggregates multiple physical switch interfaces into a single logical link (Port-Channel) to increase link bandwidth and provide fault tolerance.


* **OSPF (Open Shortest Path First):**  An Interior Gateway Protocol (IGP) dynamic link-state routing protocol used to dynamically exchange subnets and compute the optimal path for Layer 3 packets.


* **DHCP (Dynamic Host Configuration Protocol) & Relay:**  Automatically leases network credentials (IP, Subnet, Gateway, DNS) to hosts. The ip helper-address forwards DHCP broadcasts as unicast traffic across router boundaries.


* **HSRP / VRRP (First Hop Redundancy Protocols):**  Provides high availability for endpoint default gateways by pooling multiple Layer 3 switches/routers into a single virtual IP (VIP) address.


* **NAT / NAT Overload (PAT):**  Translates non-routable private IPv4 addresses (RFC 1918) into a public IPv4 address, allowing multiple internal hosts to share one public IP using source TCP/UDP ports.


* **ACL (Access Control List):**  Filters inbound and outbound IP traffic at Layer 3/4 based on rules defined by source IP, destination IP, protocol, and port numbers.



---

##### Full Configuration Scripts

###### 1. SW-ACCESS1

```cisconetwork
enable
configure terminal
hostname SW-ACCESS1

! VLAN Definitions
vlan 10
 name SALES
vlan 20
 name IT_ADMIN
vlan 93
 name MANAGEMENT
vlan 99
 name NATIVE_MGMT
exit

! STP Enhancements
spanning-tree mode rapid-pvst

! EtherChannel to SW-ACCESS2 (Fa0/2 - Fa0/3)
interface range FastEthernet0/2 - 3
 channel-group 1 mode active
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,93,99
 no shutdown

! Trunk Links to Distribution Switches
interface FastEthernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,93,99
 no shutdown

interface FastEthernet0/4
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,93,99
 no shutdown

! Access Ports
interface range FastEthernet0/21 - 22
 description SALES_HOSTS
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown

interface range FastEthernet0/23 - 24
 description IT_ADMIN_HOSTS
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit


```

###### 2. SW-ACCESS2

```cisconetwork
enable
configure terminal
hostname SW-ACCESS2

! VLAN Definitions
vlan 10
 name SALES
vlan 20
 name IT_ADMIN
vlan 93
 name MANAGEMENT
vlan 99
 name NATIVE_MGMT
exit

spanning-tree mode rapid-pvst

! EtherChannel to SW-ACCESS1 (Fa0/2 - Fa0/3)
interface range FastEthernet0/2 - 3
 channel-group 1 mode active
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,93,99
 no shutdown

! Trunk Links to Distribution Switches
interface FastEthernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,93,99
 no shutdown

interface FastEthernet0/4
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,93,99
 no shutdown

! Access Ports
interface range FastEthernet0/11 - 12
 description MANAGEMENT_HOSTS
 switchport mode access
 switchport access vlan 93
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit


```

###### 3. SW-DIST1 (Primary STP / Active HSRP)

```cisconetwork
enable
configure terminal
hostname SW-DIST1
ip routing

vlan 10
 name SALES
vlan 20
 name IT_ADMIN
vlan 93
 name MANAGEMENT
vlan 99
 name NATIVE_MGMT
exit

! STP Primary Root
spanning-tree mode rapid-pvst
spanning-tree vlan 10,20,93 priority 4096

! EtherChannel to SW-DIST2 (Fa0/2 - Fa0/4)
interface range FastEthernet0/2, FastEthernet0/4
 channel-group 2 mode active
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,93,99
 no shutdown

! Downlink Trunks to Access Switches
interface FastEthernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,93,99
 no shutdown

interface FastEthernet0/13
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,93,99
 no shutdown

! Routed Interface to R-EDGE
interface GigabitEthernet0/1
 no switchport
 ip address 10.0.0.2 255.255.255.252
 no shutdown

! SVIs, HSRP & DHCP Relays
interface Vlan10
 ip address 192.168.10.2 255.255.255.0
 ip helper-address 10.0.0.10
 standby 10 ip 192.168.10.1
 standby 10 priority 110
 standby 10 preempt
 no shutdown

interface Vlan20
 ip address 172.16.20.2 255.255.255.0
 ip helper-address 10.0.0.10
 standby 20 ip 172.16.20.1
 standby 20 priority 110
 standby 20 preempt
 no shutdown

interface Vlan93
 ip address 172.20.0.2 255.255.255.240
 ip helper-address 10.0.0.10
 standby 93 ip 172.20.0.1
 standby 93 priority 110
 standby 93 preempt
 no shutdown

interface Vlan99
 ip address 10.0.0.13 255.255.255.240
 no shutdown

! Routing Protocol
router ospf 1
 router-id 1.1.1.1
 network 10.0.0.0 0.0.0.3 area 0
 network 192.168.10.0 0.0.0.255 area 0
 network 172.16.20.0 0.0.0.255 area 0
 network 172.20.0.0 0.0.0.15 area 0
exit


```

###### 4. SW-DIST2 (Secondary STP / Standby HSRP)

```cisconetwork
enable
configure terminal
hostname SW-DIST2
ip routing

vlan 10
 name SALES
vlan 20
 name IT_ADMIN
vlan 93
 name MANAGEMENT
vlan 99
 name NATIVE_MGMT
exit

spanning-tree mode rapid-pvst
spanning-tree vlan 10,20,93 priority 8192

! EtherChannel to SW-DIST1
interface range FastEthernet0/2, FastEthernet0/4
 channel-group 2 mode active
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,93,99
 no shutdown

! Downlink Trunks
interface FastEthernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,93,99
 no shutdown

interface FastEthernet0/14
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,93,99
 no shutdown

! Routed Interface to R-EDGE
interface GigabitEthernet0/1
 no switchport
 ip address 10.0.0.6 255.255.255.252
 no shutdown

! Routed Interface to DHCP Server
interface FastEthernet0/3
 no switchport
 ip address 10.0.0.9 255.255.255.252
 no shutdown

! SVIs & HSRP
interface Vlan10
 ip address 192.168.10.3 255.255.255.0
 ip helper-address 10.0.0.10
 standby 10 ip 192.168.10.1
 standby 10 priority 100
 no shutdown

interface Vlan20
 ip address 172.16.20.3 255.255.255.0
 ip helper-address 10.0.0.10
 standby 20 ip 172.16.20.1
 standby 20 priority 100
 no shutdown

interface Vlan93
 ip address 172.20.0.3 255.255.255.240
 ip helper-address 10.0.0.10
 standby 93 ip 172.20.0.1
 standby 93 priority 100
 no shutdown

interface Vlan99
 ip address 10.0.0.14 255.255.255.240
 no shutdown

! Routing Protocol
router ospf 1
 router-id 2.2.2.2
 network 10.0.0.4 0.0.0.3 area 0
 network 10.0.0.8 0.0.0.3 area 0
 network 192.168.10.0 0.0.0.255 area 0
 network 172.16.20.0 0.0.0.255 area 0
 network 172.20.0.0 0.0.0.15 area 0
exit


```

###### 5. R-EDGE (Border Router, NAT & ACL)

```cisconetwork
enable
configure terminal
hostname R-EDGE

! Internal Links
interface GigabitEthernet0/0
 description LINK_TO_SW-DIST1
 ip address 10.0.0.1 255.255.255.252
 ip nat inside
 no shutdown

interface GigabitEthernet0/1
 description LINK_TO_SW-DIST2
 ip address 10.0.0.5 255.255.255.252
 ip nat inside
 no shutdown

! External Link to ISP
interface GigabitEthernet0/2
 description WAN_TO_ISP
 ip address 203.0.113.2 255.255.255.252
 ip nat outside
 no shutdown

! Dynamic Routing (OSPF)
router ospf 1
 router-id 3.3.3.3
 network 10.0.0.0 0.0.0.3 area 0
 network 10.0.0.4 0.0.0.3 area 0
 default-information originate
exit

! Static Default Route to ISP
ip route 0.0.0.0 0.0.0.0 203.0.113.1

! ACL for NAT Eligibility
ip access-list standard NAT_ACL
 permit 192.168.10.0 0.0.0.255
 permit 172.16.20.0 0.0.0.255
 permit 172.20.0.0 0.0.0.15
exit

! Security ACL (Example: Restrict External Access to Internal Subnets)
ip access-list extended SECURE_INBOUND
 permit ospf any any
 deny ip any 192.168.10.0 0.0.0.255
 deny ip any 172.16.20.0 0.0.0.255
 deny ip any 172.20.0.0 0.0.0.15
 permit ip any any
exit

interface GigabitEthernet0/2
 ip access-group SECURE_INBOUND in
exit

! NAT Overload (PAT)
ip nat inside source list NAT_ACL interface GigabitEthernet0/2 overload


```

###### 6. R-DHCP (Central Server)

```cisconetwork
enable
configure terminal
hostname R-DHCP

interface GigabitEthernet0/0
 ip address 10.0.0.10 255.255.255.252
 no shutdown

! Static Route back to Internal Subnets via SW-DIST2
ip route 0.0.0.0 0.0.0.0 10.0.0.9

! Excluded Ranges
ip dhcp excluded-address 192.168.10.1 192.168.10.12
ip dhcp excluded-address 172.16.20.1 172.16.20.12
ip dhcp excluded-address 172.20.0.1 172.20.0.10

! DHCP Pools
ip dhcp pool SALES_POOL
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 8.8.8.8

ip dhcp pool IT_ADMIN_POOL
 network 172.16.20.0 255.255.255.0
 default-router 172.16.20.1
 dns-server 8.8.8.8

ip dhcp pool MANAGEMENT_POOL
 network 172.20.0.0 255.255.255.240
 default-router 172.20.0.1
 dns-server 8.8.8.8


```

---

##### Verification & Troubleshooting Processes

1. **VLANs & Trunking:**
* show vlan brief: Ensures VLANs exist on access switches.


* show interfaces trunk: Validates native VLAN match (VLAN 99) and verifies allowed VLAN lists across switch links.




2. **STP & EtherChannel:**
* show spanning-tree vlan : Confirms Root Bridge election and blocking/forwarding port states.


* show etherchannel summary: Verifies operational state (SU for Layer 2 in-use; flags P for operational bundled ports).




3. **OSPF Routing & Reachability:**
* show ip ospf neighbor: Validates full neighbor adjacency states (FULL/DR, FULL/BDR, or FULL/DROTHER).


* show ip route: Confirms route propagation for all LAN and WAN segments.




4. **HSRP Redundancy:**
* show standby brief: Verifies Active and Standby role allocations and Virtual IP assignment.




5. **DHCP & NAT Overload:**
* show ip dhcp binding: Lists dynamically leased client IP addresses.


* show ip nat translations: Displays active address and port translations passing through the border router.