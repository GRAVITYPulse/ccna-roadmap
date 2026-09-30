
## CCNA Complete Lab Solution Notes

Comprehensive configuration guide covering VLANs, Trunking, EtherChannel, STP, HSRP, OSPF, DHCP, NAT/PAT, Port Security and end-to-end verification.

---

### Reference Interface Map

| Device | Interface | Connected To | Remote Interface | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| R1 | g0/0 | WWW / ISP | g0/0 | Internet / NAT outside |
| R1 | g0/1 | DSW1 | g0/1 | Layer 3 transit |
| R1 | g0/2 | DSW2 | g0/1 | Layer 3 transit |
| DSW1 | fa0/2 | DSW2 | fa0/2 | LACP member |
| DSW1 | fa0/3 | DSW2 | fa0/3 | LACP member |
| DSW1 | fa0/4 | ASW3 | fa0/4 | 802.1Q trunk |
| DSW1 | fa0/5 | ASW4 | fa0/5 | 802.1Q trunk |
| DSW1 | g0/1 | R1 | g0/1 | Layer 3 transit |
| DSW2 | fa0/2 | DSW1 | fa0/2 | LACP member |
| DSW2 | fa0/3 | DSW1 | fa0/3 | LACP member |
| DSW2 | fa0/5 | ASW3 | fa0/5 | 802.1Q trunk |
| DSW2 | fa0/4 | ASW4 | fa0/4 | 802.1Q trunk |
| DSW2 | g0/1 | R1 | g0/2 | Layer 3 transit |
| ASW3 | g0/0 | DSW1 | g0/0 | 802.1Q trunk |
| ASW3 | fa0/5 | DSW2 | fa0/5 | 802.1Q trunk |
| ASW3 | fa0/23 | Engineering1 | eth0 | VLAN 10 access |
| ASW3 | fa0/24 | Sales1 | eth0 | VLAN 20 access |
| ASW4 | fa0/4 | DSW2 | fa0/4 | 802.1Q trunk |
| ASW4 | fa0/5 | DSW1 | fa0/5 | 802.1Q trunk |
| ASW4 | fa0/23 | Engineering2 | eth0 | VLAN 10 access |
| ASW4 | fa0/24 | Sales2 | eth0 | VLAN 20 access |

---

### VLSM and Addressing Solution

| Purpose | Network | Prefix | Mask | First Usable | Last Usable | Broadcast |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Engineering | 192.168.100.0 | /25 | 255.255.255.128 | 192.168.100.1 | 192.168.100.126 | 192.168.100.127 |
| Sales | 192.168.100.128 | /26 | 255.255.255.192 | 192.168.100.129 | 192.168.100.190 | 192.168.100.191 |
| Management | 192.168.100.192 | /27 | 255.255.255.224 | 192.168.100.193 | 192.168.100.222 | 192.168.100.223 |
| R1-DSW1 | 192.168.100.224 | /30 | 255.255.255.252 | 192.168.100.225 | 192.168.100.226 | 192.168.100.227 |
| R1-DSW2 | 192.168.100.228 | /30 | 255.255.255.252 | 192.168.100.229 | 192.168.100.230 | 192.168.100.231 |

---

### Key IP Address Assignments

| Function / Device | IPv4 Address |
| :--- | :--- |
| Engineering HSRP VIP | 192.168.100.1/25 |
| DSW1 VLAN 10 | 192.168.100.2/25 |
| DSW2 VLAN 10 | 192.168.100.3/25 |
| Sales HSRP VIP | 192.168.100.129/26 |
| DSW1 VLAN 20 | 192.168.100.130/26 |
| DSW2 VLAN 20 | 192.168.100.131/26 |
| Management HSRP VIP | 192.168.100.193/27 |
| DSW1 VLAN 99 | 192.168.100.194/27 |
| DSW2 VLAN 99 | 192.168.100.195/27 |
| ASW3 VLAN 99 | 192.168.100.196/27 |
| ASW4 VLAN 99 | 192.168.100.197/27 |
| R1 g0/1 | 192.168.100.225/30 |
| DSW1 g0/1 | 192.168.100.226/30 |
| R1 g0/2 | 192.168.100.229/30 |
| DSW2 g0/2 | 192.168.100.230/30 |
| ISP / WWW gateway | 203.0.113.1/30 |
| R1 g0/0 | 203.0.113.2/30 |

---

### Challenge 1 — Basic Global Configuration
These settings give every device a consistent baseline, protect privileged access, prevent accidental DNS lookups, and enable secure remote management.

**Commands (apply on all devices):**
```cisconetconf
enable
configure terminal
hostname <DEVICE-NAME>
no ip domain-lookup
enable secret cisco
username admin privilege 15 secret cisco
service password-encryption
banner motd #AUTHORIZED ACCESS ONLY#
ip domain-name cisco.local
crypto key generate rsa modulus
2048
ip ssh version 2
line console 0
 logging synchronous
 exec-timeout 60 0
 login local
exit
line vty 0 15
 login local
 transport input ssh
 exec-timeout 60 0
exit
end
write memory


```

**Verify:** `show running-config` | `show ip ssh` | `show user`

---

### Challenge 2 — Secure VTY Access with an ACL

SSH encrypts the session, while the VTY ACL limits which source networks are allowed to manage the devices remotely. Typically only the IT/network team (and management servers) should have SSH access.

```cisconetconf
configure terminal
ip access-list standard VTY-SSH
 permit 192.168.100.0 0.0.0.127
 permit 192.168.100.192 0.0.0.31
 deny any
exit
line vty 0 15
 access-class VTY-SSH in
 transport input ssh
 login local
exit


```

**Verify:** `show access-lists VTY-SSH` | `show running-config | section line vty`

---

### Challenge 3 — Create VLANs

VLANs divide the switched network into separate Layer 2 broadcast domains and map users to the correct IP subnets. Configure on DSW1, DSW2, ASW3, and ASW4.

```cisconetconf
configure terminal
vlan 10
 name ENGINEERING
exit
vlan 20
 name SALES
exit
vlan 99
 name MANAGEMENT
exit
end


```

**Verify:** `show vlan brief` | `show spanning-tree`

---

### Challenge 4 — Configure Client Access Ports

Access ports place each endpoint into exactly one VLAN. No 802.1Q tag is sent to the client.

```cisconetconf
! ASW3
interface f0/23
 description ENGINEERING1
 switchport mode access
 switchport access vlan 10
 no shutdown
exit
interface f0/24
 description SALES1
 switchport mode access
 switchport access vlan 20
 no shutdown
exit

! ASW4
interface f0/23
 description ENGINEERING2
 switchport mode access
 switchport access vlan 10
 no shutdown
exit
interface f0/24
 description SALES2
 switchport mode access
 switchport access vlan 20
 no shutdown
exit


```

**Verify:** `show vlan brief` | `show interfaces status` | `show spanning-tree vlan 10`

---

### Challenge 5 — Configure Access-Switch Management

The management SVI gives each Layer 2 access switch an IP presence. A default gateway is required to reach administrators outside VLAN 99.

> **IMPORTANT:** If you enable `ip routing`, the `ip default-gateway` command has no effect. Order of operations: first configure the default route, then enable IP routing.

```cisconetconf
! ASW3
interface vlan 99
 ip address 192.168.100.196 255.255.255.224
 no shutdown
exit
ip default-gateway 192.168.100.193

! ASW4
interface vlan 99
 ip address 192.168.100.197 255.255.255.224
 no shutdown
exit
ip default-gateway 192.168.100.193


```

**Verify:** `show ip interface brief` | `show running-config | include default-gateway`

---

### Challenge 6 — Configure 802.1Q Trunks

Trunks carry multiple VLANs between switches. Manual pruning (allowed VLAN list) keeps unnecessary VLAN traffic off links that do not need it.

```cisconetconf
! DSW1
interface f0/4
 description TRUNK_TO_ASW3
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 no shutdown
exit
interface f0/5
 description TRUNK_TO_ASW4
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 no shutdown
exit

! DSW2
interface f0/5
 description TRUNK_TO_ASW3
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 no shutdown
exit
interface f0/4
 description TRUNK_TO_ASW4
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 no shutdown
exit

! ASW3
interface f0/4
 description TRUNK_TO_DSW1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 no shutdown
exit
interface f0/5
 description TRUNK_TO_DSW2
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 no shutdown
exit

! ASW4
interface f0/4
 description TRUNK_TO_DSW2
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 no shutdown
exit
interface f0/5
 description TRUNK_TO_DSW1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 no shutdown
exit


```

**Verify:** `show interfaces trunk` | `show interfaces switchport`

---

### Challenge 7 — Build the LACP EtherChannel

LACP (IEEE 802.3ad) provides link aggregation and resiliency between the distribution switches. Use *active* mode because the requirement asks for the IEEE standard (not Cisco proprietary PAgP).

```cisconetconf
! DSW1
interface range f0/2 - 3
 description LACP_TO_DSW2
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 channel-group 1 mode active
 no shutdown
exit
interface port-channel 1
 description LACP_TRUNK_TO_DSW2
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
exit

! DSW2
interface range f0/2 - 3
 description LACP_TO_DSW1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
 channel-group 1 mode active
 no shutdown
exit
interface port-channel 1
 description LACP_TRUNK_TO_DSW1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
exit


```

**Verify:** `show etherchannel summary` | `show interfaces port-channel 1` | `show etherchannel load-balance`

---

### Challenge 8 — Enable LLDP and Verify Neighbors

CDP is Cisco proprietary; LLDP is the vendor-neutral standard and is useful in mixed-vendor networks. Many modern features (including some PoE behaviors) rely on LLDP.

```cisconetconf
configure terminal
lldp run
end


```

**Verify:** `show cdp neighbors` | `show lldp neighbors` | `show lldp neighbors detail`

---

### Challenge 9 — Optimize Spanning Tree

Aligning the STP root with the HSRP active gateway keeps Layer 2 forwarding efficient: Engineering prefers DSW1, while Sales prefers DSW2.

```cisconetconf
! All switches
spanning-tree mode rapid-pvst

! DSW1
spanning-tree vlan 10 root primary
spanning-tree vlan 20 root secondary

! DSW2
spanning-tree vlan 20 root primary
spanning-tree vlan 10 root secondary


```

**Verify:** `show spanning-tree vlan 10` | `show spanning-tree vlan 20` | `show spanning-tree root`

---

### Challenge 10 — Apply PortFast and BPDU Guard

PortFast gives end hosts immediate forwarding. BPDU Guard protects the topology if a switch is accidentally connected where a client should be.

```cisconetconf
! Global (recommended)
spanning-tree portfast default
spanning-tree portfast bpduguard default

! Or per-interface on ASW3 / ASW4
interface range f0/23-24
 spanning-tree portfast
 spanning-tree bpduguard enable
exit


```

**Verify:** `show spanning-tree summary` | `show spanning-tree interface e1/1 detail`

---

### Challenge 11 — Enable Multilayer Switching and Create SVIs

The distribution switches route between VLANs using SVIs. `ip routing` turns the switch into a Layer 3 forwarding device.

```cisconetconf
! DSW1
ip routing
interface vlan 10
 ip address 192.168.100.2 255.255.255.128
 no shutdown
exit
interface vlan 20
 ip address 192.168.100.130 255.255.255.192
 no shutdown
exit
interface vlan 99
 ip address 192.168.100.194 255.255.255.224
 no shutdown
exit

! DSW2
ip routing
interface vlan 10
 ip address 192.168.100.3 255.255.255.128
 no shutdown
exit
interface vlan 20
 ip address 192.168.100.131 255.255.255.192
 no shutdown
exit
interface vlan 99
 ip address 192.168.100.195 255.255.255.224
 no shutdown
exit


```

**Verify:** `show ip interface brief` *(SVI must be up/up — VLAN must be active on a trunk)*

---

### Challenge 12 — Configure HSRP

HSRP gives clients a virtual default gateway that survives the loss of one distribution switch. Preemption lets the preferred switch reclaim its role after recovery.

```cisconetconf
! DSW1 - VLAN 10 Active / VLAN 20 Standby / VLAN 99 Preferred
interface vlan 10
 standby 10 ip 192.168.100.1
 standby 10 priority 110
 standby 10 preempt
exit
interface vlan 20
 standby 20 ip 192.168.100.129
 standby 20 priority 100
 standby 20 preempt
exit
interface vlan 99
 standby 99 ip 192.168.100.193
 standby 99 priority 110
 standby 99 preempt
exit

! DSW2 - VLAN 10 Standby / VLAN 20 Active / VLAN 99 Standby
interface vlan 10
 standby 10 ip 192.168.100.1
 standby 10 priority 100
 standby 10 preempt
exit
interface vlan 20
 standby 20 ip 192.168.100.129
 standby 20 priority 110
 standby 20 preempt
exit
interface vlan 99
 standby 99 ip 192.168.100.193
 standby 99 priority 100
 standby 99 preempt
exit


```

**Verify:** `show standby brief` | `show standby 10`

---

### Challenge 13 — Configure the Layer 3 Transit Links

These are routed point-to-point links. The distribution-facing interfaces must be Layer 3 (use *no switchport* on multilayer switches).

```cisconetconf
! R1
interface g0/1
 description L3_TO_DSW1
 ip address 192.168.100.225 255.255.255.252
 no shutdown
exit
interface g0/2
 description L3_TO_DSW2
 ip address 192.168.100.229 255.255.255.252
 no shutdown
exit

! DSW1
interface g0/1
 description L3_TO_R1
 no switchport
 ip address 192.168.100.226 255.255.255.252
 no shutdown
exit

! DSW2
interface g0/1
 description L3_TO_R1
 no switchport
 ip address 192.168.100.230 255.255.255.252
 no shutdown
exit


```

**Verify:** `show ip interface brief` | *From R1:* `ping 192.168.100.226` / `192.168.100.230`

---

### Challenge 14 — Configure DHCP on R1 and DHCP Relay

DHCP centralizes client addressing. Because DHCP Discover is a broadcast, the SVIs relay requests to R1 with *ip helper-address*.

```cisconetconf
! R1 - exclude addresses first, then create pools
ip dhcp excluded-address 192.168.100.1 192.168.100.3
ip dhcp excluded-address 192.168.100.129 192.168.100.131
ip dhcp pool ENGINEERING
 network 192.168.100.0 255.255.255.128
 default-router 192.168.100.1
 dns-server 8.8.8.8
exit
ip dhcp pool SALES
 network 192.168.100.128 255.255.255.192
 default-router 192.168.100.129
 dns-server 8.8.8.8
exit

! DSW1 relay
interface vlan 10
 ip helper-address 192.168.100.225
exit
interface vlan 20
 ip helper-address 192.168.100.225
exit

! DSW2 relay
interface vlan 10
 ip helper-address 192.168.100.229
exit
interface vlan 20
 ip helper-address 192.168.100.229
exit


```

**Verify:** `show ip dhcp binding` | `show ip dhcp pool`

---

### Challenge 15 — Configure OSPF

R1 forms one OSPF adjacency with each distribution switch. Use passive-interface default on the distribution switches so hellos are sent only on the transit links.

```cisconetconf
! R1
router ospf 1
 router-id 1.1.1.1
 network 192.168.100.224 0.0.0.3 area 0
 network 192.168.100.228 0.0.0.3 area 0
exit
interface g0/1
 ip ospf network point-to-point
exit
interface g0/2
 ip ospf network point-to-point
exit

! DSW1
router ospf 1
 router-id 2.2.2.2
 passive-interface default
 no passive-interface g0/1
 network 192.168.100.0 0.0.0.127 area 0
 network 192.168.100.128 0.0.0.63 area 0
 network 192.168.100.192 0.0.0.31 area 0
 network 192.168.100.224 0.0.0.3 area 0
exit
interface g0/1
 ip ospf network point-to-point
exit

! DSW2
router ospf 1
 router-id 3.3.3.3
 passive-interface default
 no passive-interface g0/1
 network 192.168.100.0 0.0.0.127 area 0
 network 192.168.100.128 0.0.0.63 area 0
 network 192.168.100.192 0.0.0.31 area 0
 network 192.168.100.228 0.0.0.3 area 0
exit
interface g0/1
 ip ospf network point-to-point
exit


```

**Verify:** `show ip ospf neighbor` | `show ip ospf interface` | `show ip protocols`

---

### Challenge 19 — Internet Interface and Default Route

R1 needs a route for all unknown destinations. The distribution switches learn this default dynamically through OSPF via *default-information originate*.

```cisconetconf
interface g0/0
 description INTERNET
 ip address 203.0.113.2 255.255.255.252
 no shutdown
exit
ip route 0.0.0.0 0.0.0.0 203.0.113.1
router ospf 1
 default-information originate
exit


```

**Verify:** `ping 203.0.113.1` | `show ip route` | *On DSW1/DSW2:* `show ip route 0.0.0.0`

---

### Challenge 20 — Configure NAT/PAT

PAT lets all private campus hosts share R1's single Internet-facing IPv4 address. Sessions remain distinguishable by transport-layer ports.

```cisconetconf
ip access-list standard NAT_INSIDE
 permit 192.168.100.0 0.0.0.127
 permit 192.168.100.128 0.0.0.63
 permit 192.168.100.192 0.0.0.31
exit
interface g0/1
 ip nat inside
exit
interface g0/2
 ip nat inside
exit
interface g0/0
 ip nat outside
exit
ip nat inside source list NAT_INSIDE interface g0/0 overload


```

**Verify:** `show ip nat translations` | `show ip nat statistics` | `show access-lists NAT_INSIDE`

> **Note:** The ISP router has no route back to the private addresses. PAT works because return traffic is destined to the public address 203.0.113.2 and the NAT table on R1 translates it back.

---

### Challenge 21 — Configure Port Security

Port security restricts each client interface to one learned endpoint. Sticky learning records the MAC address. Shutdown violation mode error-disables the port on violation.

```cisconetconf
! ASW3 and ASW4
int r fa0/23-24
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation shutdown
 spanning-tree portfast
 spanning-tree bpduguard enable
exit


```

**Verify:** `show port-security` | `show port-security interface e1/1` | `show port-security address`

> **Recovery from violation:** After removing the unauthorized device, use `shutdown` / `no shutdown` on the interface, or enable *errdisable recovery cause psecure-violation* with an interval.

---

### Failure & Redundancy Tests

#### HSRP Failover Test

```cisconetconf
! Simulate loss of Engineering gateway on DSW1
interface vlan 10
 shutdown

! Verify DSW2 becomes Active, then restore
interface vlan 10
 no shutdown


```

**Verify:** `show standby brief` | *From client:* `ping 192.168.100.1`

#### EtherChannel Failure Test

```cisconetconf
interface e0/2
 shutdown

! Restore after testing
interface e0/2
 no shutdown


```

**Verify:** `show etherchannel summary` | `show interfaces port-channel 1`

#### STP Redundant-Uplink Test

```cisconetconf
! Identify forwarding uplink with show spanning-tree, then shut it
interface e0/0
 shutdown
show spanning-tree vlan 10

! Restore
interface e0/0
 no shutdown


```

**Verify:** `show spanning-tree vlan 10` | `show spanning-tree vlan 20`

---

### Final End-to-End Verification Checklist

* **Engineering clients** receive addresses from the /25 DHCP pool and use 192.168.100.1 as gateway.
* **Sales clients** receive addresses from the /26 DHCP pool and use 192.168.100.129 as gateway.
* **DSW1** is STP root + HSRP Active for Engineering; **DSW2** is STP root + HSRP Active for Sales.
* Only R1-DSW1 and R1-DSW2 form OSPF neighbors.
* Transit links show OSPF network type `POINT_TO_POINT`.
* **DSW1** and **DSW2** learn a default route from R1 through OSPF.
* **R1** translates inside traffic to 203.0.113.2 using PAT.

#### Recommended Verification Commands:

```cisconetconf
show vlan brief
show interfaces trunk
show etherchannel summary
show spanning-tree vlan 10
show spanning-tree vlan 20
show cdp neighbors / show lldp neighbors
show standby brief
show ip dhcp binding
show ip route / show ip route ospf
show ip ospf neighbor
show ip ospf interface
show access-lists
show ip nat translations
show port-security


```

---

### Recommended Troubleshooting Flow

**Physical** $\rightarrow$ **Layer 2** $\rightarrow$ **VLAN** $\rightarrow$ **STP / EtherChannel** $\rightarrow$ **Layer 3** $\rightarrow$ **HSRP** $\rightarrow$ **DHCP** $\rightarrow$ **Routing** $\rightarrow$ **ACL** $\rightarrow$ **NAT**

---

## Detailed Configuration Breakdown & Explanations

Below is a detailed breakdown explaining the purpose, mechanics, and design logic of every configuration challenge in this lab.

---

### Challenge 1: Basic Global Configuration

**Purpose:** Establishes a secure administrative baseline across all network devices (routers and switches).

* **`hostname <DEVICE-NAME>`**: Uniquely identifies the node in CLI prompts, system logs, and network monitoring tools.
* **`no ip domain-lookup`**: Disables automatic DNS resolution when mistyping a command in global or exec mode. Prevents terminal freeze while waiting for a non-existent DNS server to respond.
* **`enable secret cisco`**: Encrypts the enable password using strong hashing (MD5/SHA-256) to protect privileged EXEC mode.
* **`username admin privilege 15 secret cisco`**: Creates a local administrator account with full privileges (level 15) for local authentication.
* **`service password-encryption`**: Encrypts legacy plain-text passwords stored in the running configuration file.
* **`banner motd #AUTHORIZED ACCESS ONLY#`**: Displays a legal warning banner prior to login to notify unauthorized users.
* **`ip domain-name cisco.local` & `crypto key generate rsa modulus 2048**`: Sets the domain name needed to generate RSA key pairs required for secure SSH connections. A 2048-bit key length ensures robust encryption.
* **`ip ssh version 2`**: Forces SSH to use version 2, disabling vulnerable SSHv1.
* **`line console 0` & `line vty 0 15`**:
* **`logging synchronous`**: Prevents syslog notifications from breaking up CLI command input lines.
* **`exec-timeout 60 0`**: Automatically logs out inactive sessions after 60 minutes.
* **`login local`**: Enforces user authentication against the local local database.
* **`transport input ssh`**: Restricts incoming VTY connections exclusively to encrypted SSH sessions, blocking unencrypted Telnet.



---

### Challenge 2: Secure VTY Access with an ACL

**Purpose:** Implements Layer 3 access controls to restrict management access (SSH) to authorized administrative networks only.

* **`ip access-list standard VTY-SSH`**: Creates a named standard access list.
* **`permit 192.168.100.0 0.0.0.127`**: Permits SSH traffic originating from the Engineering subnet (`192.168.100.0/25`).
* **`permit 192.168.100.192 0.0.0.31`**: Permits SSH traffic originating from the Management subnet (`192.168.100.192/27`).
* **`deny any`**: Explicitly drops all other incoming SSH management attempts.


* **`access-class VTY-SSH in`**: Applies the standard access list to incoming VTY lines, restricting remote management connections at the control plane level.

---

### Challenge 3: Create VLANs

**Purpose:** Segregates a single physical Layer 2 infrastructure into isolated broadcast domains to improve network performance, security, and administration.

* **`vlan 10`, `vlan 20`, `vlan 99**`: Instantiates local VLAN database IDs.
* **`name ENGINEERING`, `name SALES`, `name MANAGEMENT**`: Assigns descriptive tags to each VLAN to identify functional department usage.

---

### Challenge 4: Configure Client Access Ports

**Purpose:** Connects end-user computers to the switch network and places them in their dedicated department VLANs.

* **`switchport mode access`**: Configures the interface to operate in access mode, intended for end-user devices (non-trunking).
* **`switchport access vlan <10|20>`**: Statically assigns untagged traffic from the attached endpoint to the designated VLAN.

---

### Challenge 5: Configure Access-Switch Management

**Purpose:** Provides Layer 2 access switches with IP connectivity so they can be managed remotely via SSH across subnets.

* **`interface vlan 99` & `ip address 192.168.100.x 255.255.255.224**`: Configures the Switch Virtual Interface (SVI) on Management VLAN 99, giving the switch its own IP address.
* **`ip default-gateway 192.168.100.193`**: Defines the default gateway for Layer 2 switches (which lack routing tables) so management traffic can return to remote administrators residing outside VLAN 99.

---

### Challenge 6: Configure 802.1Q Trunks

**Purpose:** Enables inter-switch links to carry multi-VLAN traffic across the network using standard IEEE 802.1Q tagging.

* **`switchport mode trunk`**: Forces the port into 802.1Q trunking mode.
* **`switchport trunk allowed vlan 10,20,99`**: Implements VLAN pruning, restricting link bandwidth to necessary VLANs (10, 20, and 99) and blocking unnecessary broadcast traffic.

---

### Challenge 7: Build the LACP EtherChannel

**Purpose:** Combines multiple physical interfaces between distribution switches into a single logical link to increase bandwidth and provide link redundancy.

* **`channel-group 1 mode active`**: Configures the ports to negotiate an IEEE 802.3ad Link Aggregation Control Protocol (LACP) EtherChannel dynamically.
* **`interface port-channel 1`**: Applies global trunk configurations to the logical EtherChannel bundle, ensuring interface parameters remain consistent.

---

### Challenge 8: Enable LLDP

**Purpose:** Replaces proprietary protocols with Link Layer Discovery Protocol (LLDP) to discover directly connected neighbors in vendor-neutral environments.

* **`lldp run`**: Enables global LLDP processing, allowing devices to transmit and receive neighbor discovery advertisements.

---

### Challenge 9: Optimize Spanning Tree

**Purpose:** Ensures STP prevents Layer 2 loops while aligning active Spanning Tree root bridges with HSRP active routers for optimal traffic routing.

* **`spanning-tree mode rapid-pvst`**: Enables Per-VLAN Rapid Spanning Tree Protocol (RSTP), accelerating convergence times after topology changes.
* **`spanning-tree vlan X root primary / secondary`**: Decreases the STP priority for specific VLANs on target distribution switches, guaranteeing deterministic traffic paths:
* **DSW1**: Primary root for Engineering (VLAN 10), Secondary for Sales (VLAN 20).
* **DSW2**: Primary root for Sales (VLAN 20), Secondary for Engineering (VLAN 10).



---

### Challenge 10: Apply PortFast and BPDU Guard

**Purpose:** Enhances edge port connectivity security and speeds up client connection initialization.

* **`spanning-tree portfast`**: Transitions access interfaces directly to the STP Forwarding state, bypassing Listening/Learning states.
* **`spanning-tree bpduguard enable`**: Protects the network topology by immediately disabling (`err-disable`) an edge port if a switch sending BPDUs is connected to it.

---

### Challenge 11: Enable Multilayer Switching and SVIs

**Purpose:** Converts distribution switches into Layer 3 routing nodes that route packets between local VLANs.

* **`ip routing`**: Activates IPv4 routing globally on multilayer switches.
* **`interface vlan <10|20|99>`**: Creates default gateway SVIs for each internal VLAN, allowing routing between VLANs at wire speed.

---

### Challenge 12: Configure HSRP

**Purpose:** Uses Hot Standby Router Protocol (HSRP) to provide transparent default gateway redundancy for client subnets.

* **`standby <group> ip <VIP>`**: Configures the Virtual IP address shared by the active and standby routers, which clients use as their default gateway.
* **`standby <group> priority <110|100>`**: Determines gateway selection; the switch with higher priority (110) becomes the Active gateway for that VLAN.
* **`standby <group> preempt`**: Forces a recovered router with higher priority to resume the Active role immediately after a failure recovery.

---

### Challenge 13: Configure Layer 3 Transit Links

**Purpose:** Establishes routed point-to-point connections between distribution switches and the primary edge router.

* **`no switchport`**: Converts a physical switch port into a dedicated Layer 3 routed interface.
* **`/30 Subnets (`255.255.255.252`)**: Conserves IPv4 address space by allocating exactly two usable IP addresses per point-to-point transit link.

---

### Challenge 14: Configure DHCP on R1 and DHCP Relay

**Purpose:** Centralizes IP address assignment on router R1 and uses DHCP relays to forward requests across subnets.

* **`ip dhcp excluded-address`**: Prevents DHCP pools from assigning statically configured infrastructure addresses (SVI IPs, VIPs).
* **`ip dhcp pool`**: Defines dynamic client addressing parameters (network scope, default router, and DNS servers).
* **`ip helper-address <R1-IP>`**: Converts client broadcast DHCP Discover requests into unicast packets, forwarding them through Layer 3 boundaries to central server R1.

---

### Challenge 15: Configure OSPF

**Purpose:** Enables dynamic IPv4 routing using Open Shortest Path First (OSPF) to exchange subnets automatically between distribution switches and the edge router.

* **`router ospf 1` & `router-id x.x.x.x**`: Starts the OSPF process with a unique router ID.
* **`passive-interface default` & `no passive-interface g0/1**`: Prevents OSPF hello packets from being broadcast toward user access ports, restricting OSPF adjacencies strictly to transit links.
* **`ip ospf network point-to-point`**: Optimizes neighbor discovery on `/30` links by eliminating DR/BDR elections.

---

### Challenge 19: Internet Interface and Default Route

**Purpose:** Routes external traffic toward the Internet ISP gateway and advertises a default route internally.

* **`ip route 0.0.0.0 0.0.0.0 203.0.113.1`**: Creates a static default route directing all unknown destination traffic toward the ISP gateway.
* **`default-information originate`**: Automatically propagates the default route (`0.0.0.0/0`) via OSPF to internal distribution switches.

---

### Challenge 20: Configure NAT/PAT

**Purpose:** Translates internal private IP addresses (`192.168.100.0/24`) into a single public IP address using Port Address Translation (PAT).

* **`ip access-list standard NAT_INSIDE`**: Identifies local subnets allowed to be translated for Internet access.
* **`ip nat inside` / `ip nat outside**`: Defines internal and external NAT boundaries on interfaces.
* **`ip nat inside source list NAT_INSIDE interface g0/0 overload`**: Maps multiple internal IP addresses to the single public address assigned to interface `g0/0` using unique source port numbers.

---

### Challenge 21: Configure Port Security

**Purpose:** Secures physical access switch ports against unauthorized devices and MAC flooding attacks.

* **`switchport port-security`**: Enables port security features on the interface.
* **`switchport port-security maximum 1`**: Restricts the port to a single learned MAC address.
* **`switchport port-security mac-address sticky`**: Dynamically learns connected MAC addresses and saves them directly to the running configuration.
* **`switchport port-security violation shutdown`**: Places the interface into an `err-disable` state if an unauthorized MAC address attempts to communicate.

```

```
