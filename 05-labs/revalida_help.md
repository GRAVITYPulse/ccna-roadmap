# Enterprise Network Topology: Routing, Switching & Security Defense Guide

This document provides a conceptual defense breakdown of the routing protocols, switching mechanisms, security policies, and physical topology links for revalida defense presentations.

---

## Global System & Management Configuration

* **`hostname <NAME>`**
  Modifies the CLI prompt to uniquely identify each device in the network hierarchy (`R-ISP`, `R-EDGE`, `R-CORE1`, `R-CORE2`, `SW-DIST1`, `SW-DIST2`, `SW-ACCESS1`, `SW-ACCESS2`).
* **`no ip domain-lookup`**
  Disables DNS name resolution on the device CLI to prevent command line hangs when typing incorrect commands.
* **`username admin privilege 15 secret <password>`**
  Creates an administrative account with privilege level 15 protected by strong cryptographic password hashing.
* **Line Security (`line con 0` & `line vty 0 4`)**
  * **`logging synchronous`**: Keeps system output from interrupting active console or remote terminal typing.
  * **`login local`**: Enforces authentication using the local account database for console and remote VTY connections.

---

## 1. R-ISP (Simulated Internet Provider)

### Role & Connections
* **Role:** Represents the public external Internet edge outside the private domain.
* **Physical Link:** `Gig0/0` (`203.0.113.1/30`) connects to `R-EDGE` (`Gig0/2` - `203.0.113.2/30`).
* **`interface Loopback0` (`8.8.8.8/32`):** Acts as a virtual operational target for off-network ping and path verification tests.

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

### Role & Core-to-Distribution Mapping
* **Role:** Layer 3 core handling internal routing, redundant paths, inter-VLAN default gateways, and stateful access control filtering.
* **Inter-Core Link:** `R-CORE1` (`Gig0/0` - `10.0.0.9/30`) connects directly to `R-CORE2` (`Gig0/1` - `10.0.0.10/30`).
* **Core Uplinks:**
  * `R-CORE1` connects to **`SW-DIST1`**.
  * `R-CORE2` connects to **`SW-DIST2`**.

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

### Role & Physical Distribution Paths
* **Role:** Provides a redundant distribution layer aggregating connection flows from access switches to their respective core routers while managing STP topology convergence.
* **Dedicated Connectivity:**
  * **`SW-DIST1`** is connected directly to **`R-CORE1`** (Uplink) and **`SW-ACCESS1`** (Downlink).
  * **`SW-DIST2`** is connected directly to **`R-CORE2`** (Uplink) and **`SW-ACCESS2`** (Downlink).
  * An inter-distribution trunk connects **`SW-DIST1`** to **`SW-DIST2`** for cross-distribution redundancy.

### Switching Mechanics
* **`vlan 10`, `vlan 20`, `vlan 93`**: Defines local Layer 2 broadcast domains across both distribution switches.
* **`spanning-tree mode rapid-pvst`**: Enables Rapid PVST+ (802.1w) for sub-second failover convergence.
* **STP Primary & Secondary Roles:**
  * **`SW-DIST1` (`root primary`)**: Acts as the Primary Root Bridge for user VLANs (VLAN 10 & VLAN 20).
  * **`SW-DIST2` (`root secondary`)**: Acts as the Secondary Backup Root Bridge for user VLANs (or Primary for Management VLAN 93).
* **`switchport mode trunk` & `switchport trunk allowed vlan 10,20,93`**: Passes VLAN tagged frames across trunks while restricting unauthorized VLAN traffic.
* **Management SVIs (`interface vlan 93` & `ip default-gateway`)**:
  * **`SW-DIST1` SVI:** `172.20.0.2/28`
  * **`SW-DIST2` SVI:** `172.20.0.5/28` (Gateway: `172.20.0.1`)
* **`interface range ... shutdown`**: Hardens unused switch ports against physical access.

---

## 5. SW-ACCESS1 & SW-ACCESS2 (Access Layer Switches)

### Role & Connectivity
* **Role:** Provides direct access port connections for end-user PCs and enforces port security.
* **Uplinks & Inter-Switch Links:**
  * **`SW-ACCESS1`** uplinks to **`SW-DIST1`**.
  * **`SW-ACCESS2`** uplinks to **`SW-DIST2`**.
  * Inter-access trunk connects **`SW-ACCESS1`** (`Fa0/3`) directly to **`SW-ACCESS2`** (`Fa0/3`).

### Port Assignments
* **SW-ACCESS1:**
  * `Fa0/21` & `Fa0/22`: Access ports for **VLAN 10 SALES** (PC0, PC1).
  * `Fa0/23` & `Fa0/24`: Access ports for **VLAN 20 IT/ADMIN** (PC2, PC3).
* **SW-ACCESS2:**
  * `Fa0/11` & `Fa0/12`: Access ports for **VLAN 93 MANAGEMENT** (PC4, PC5).

### Access Layer Protection
* **`switchport mode access` & `switchport access vlan <id>`**: Binds access interfaces to designated VLANs.
* **`spanning-tree portfast`**: Places endpoint ports directly into forwarding state, skipping Listening and Learning delays.
* **`spanning-tree bpduguard enable`**: Protects the Layer 2 domain by automatically placing ports into an `err-disable` state if an unauthorized switch or BPDU generator is attached.

---

## 6. End-Devices (PC0 through PC5)

### Addressing Breakdown
* **VLAN 10 SALES (`192.168.10.0/24`) — Gateway: `192.168.10.1`**
  * **PC0:** `192.168.10.11/24` (Connected to `SW-ACCESS1` `Fa0/21`)
  * **PC1:** `192.168.10.12/24` (Connected to `SW-ACCESS1` `Fa0/22`)
* **VLAN 20 IT / ADMIN (`172.16.20.0/24`) — Gateway: `172.16.20.1`**
  * **PC2:** `172.16.20.11/24` (Connected to `SW-ACCESS1` `Fa0/23`)
  * **PC3:** `172.16.20.12/24` (Connected to `SW-ACCESS1` `Fa0/24`)
* **VLAN 93 MANAGEMENT (`172.20.0.0/28`) — Gateway: `172.20.0.1`**
  * **PC4:** `172.20.0.11/28` (Connected to `SW-ACCESS2` `Fa0/12`)
  * **PC5:** `172.20.0.12/28` (Connected to `SW-ACCESS2` `Fa0/11`)

* **Host Settings:** All endpoints use DNS `8.8.8.8`. Intra-VLAN switching occurs locally at the access/distribution layer, while inter-VLAN and Internet-bound traffic are routed via core gateway subinterfaces.
