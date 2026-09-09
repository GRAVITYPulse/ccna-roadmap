# Enterprise Network Topology: Routing, Switching & Security Defense Guide

This document breaks down the operational concepts, routing protocols, switching mechanisms, and security policies configured across the enterprise network topology for revalida presentation.

---

## Global System & Management Configuration

* **`hostname <NAME>`**
  Modifies the CLI prompt to uniquely identify each device in the network hierarchy, aiding in session identification and centralized logging.
* **`no ip domain-lookup`**
  Disables DNS name resolution on the device CLI. This prevents long delay freezes (30+ seconds) caused by broadcast lookups when mistyping commands.
* **`username admin privilege 15 secret <password>`**
  Creates a local administrator account with privilege level 15 (full administrative access) protected by strong cryptographic password hashing.
* **Line Configuration (`line con 0` & `line vty 0 4`)**
  * **`logging synchronous`**: Prevents asynchronous system notifications and debug outputs from interrupting active CLI input lines.
  * **`login local`**: Configures console and remote VTY lines to authenticate users against the local device account database.

---

## 1. R-ISP (Simulated Internet Provider)

### Role
Functions as the untrusted, public external provider edge outside the enterprise domain.

### Operational Mechanics
* **`interface Loopback0` (`8.8.8.8/32`)**
  A logical virtual interface that remains continuously in an UP state regardless of physical link conditions. It acts as an off-network, external target for ping and traceroute verification.
* **`interface GigabitEthernet0/0` (`203.0.113.1/30`)**
  The public WAN edge interface facing the enterprise gateway router (`R-EDGE`).

---

## 2. R-EDGE (Enterprise Edge & NAT Gateway)

### Role
The enterprise boundary router handling edge security, default WAN routing, and IPv4 address translation between private RFC 1918 networks and the public Internet.

### Routing & Translation Concepts
* **`ip nat inside` / `ip nat outside`**
  Defines the Network Address Translation (NAT) boundaries. Internal interfaces (`G0/0`, `G0/1`) are marked as the inside private network, while `G0/2` is marked as the outside public network.
* **`ip access-list standard NAT-ACL`**
  Defines the standard ACL identifying internal private source subnets allowed to be translated:
  * `192.168.10.0/24` (Sales)
  * `172.16.20.0/24` (IT-Admin)
  * `172.20.0.0/28` (Management)
* **`ip nat inside source list NAT-ACL interface G0/2 overload`**
  Implements **Port Address Translation (PAT)** / NAT Overload. Multiple internal private IP addresses share a single public IP address (`203.0.113.2`) on interface `G0/2` by appending unique Layer 4 source port numbers to distinguish returning flows.
* **`ip route 0.0.0.0 0.0.0.0 203.0.113.1`**
  Establishes a static **Gateway of Last Resort** directing all traffic destined for unknown/external subnets out toward the ISP edge router.
* **`default-information originate` (OSPF)**
  Injects the static default route into the internal OSPF domain, dynamically informing core routers (`R-CORE1` and `R-CORE2`) how to route outbound Internet traffic.

---

## 3. R-CORE1 & R-CORE2 (OSPF Core & Inter-VLAN Gateway)

### Role
High-speed Layer 3 core routers handling dynamic inter-router routing, default gateway services for internal VLANs, and stateful access control filtering.

### Routing Concepts
* **`router ospf 1` & `router-id <x.x.x.x>`**
  Initializes OSPF process ID `1`. Explicitly setting unique 32-bit Router IDs (`1.1.1.1`, `2.2.2.2`, `3.3.3.3`) ensures deterministic neighbor selection and link-state database stability.
* **`network <subnet> <wildcard> area 0`**
  Enables OSPF link-state routing on internal `/30` point-to-point core links within **Area 0 (Backbone Area)** to construct an accurate topology database.
* **Router-on-a-Stick (ROAS) on R-CORE2 (`Gig0/2.x` subinterfaces)**
  * **`encapsulation dot1Q <vlan_id>`**: Configures 802.1Q VLAN encapsulation on virtual subinterfaces. A single physical trunk cable carries traffic for multiple subnets, acting as the default gateway for VLAN 10 (`192.168.10.1`), VLAN 20 (`172.16.20.1`), and VLAN 93 (`172.20.0.1`).
* **`passive-interface GigabitEthernet0/2.x`**
  Includes the user subnets in OSPF network advertisements while suppressing outgoing OSPF Hello packets down into access segments, conserving bandwidth and preventing unauthorized routing adjacencies.

### Stateful Inter-VLAN Access Control (`BLOCK-SALES-TO-IT-MGMT`)
Applied inbound (`IN`) on `R-CORE2` subinterface `GigabitEthernet0/2.10`:
1. **`permit tcp 192.168.10.0 ... established`**
   Simulates stateful inspection by allowing returning TCP traffic into Sales *only if* the connection was originally initiated by hosts in IT-Admin (VLAN 20) or Management (VLAN 93).
2. **`deny ip 192.168.10.0 ...`**
   Blocks hosts in Sales (VLAN 10) from initiating *any new* IP connections toward the sensitive IT-Admin (`172.16.20.0/24`) or Management (`172.20.0.0/28`) subnets.
3. **`permit ip 192.168.10.0 ... any`**
   Permits Sales hosts to reach all other destinations, including cross-router links and external public Internet addresses (`8.8.8.8`).

---

## 4. SW-DIST (Layer 2 Distribution Switch)

### Role
Aggregates connection flows from access layer switches, maintains VLAN segmentation databases, and dictates Spanning Tree paths.

### Switching Concepts
* **`vlan 10`, `vlan 20`, `vlan 93`**
  Creates distinct Layer 2 broadcast domains within the switch database, isolating traffic at Layer 2.
* **`spanning-tree mode rapid-pvst`**
  Enables **Rapid Per-VLAN Spanning Tree Plus (RSTP / 802.1w)**, allowing individual Spanning Tree instances per VLAN with fast convergence times (seconds instead of 30–50 seconds in legacy 802.1D).
* **`spanning-tree vlan 10,20,93 root primary`**
  Lowers the bridge priority for VLANs 10, 20, and 93, electing `SW-DIST` as the **Root Bridge**. This creates a predictable tree structure with optimal path selection.
* **`switchport mode trunk` & `switchport trunk allowed vlan 10,20,93`**
  Configures 802.1Q trunking on inter-switch and router links while restricting frame propagation strictly to authorized VLAN IDs.
* **Switch Virtual Interface (SVI) (`interface vlan 93` & `ip default-gateway`)**
  Configures a management IP address (`172.20.0.2/28`) inside VLAN 93 and sets `172.20.0.1` as the gateway, allowing administrators on other subnets to manage the switch remotely.
* **`interface range ... shutdown`**
  Hardens Layer 2 security by disabling unused physical ports, preventing unauthorized physical access to the network.

---

## 5. SW-ACCESS1 & SW-ACCESS2 (Access Switches)

### Role
Provides high-density physical port access for end-user hosts, enforcing edge port protection and VLAN assignments.

### Switching Concepts
* **`spanning-tree vlan 10,20,93 root secondary` (SW-ACCESS1)**
  Assigns a secondary bridge priority, ensuring `SW-ACCESS1` instantly assumes Root Bridge responsibilities if `SW-DIST` fails.
* **`switchport mode access` & `switchport access vlan <id>`**
  Configures host-facing interfaces as fixed access ports belonging to a single VLAN, stripping 802.1Q tags on egress toward the endpoint.
* **`spanning-tree portfast`**
  Configures access ports to transition instantly from Blocking to Forwarding state upon link activation, bypassing the STP Listening and Learning states to eliminate delay for end-host devices.
* **`spanning-tree bpduguard enable`**
  Complements PortFast by monitoring access ports for Bridge Protocol Data Units (BPDUs). If an unauthorized switch or device sending BPDUs is connected, the port is put into an `err-disable` state to prevent topology loops or rogue Root Bridge takeovers.

---

## 6. End-Devices (PC0 through PC5)

### Role
Operational endpoints configured within their designated logical subnets.

* **Configuration Rules:** End-hosts are configured with static IP addresses (`.11` and `.12`), matching network subnet masks, external DNS (`8.8.8.8`), and Default Gateways (`192.168.10.1`, `172.16.20.1`, `172.20.0.1`).
* **Traffic Flow:** Local intra-VLAN traffic stays within the access switch layer. Cross-VLAN and outbound Internet traffic are directed to the respective default gateway subinterfaces on `R-CORE2` for routing and policy enforcement.