```markdown
# L2 Network Engineer — Quick Cheat Sheet
*Commands | Troubleshooting | Key Concepts | Most Asked Scenarios*
*Stay Calm, Think Logical, Solve It :-)*

---

### 1. Basic Device Information (Switch/Router)
* `- show version` — Device model, IOS version
* `- show ip interface brief` — Interface status & IP
* `- show interfaces status` — Current & admin status
* `- show running-config` — Current config
* `- show startup-config` — Saved config
* `- show vlan brief` — VLANs on the switch
* `- show mac address-table` — MAC table
* `- show spanning-tree` — STP info
* `- show cdp neighbors` — Connected devices (Cisco)
* `- show lldp neighbors` — Connected devices (multi-vendor)

---

### 2. VLAN & Trunk Configuration
```text
# Create VLAN
vlan 10

# Assign to interface (Access)
interface Gi0/1
 switchport mode access
 switchport access vlan 10

# Trunk mode
interface Gi0/24
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30

# Check VLAN & trunk
show vlan brief
show interfaces trunk

```

---

### 3. STP (Spanning Tree Protocol)

* `- show spanning-tree vlan 10` (STP states)
* `- show spanning-tree root` (Root bridge info)
* `- show spanning-tree inconsistentports` (Inconsistent port)
* `- show spanning-tree interface Gi0/1` (Port details)

#### **STP States**

| State | Description |
| --- | --- |
| **Blocking** | Not forwarding |
| **Listening** | STP state |
| **Learning** | Build MAC table |
| **Forwarding** | Normal operation |
| **Disabled** | Manually disabled |

---

### 4. Trunking & Native VLAN

* `- show interface trunk` (Trunk status)
* `- show interfaces g/La4 switchport` (Port mode & VLAN)
* **Native VLAN** — Untagged traffic
* **Allowed VLAN** — Tagged traffic

```
[ SW1 ] <====== Trunk ======> [ SW2 ]
VLAN 10,20,30                VLAN 10,20,30

```

---

### 5. EtherChannel (LACP/PaGP)

* `- show etherchannel summary`
* `- show port-channel port-channel 1`
* `- show interfaces port-channel 1` (Member links & states)
* **LACP** = active / passive
* **PaGP** = desirable / auto

---

### 6. Troubleshooting Flow (Condition)

1. **Check physical link** (`show interface status`)
2. **Check VLAN config** (`show vlan brief`)
3. **Check trunk config** (`show interface trunk`)
4. **Check MAC table** (`show mac address-table`)
5. **Check STP** (`show spanning-tree`)
6. **Check errors** (`show interface counters`)
7. **Verify with ping / traceroute**

---

### 7. Common Issues & Fixes

* **Port not coming up** — Check routing, speed/duplex, err-disabled
* **VLAN mismatch** — Check trunk status/priority
* **STP blocking** — Check root bridge/priority
* **No internet** — Check gateway, ACL, routing
* **Intermittent link** — Check duplex, errors, cable
* **High CPU** — Check loops, STP, logs, queue

---

### 8. Routing Basics (Quick Ref)

* **Default Route:** `0.0.0.0/0`
* **Host Route:** `/32`
* **Subnet Masks:** `255.255.255.0` = `/24`
* **Broadcast:** `xxx.xxx.xxx.255`
* **Private IP:** `10.x.x.x`, `172.16.x.x - 172.31.x.x`, `192.168.x.x`
* **Hop:** Hop: Next router IP
* **Administrative Distance (AD):**
* Connected: `0`
* Static: `1`
* EIGRP: `90`
* OSPF: `110`
* BGP: `120`



---

### 9. Useful Show Commands

* `- show ip route` — Routing table
* `- show ip arp` — ARP table
* `- show users` — Logged in users
* `- show processes cpu` — CPU usage
* `- show processes memory` — Memory usage
* `- show logging` — Logs
* `- show clock` — Time
* `- show tech-support` — Full debug info

---

### 10. Wireless (Quick Points)

* **Port AP status** — `show ap summary`
* **Client details** — `show client summary`
* **Radio info** — `show ap config general`
* **Channel/Power** — `show ap config 802.11a`
* **Common Issues:**
* No client join
* Link down
* Interference
* DHCP failure


* *Check AP, switch, AP, and controller logs.*

---

### 11. Important Protocols

* **STP** — Loop protection
* **LACP** — Link aggregation
* **VLAN** — Segmentation
* **CDP/LLDP** — Neighbor discovery
* **EIGRP** — Cisco IGP
* **OSPF** — Open IGP
* **BGP** — Exterior gateway
* **VRRP / HSRP** — Gateway redundancy

---

### 12. Key Points to Remember

* [ ] Always check link and interface status first.
* [ ] Document the changes.
* [ ] Verify configuration on both ends.
* [ ] Use ping, traceroute, show commands.
* [ ] Check for loops, duplex mismatch, errors.
* [ ] Follow ITIL & Change management process.
* [ ] Keep a cool mind — maintain standard setup! :-)

---

### 13. Useful Abbreviations

* **L1** — Layer 1
* **L2** — Layer 2
* **L3** — Layer 3
* **LAN** — Local Area Network
* **WAN** — Wide Area Network
* **IP** — Internet Protocol
* **MTU** — Maximum Transmission Unit
* **DNS** — Domain Name System
* **DHCP** — Dynamic Host Configuration Protocol

---

### 14. VLAN Ranges & Subnets

#### **VLAN Ranges**

* `1 - 100` $\rightarrow$ User VLAN
* `101 - 200` $\rightarrow$ Infrastructure
* `201 - 2000` $\rightarrow$ Reserved / Others

#### **Common Subnet Masks**

* `/24` $\rightarrow$ `255.255.255.0`
* `/20` $\rightarrow$ `255.255.240.0`
* `/22` $\rightarrow$ `255.255.252.0`
* `/23` $\rightarrow$ `255.255.254.0`
* `/30` $\rightarrow$ `255.255.255.252`

---

### 15. Final Reminder

Network issues are like puzzles...
Look at the bigger picture, check the basics, and don't forget to document! :-)

**You Got This!**

```

```