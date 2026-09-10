# Enterprise Network Topology: Routing, Switching & Security Defense Guide

This document provides a comprehensive defense breakdown of the routing protocols, switching mechanisms, security policies, and physical topology links based on the updated infrastructure design.

---

## Global System & Management Configuration

* **`hostname <NAME>`**
  Modifies the CLI prompt to uniquely identify each device in the network hierarchy (`R-ISP`, `R-EDGE`, `R-CORE1`, `R-CORE2`, `SW-DIST1`, `SW-DIST2`, `SW-ACCESS1`, `SW-ACCESS2`).
* **`no ip domain-lookup`**
  Disables DNS name resolution on the device CLI to prevent CLI command line hangs when typing incorrect commands.
* **`username admin privilege 15 secret <password>`**
  Creates an administrative account with privilege level 15 protected by strong cryptographic password hashing.
* **Line Security (`line con 0` & `line vty 0 4`)**
  * **`logging synchronous`**: Keeps system notifications from interrupting active console or remote terminal typing.
  * **`login local`**: Enforces authentication using the local account database for console and remote VTY connections.

---

## 1. R-ISP (Simulated Internet Provider)

### Role & Connections
* **Role:** Represents the public external Internet edge outside the private enterprise domain.
* **Physical Link:** `Gig0/0` (`203.0.113.1/30`) connects directly to `R-EDGE` (`Gig0/2` - `203.0.113.2/30`).
* **`interface Loopback0` (`8.8.8.8/32`):** Serves as an off-network, virtual operational target for ping and path verification tests.

---

## 2. R-EDGE (Enterprise Edge & NAT Gateway)

### Role & Connections
* **Role:** Links private enterprise subnets to the public Internet, performing network address translation and edge default routing.
* **Physical Links:**
  * `Gig0/2` (`203.0.113.2/30`) facing `R-ISP` (`Gig0/0`).
  * `Gig0/1` (`10.0.0.1/30`) facing `R-CORE1` (`Gig0/1` - `.2`).
  * `Gig0/0` (`10.0.0.5/30`) facing `R-CORE2` (`Gig0/0` - `.6`).

### Routing & NAT Mechanics
* **`ip nat inside` / `ip nat outside`**: Identifies internal interfaces (`Gig0/0`, `Gig0/1`) as the inside private zone and `Gig0/2` as the outside public zone.
* **`ip access-list standard NAT-ACL`**: Identifies authorized private source subnets (`192.168.10.0/24`, `172.16.20.0/24`, `172.20.0.0/28`).
* **`ip nat inside source list NAT-ACL interface Gig0/2 overload`**: Implements **Port Address Translation (PAT)**, dynamically mapping private IP addresses to single public IP `203.0.113.2` using L4 source ports.
* **`ip route 0.0.0.0 0.0.0.0 203.0.113.1`**: Static default route sending all unknown/external traffic toward the ISP.
* **`default-information originate` (OSPF)**: Injects the static default route into the internal OSPF domain for core routers.

---

## 3. R-CORE1 & R-CORE2 (OSPF Core & Inter-VLAN Routing)

### Role & Core-to-Distribution Links
* **Role:** Layer 3 core handling internal routing, redundant paths, inter-VLAN default gateways, and stateful access control filtering.
* **Inter-Core Link:** `R-CORE1` (`Gig0/0` - `10.0.0.9/30`) connects directly to `R-CORE2` (`Gig0/1` - `10.0.0.10/30`).
* **Core-to-Distribution Links:**
  * `R-CORE1` `Gig0/2` (`10.0.0.13/30`) connects to `SW-DIST1` `Gig0/1`.
  * `R-CORE2` `Gig0/2` (`10.0.0.14/30`) connects to `SW-DIST2` `Gig0/1`.

### Routing Concepts
* **`router ospf 1` & `router-id <x.x.x.x>`**: Initializes OSPF process `1` using explicit Router IDs (`1.1.1.1`, `2.2.2.2`, `3.3.3.3`) for link-state stability.
* **`network <subnet> <wildcard> area 0`**: Advertises `/30` point-to-point transit subnets into **Backbone Area 0**.
* **Router-on-a-Stick (ROAS) (`Gig0/2.x` subinterfaces on Core Routers)**:
  * Uses 802.1Q encapsulation (`encapsulation dot1Q <vlan>`) on virtual subinterfaces to act as default gateways for VLAN 10 (`192.168.10.1`), VLAN 20 (`172.16.20.1`), and VLAN 93 (`172.20.0.1`).
* **`passive-interface Gig0/2.x`**: Advertises user networks via OSPF while suppressing OSPF hello frames down into access segments.

### Stateful Inter-VLAN ACL (`BLOCK-SALES-TO-IT-MGMT`)
Applied inbound (`IN`) on subinterface `Gig0/2.10`:
1. **`permit tcp 192.168.10.0 ... established`**: Allows returning TCP traffic to Sales if the connection was initiated by IT-Admin (VLAN 20) or Management (VLAN 93).
2. **`deny ip 192.168.10.0 ...`**: Prevents Sales (VLAN 10) from initiating new connections toward IT-Admin (`172.16.20.0/24`) or Management (`172.20.0.0/28`).
3. **`permit ip 192.168.10.0 ... any`**: Allows Sales hosts access to all other destinations (including WAN and Internet target `8.8.8.8`).

---

## 4. SW-DIST1 & SW-DIST2 (Layer 2 Redundant Distribution Switches)

### Role & Physical Interconnections
* **Role:** Aggregates connections from access layer switches to core routers and controls STP tree paths.
* **Physical Port Links:**
  * **`SW-DIST1`**: Uplink `Gig0/1` to `R-CORE1` (`Gig0/2`), Downlink `Fa0/1` to `SW-ACCESS1` (`Fa0/1`), Cross-link `Fa0/2` to `SW-DIST2` (`Fa0/2`).
  * **`SW-DIST2`**: Uplink `Gig0/1` to `R-CORE2` (`Gig0/2`), Downlink `Fa0/4` to `SW-ACCESS2` (`Fa0/4`), Cross-link `Fa0/2` to `SW-DIST1` (`Fa0/2`).

### Switching Mechanics
* **`vlan 10`, `vlan 20`, `vlan 93`**: Defines local Layer 2 broadcast domains across both distribution switches.
* **`spanning-tree mode rapid-pvst`**: Enables Rapid PVST+ (802.1w) for fast link failover.
* **STP Primary & Secondary Roles:**
  * **`SW-DIST1` (`root primary`)**: Acts as the Primary Root Bridge for user VLANs (VLAN 10 & VLAN 20).
  * **`SW-DIST2` (`root secondary`)**: Acts as Secondary Backup Root Bridge (or Primary for Management VLAN 93).
* **`switchport mode trunk` & `switchport trunk allowed vlan 10,20,93`**: Restricts trunk traffic to authorized VLAN IDs.
* **Management SVIs (`interface vlan 93` & `ip default-gateway`)**:
  * **`SW-DIST1` SVI:** `172.20.0.2/28` (Gateway: `172.20.0.1`)
  * **`SW-DIST2` SVI:** `172.20.0.5/28` (Gateway: `172.20.0.1`)
* **`interface range ... shutdown`**: Disables unassigned ports to harden network security.

---

## 5. SW-ACCESS1 & SW-ACCESS2 (Access Layer Switches)

### Role & Connectivity
* **Role:** Provides physical port access for endpoints and enforces port security controls.
* **Uplinks & Inter-Access Links:**
  * **`SW-ACCESS1`**: Uplink `Fa0/1` to `SW-DIST1` (`Fa0/1`), Inter-switch link `Fa0/3` to `SW-ACCESS2` (`Fa0/3`).
  * **`SW-ACCESS2`**: Uplink `Fa0/4` to `SW-DIST2` (`Fa0/4`), Inter-switch link `Fa0/3` to `SW-ACCESS1` (`Fa0/3`).

### Exact Port Mappings
* **`SW-ACCESS1` Host Ports:**
  * `Fa0/21` — **PC0** (VLAN 10 SALES - `192.168.10.11/24`)
  * `Fa0/22` — **PC1** (VLAN 10 SALES - `192.168.10.12/24`)
  * `Fa0/23` — **PC2** (VLAN 20 IT/ADMIN - `172.16.20.11/24`)
  * `Fa0/24` — **PC3** (VLAN 20 IT/ADMIN - `172.16.20.12/24`)
* **`SW-ACCESS2` Host Ports:**
  * `Fa0/11` — **PC5** (VLAN 93 MANAGEMENT - `172.20.0.12/28`)
  * `Fa0/12` — **PC4** (VLAN 93 MANAGEMENT - `172.20.0.11/28`)

### Access Layer Security Controls
* **`switchport mode access` & `switchport access vlan <id>`**: Assigns host interfaces to designated VLAN domains.
* **`spanning-tree portfast`**: Allows access ports to bypass Listening and Learning states, transitioning immediately into Forwarding state.
* **`spanning-tree bpduguard enable`**: Automatically err-disables access ports if an unauthorized switch or BPDU generator is connected.

---

## 6. End-Devices (PC0 through PC5 Summary)

### Addressing & Gateway Summary Table

| Host Name | Connected Switch / Port | VLAN ID | Assigned IP Address | Subnet Mask | Default Gateway | Primary DNS |
| --- | --- | --- | --- | --- | --- | --- |
| **PC0** | `SW-ACCESS1` / `Fa0/21` | **VLAN 10** | `192.168.10.11` | `255.255.255.0` | `192.168.10.1` | `8.8.8.8` |
| **PC1** | `SW-ACCESS1` / `Fa0/22` | **VLAN 10** | `192.168.10.12` | `255.255.255.0` | `192.168.10.1` | `8.8.8.8` |
| **PC2** | `SW-ACCESS1` / `Fa0/23` | **VLAN 20** | `172.16.20.11` | `255.255.255.0` | `172.16.20.1` | `8.8.8.8` |
| **PC3** | `SW-ACCESS1` / `Fa0/24` | **VLAN 20** | `172.16.20.12` | `255.255.255.0` | `172.16.20.1` | `8.8.8.8` |
| **PC5** | `SW-ACCESS2` / `Fa0/11` | **VLAN 93** | `172.20.0.12` | `255.255.255.240` | `172.20.0.1` | `8.8.8.8` |
| **PC4** | `SW-ACCESS2` / `Fa0/12` | **VLAN 93** | `172.20.0.11` | `255.255.255.240` | `172.20.0.1` | `8.8.8.8` |
