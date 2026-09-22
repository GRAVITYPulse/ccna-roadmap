# ATTA NETWORK ACADEMY

## CCNA Lab Implementation Guide

This lab guide provides step-by-step instructions to design, configure, and verify an enterprise campus network infrastructure featuring high availability, dynamic routing, centralized addressing, security, and edge NAT/PAT connectivity.

---

### Reference Interface Map

| Device | Interface | Connected To | Remote Interface | Purpose |
| --- | --- | --- | --- | --- |
| R1 | e0/0 | WWW / ISP | e0/0 | Internet / NAT outside |
| R1 | e1/1 | DSW1 | e1/1 | Layer 3 transit |
| R1 | e1/2 | DSW2 | e1/2 | Layer 3 transit |
| DSW1 | e0/2 | DSW2 | e0/2 | LACP member |
| DSW1 | e0/3 | DSW2 | e0/3 | LACP member |
| DSW1 | e0/0 | ASW3 | e0/0 | 802.1Q trunk |
| DSW1 | e0/1 | ASW4 | e0/1 | 802.1Q trunk |
| DSW1 | e1/1 | R1 | e1/1 | Layer 3 transit |
| DSW2 | e0/2 | DSW1 | e0/2 | LACP member |
| DSW2 | e0/3 | DSW1 | e0/3 | LACP member |
| DSW2 | e0/1 | ASW3 | e0/1 | 802.1Q trunk |
| DSW2 | e0/0 | ASW4 | e0/0 | 802.1Q trunk |
| DSW2 | e1/2 | R1 | e1/2 | Layer 3 transit |
| ASW3 | e0/0 | DSW1 | e0/0 | 802.1Q trunk |
| ASW3 | e0/1 | DSW2 | e0/1 | 802.1Q trunk |
| ASW3 | e1/1 | Engineering1 | eth0 | VLAN 10 access |
| ASW3 | e1/2 | Sales1 | eth0 | VLAN 20 access |
| ASW4 | e0/0 | DSW2 | e0/0 | 802.1Q trunk |
| ASW4 | e0/1 | DSW1 | e0/1 | 802.1Q trunk |
| ASW4 | e1/1 | Engineering2 | eth0 | VLAN 10 access |
| ASW4 | e1/2 | Sales2 | eth0 | VLAN 20 access |

---

### VLSM and Addressing Plan

| Purpose | Network | Prefix | Mask | First Usable | Last Usable | Broadcast |
| --- | --- | --- | --- | --- | --- | --- |
| Engineering | 192.168.100.0 | /25 | 255.255.255.128 | 192.168.100.1 | 192.168.100.126 | 192.168.100.127 |
| Sales | 192.168.100.128 | /26 | 255.255.255.192 | 192.168.100.129 | 192.168.100.190 | 192.168.100.191 |
| Management | 192.168.100.192 | /27 | 255.255.255.224 | 192.168.100.193 | 192.168.100.222 | 192.168.100.223 |
| R1-DSW1 | 192.168.100.224 | /30 | 255.255.255.252 | 192.168.100.225 | 192.168.100.226 | 192.168.100.227 |
| R1-DSW2 | 192.168.100.228 | /30 | 255.255.255.252 | 192.168.100.229 | 192.168.100.230 | 192.168.100.231 |

---

### Key IP Address Assignments Reference

| Function / Device | IPv4 Address |
| --- | --- |
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
| R1 e1/1 | 192.168.100.225/30 |
| DSW1 e1/1 | 192.168.100.226/30 |
| R1 e1/2 | 192.168.100.229/30 |
| DSW2 e1/2 | 192.168.100.230/30 |
| ISP / WWW gateway | 203.0.113.1/30 |
| R1 e0/0 | 203.0.113.2/30 |

---

### Challenge 1 — Baseline and Secure System Configuration

Establish a standard security baseline on **all devices** (R1, DSW1, DSW2, ASW3, ASW4).

1. **Device Identification & Domain:** Set unique hostnames for each device matching the topology map, domain name to `cisco.local`, and disable automatic IP domain lookup to prevent CLI delays on typos.
2. **Access Security:** Secure privilege mode access using an encrypted secret `cisco`. Create a local administrator account named `admin` with full privilege level 15 and secret `cisco`. Enable global service password encryption.
3. **Banner Notice:** Add a Message-of-the-Day banner explicitly displaying `#AUTHORIZED ACCESS ONLY#`.
4. **SSH Encryption:** Generate RSA keys with a 2048-bit modulus size and enforce SSH Version 2 globally.
5. **Console & Remote Lines:**
* Configure the console line to use local authentication, set an execution timeout of 60 minutes, and enable synchronous logging to prevent prompt interruption.
* Configure VTY lines 0 through 15 to permit SSH connections only, use local login credentials, and set an execution timeout of 60 minutes.


6. **Save State:** Save running configurations to startup memory across all network equipment.

**Verification Tasks:**

* Check running configuration settings.
* Confirm SSH operational status and verify currently logged-in user accounts.

---

### Challenge 2 — Secure VTY Access via Standard ACL

Restrict administrative remote management access across all network equipment.

1. **Define Access Control:** Create a standard named access list named `VTY-SSH`.
2. **Configure Security Rules:**
* Explicitly allow access from the Engineering network subnet (`192.168.100.0/25`).
* Explicitly allow access from the Management network subnet (`192.168.100.192/27`).
* Explicitly deny and log all other network source attempts.


3. **Apply Enforcement:** Attach the access list inbound to all VTY lines (0 through 15) while maintaining local authentication and SSH protocol rules.

**Verification Tasks:**

* Verify active access list entries and match counts.
* Confirm proper association of the access list under line VTY configuration settings.

---

### Challenge 3 — Virtual LAN Setup

Isolate broad dynamic traffic into logical segments on **DSW1, DSW2, ASW3, and ASW4**.

1. **VLAN Provisioning:**
* Create **VLAN 10** and assign the description `ENGINEERING`.
* Create **VLAN 20** and assign the description `SALES`.
* Create **VLAN 99** and assign the description `MANAGEMENT`.



**Verification Tasks:**

* Inspect brief VLAN summary tables to confirm named VLAN entries.
* Confirm Spanning Tree Protocol instances exist for newly generated VLANs.

---

### Challenge 4 — Client Access Switchport Assignments

Configure end-user access connectivity across access switches.

1. **ASW3 Port Assignment:**
* Set interface `e1/1` to static access mode, assign it to VLAN 10, add description `ENGINEERING1`, and ensure interface status is administrative up.
* Set interface `e1/2` to static access mode, assign it to VLAN 20, add description `SALES1`, and ensure interface status is administrative up.


2. **ASW4 Port Assignment:**
* Set interface `e1/1` to static access mode, assign it to VLAN 10, add description `ENGINEERING2`, and ensure interface status is administrative up.
* Set interface `e1/2` to static access mode, assign it to VLAN 20, add description `SALES2`, and ensure interface status is administrative up.



**Verification Tasks:**

* Validate VLAN interface assignment mappings.
* Check interface link statuses and operational states.
* Confirm Spanning Tree status specifically for VLAN 10 access links.

---

### Challenge 5 — Access Switch Management Interface

Assign network presence to Layer 2 access devices for remote administrative access.

1. **ASW3 Interface Assignment:**
* Enable Switch Virtual Interface (SVI) `vlan 99` with IP address `192.168.100.196` and mask `255.255.255.224`.
* Assign default gateway destination `192.168.100.193`.


2. **ASW4 Interface Assignment:**
* Enable SVI `vlan 99` with IP address `192.168.100.197` and mask `255.255.255.224`.
* Assign default gateway destination `192.168.100.193`.



> **Implementation Note:** Ensure global IP routing is kept disabled on pure Layer 2 access switches for the default gateway command to function as intended.

**Verification Tasks:**

* Display IP interface summary tables to confirm SVI status.
* Validate default gateway configuration entries in active running memory.

---

### Challenge 6 — 802.1Q Inter-Switch Trunking

Establish multi-VLAN trunk links carrying inter-switch traffic.

1. **DSW1 Trunk Interfaces:** Configure `e0/0` (facing ASW3) and `e0/1` (facing ASW4) as static 802.1Q trunk interfaces, explicitly restricting allowed transit traffic strictly to VLANs `10, 20, and 99`.
2. **DSW2 Trunk Interfaces:** Configure `e0/1` (facing ASW3) and `e0/0` (facing ASW4) as static 802.1Q trunk interfaces, explicitly restricting allowed transit traffic strictly to VLANs `10, 20, and 99`.
3. **ASW3 Trunk Interfaces:** Configure `e0/0` (facing DSW1) and `e0/1` (facing DSW2) as static 802.1Q trunk interfaces, explicitly restricting allowed transit traffic strictly to VLANs `10, 20, and 99`.
4. **ASW4 Trunk Interfaces:** Configure `e0/0` (facing DSW2) and `e0/1` (facing DSW1) as static 802.1Q trunk interfaces, explicitly restricting allowed transit traffic strictly to VLANs `10, 20, and 99`.

**Verification Tasks:**

* Confirm operational trunk interfaces and explicitly allowed active VLAN lists.
* Verify operational switchport modes across trunk interfaces.

---

### Challenge 7 — IEEE 802.3ad LACP EtherChannel

Aggregate redundant inter-switch links between distribution switches into a logical bundle.

1. **Physical & Logical Configuration (DSW1 & DSW2):**
* Bundle physical interfaces `e0/2` and `e0/3` into Channel Group 1 using standards-based LACP active negotiation mode.
* Configure physical interfaces as static trunks allowing VLANs `10, 20, and 99`.
* Define logical `port-channel 1` as a static trunk allowing VLANs `10, 20, and 99`.



**Verification Tasks:**

* Validate EtherChannel summary status to ensure flags indicate active bundled operation.
* Display detailed interface states for logical `port-channel 1`.
* Review configured frame load-balancing hashing methods.

---

### Challenge 8 — Vendor-Neutral Discovery (LLDP)

Enable standards-based neighbor discovery for mixed-vendor hardware visibility.

1. **Activation:** Enable Link Layer Discovery Protocol (LLDP) globally across all switches and routers.

**Verification Tasks:**

* Review adjacent devices using both Cisco Discovery Protocol (`CDP`) and standard Link Layer Discovery Protocol (`LLDP`) commands.
* Review extended detailed neighbor characteristics (system capability, port ID, IP address).

---

### Challenge 9 — Spanning Tree Optimization

Tune Spanning Tree Protocol (STP) parameters for optimal path selection and fast topology convergence.

1. **STP Mode:** Transition all active switching nodes (DSW1, DSW2, ASW3, ASW4) to use Rapid Per-VLAN Spanning Tree Plus (`rapid-pvst`).
2. **Root Bridge Alignment:**
* **DSW1:** Set as primary Root Bridge for VLAN 10 and secondary Root Bridge for VLAN 20.
* **DSW2:** Set as primary Root Bridge for VLAN 20 and secondary Root Bridge for VLAN 10.



**Verification Tasks:**

* Inspect STP root status and bridge priorities for VLAN 10 and VLAN 20.
* Confirm designated Root Bridge IDs and local root port statuses across instances.

---

### Challenge 10 — Access Edge Port Protection

Accelerate edge connectivity transitions while locking down unexpected switch connections.

1. **Edge Optimization:** Enable PortFast globally on access ports to bypass listening and learning states, and enable BPDU Guard globally or explicitly on end-user interfaces (`ASW3/ASW4 e1/1-2`) to error-disable interfaces upon receiving incoming BPDU frames.

**Verification Tasks:**

* Review global Spanning Tree summary settings for fast transitioning features.
* Inspect detail status for individual client-facing interfaces.

---

### Challenge 11 — Multilayer Inter-VLAN Routing

Enable core routing and establish gateway interfaces across distribution layers.

1. **Global Routing Initialization:** Enable global IPv4 routing on both DSW1 and DSW2.
2. **DSW1 Gateway SVIs:**
* **VLAN 10:** Assign IP address `192.168.100.2/25`.
* **VLAN 20:** Assign IP address `192.168.100.130/26`.
* **VLAN 99:** Assign IP address `192.168.100.194/27`.


3. **DSW2 Gateway SVIs:**
* **VLAN 10:** Assign IP address `192.168.100.3/25`.
* **VLAN 20:** Assign IP address `192.168.100.131/26`.
* **VLAN 99:** Assign IP address `192.168.100.195/27`.



**Verification Tasks:**

* Verify line and protocol status for all defined SVIs (ensure underlying VLANs exist and are active on trunk ports).

---

### Challenge 12 — First-Hop Redundancy Protocol (HSRP)

Establish gateway redundancy for access subnets aligning active traffic flow with STP Root bridges.

1. **DSW1 HSRP Parameters:**
* **VLAN 10 (Active):** Assign Virtual IP `192.168.100.1`, set priority to `110`, enable preemption.
* **VLAN 20 (Standby):** Assign Virtual IP `192.168.100.129`, set priority to `100`, enable preemption.
* **VLAN 99 (Active):** Assign Virtual IP `192.168.100.193`, set priority to `110`, enable preemption.


2. **DSW2 HSRP Parameters:**
* **VLAN 10 (Standby):** Assign Virtual IP `192.168.100.1`, set priority to `100`, enable preemption.
* **VLAN 20 (Active):** Assign Virtual IP `192.168.100.129`, set priority to `110`, enable preemption.
* **VLAN 99 (Standby):** Assign Virtual IP `192.168.100.193`, set priority to `100`, enable preemption.



**Verification Tasks:**

* Confirm HSRP active/standby state distribution using `show standby brief`.
* Inspect state transitions, timer intervals, and active gateway information.

---

### Challenge 13 — Layer 3 Point-to-Point Transit Links

Convert distribution-to-edge interfaces into routed point-to-point links.

1. **R1 Interface Configuration:**
* Interface `e1/1`: Assign IP address `192.168.100.225/30`, add description `L3_TO_DSW1`, and enable interface.
* Interface `e1/2`: Assign IP address `192.168.100.229/30`, add description `L3_TO_DSW2`, and enable interface.


2. **DSW1 Interface Configuration:**
* Interface `e1/1`: Remove switchport properties (`no switchport`), assign IP address `192.168.100.226/30`, add description `L3_TO_R1`, and enable interface.


3. **DSW2 Interface Configuration:**
* Interface `e1/2`: Remove switchport properties (`no switchport`), assign IP address `192.168.100.230/30`, add description `L3_TO_R1`, and enable interface.



**Verification Tasks:**

* Verify operational status using interface IP summaries.
* Confirm layer 3 point-to-point reachability by pinging adjacent transit endpoints from R1.

---

### Challenge 14 — Centralized DHCP and IP Helper Relay

Configure centralized IP addressing on R1 and relay dynamic requests across SVIs.

1. **R1 DHCP Server Engine:**
* Define address exclusions: Exclude `192.168.100.1` through `192.168.100.3` and `192.168.100.129` through `192.168.100.131`.
* Create `ENGINEERING` pool: Network `192.168.100.0/25`, default router `192.168.100.1`, DNS server `8.8.8.8`.
* Create `SALES` pool: Network `192.168.100.128/26`, default router `192.168.100.129`, DNS server `8.8.8.8`.


2. **DSW1 DHCP Relay:** Configure `ip helper-address 192.168.100.225` under VLAN 10 and VLAN 20 SVIs.
3. **DSW2 DHCP Relay:** Configure `ip helper-address 192.168.100.229` under VLAN 10 and VLAN 20 SVIs.

**Verification Tasks:**

* View dynamic DHCP bindings leasing history on R1.
* Inspect configured DHCP pool utilisation metrics.

---

### Challenge 15 — Dynamic OSPF Area 0 Routing

Form interior dynamic routing adjacencies to exchange internal reachability.

1. **R1 OSPF Instance:**
* Enable Process ID 1 with Router ID `1.1.1.1` in Area 0.
* Advertise transit links `192.168.100.224/30` and `192.168.100.228/30` into Area 0.
* Set interface network types to `point-to-point` on `e1/1` and `e1/2`.


2. **DSW1 OSPF Instance:**
* Enable Process ID 1 with Router ID `2.2.2.2` in Area 0.
* Configure global passive-interface default and suppress passive behavior on `e1/1` (`no passive-interface e1/1`).
* Network Advertisements: Include subnets `192.168.100.0/25`, `192.168.100.128/26`, `192.168.100.192/27`, and `192.168.100.224/30` in Area 0.
* Set interface network type to `point-to-point` on `e1/1`.


3. **DSW2 OSPF Instance:**
* Enable Process ID 1 with Router ID `3.3.3.3` in Area 0.
* Configure global passive-interface default and suppress passive behavior on `e1/2` (`no passive-interface e1/2`).
* Network Advertisements: Include subnets `192.168.100.0/25`, `192.168.100.128/26`, `192.168.100.192/27`, and `192.168.100.228/30` in Area 0.
* Set interface network type to `point-to-point` on `e1/2`.



**Verification Tasks:**

* Verify active OSPF neighbor adjacencies and ensure state reaches `FULL`.
* Check OSPF interface state types and protocol configuration details.

---

### Challenge 16 — Edge Gateway Route Propagation

Establish default WAN connectivity and dynamically originate default path information.

1. **R1 WAN Link Setup:** Configure interface `e0/0` with IP `203.0.113.2/30`, description `INTERNET`, and administrative status up.
2. **Static Gateway Path:** Add static IPv4 default route pointing all outbound traffic (`0.0.0.0/0`) to ISP gateway `203.0.113.1`.
3. **Dynamic Propagation:** Inject default route information into OSPF using `default-information originate` under OSPF Process 1.

**Verification Tasks:**

* Verify WAN path connectivity by pinging Next-Hop gateway `203.0.113.1`.
* Validate routing table details on R1 and ensure DSW1/DSW2 dynamically learn `0.0.0.0/0` via OSPF.

---

### Challenge 17 — Port Address Translation (PAT)

Configure overloaded NAT on R1 allowing private network access to the internet.

1. **Define Translation Sources:** Create standard Access List `NAT_INSIDE` permitting subnets `192.168.100.0/25` (Engineering), `192.168.100.128/26` (Sales), and `192.168.100.192/27` (Management).
2. **Assign Interface Roles:** Set interfaces `e1/1` and `e1/2` as NAT inside interfaces. Set interface `e0/0` as NAT outside interface.
3. **Configure Translation Rule:** Enable dynamic NAT inside source translation matching list `NAT_INSIDE` to interface `e0/0` using `overload`.

**Verification Tasks:**

* Inspect operational active NAT translation tables.
* Review NAT operational statistics and match counters on access control rules.

---

### Challenge 18 — Port Security Enforcement

Lock down client edge access switch ports to explicit single device identities.

1. **Edge Lockdown (ASW3 & ASW4 Interfaces `e1/1 - 2`):**
* Configure interface access operation, enable port security, set maximum allowed addresses to `1`, enable sticky learning mode, and set security violation mode to `shutdown`.
* Ensure PortFast and BPDU Guard enforcement remain active.



**Verification Tasks:**

* Review port security status globally and per interface.
* Verify dynamically stored sticky MAC address entries.

---

### Failure Validation & Resiliency Drills

#### Drill A — Gateway Redundancy (HSRP Failover)

1. **Simulate Outage:** Administrative shutdown of SVI `vlan 10` on primary active node DSW1.
2. **Observe Failover:** Verify standby node DSW2 transitions to Active state for VLAN 10. Ensure continuous active ping reachability from client endpoints to VIP `192.168.100.1`.
3. **Recovery:** Administrative enable (`no shutdown`) of SVI `vlan 10` on DSW1 and confirm preemption restores primary active ownership.

#### Drill B — Link Aggregation Resilience (EtherChannel)

1. **Simulate Outage:** Administrative shutdown of individual physical member interface `e0/2` on DSW1/DSW2.
2. **Observe Failover:** Verify logical `port-channel 1` maintains bundle operational status via remaining active member `e0/3`.
3. **Recovery:** Administrative enable (`no shutdown`) interface `e0/2` and verify complete LACP re-bundling.

#### Drill C — Spanning Tree Uplink Convergence

1. **Simulate Outage:** Determine forwarding trunk link interface using STP queries, then execute administrative shutdown on that interface.
2. **Observe Failover:** Confirm Rapid PVST+ transitions redundant blocked uplinks into active forwarding state without long outages.
3. **Recovery:** Re-enable disabled uplink and verify standard baseline path convergence.

---

### End-to-End Verification Runbook

Validate overall system deployment against the following key criteria:

* **Client Addressing:** Engineering endpoints lease addresses from the `/25` pool with gateway `192.168.100.1`; Sales endpoints lease addresses from the `/26` pool with gateway `192.168.100.129`.
* **Topology Balance:** DSW1 functions as STP Root and HSRP Active node for Engineering; DSW2 functions as STP Root and HSRP Active node for Sales.
* **Routing Topology:** OSPF adjacencies form exclusively across transit links between R1-DSW1 and R1-DSW2 using Point-to-Point link settings. Distribution switches dynamically receive `0.0.0.0/0` defaults.
* **Edge Translation:** Internal private subnets translate to `203.0.113.2` via overloaded PAT when reaching external interfaces.

#### Consolidated Diagnostic Command List:

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

### Troubleshooting Decision Path

When diagnosing network faults, systematically isolate issues layer-by-layer:

$$\text{Physical} \longrightarrow \text{Layer 2} \longrightarrow \text{VLAN} \longrightarrow \text{STP / EtherChannel} \longrightarrow \text{Layer 3} \longrightarrow \text{HSRP} \longrightarrow \text{DHCP} \longrightarrow \text{Routing} \longrightarrow \text{ACL} \longrightarrow \text{NAT}$$