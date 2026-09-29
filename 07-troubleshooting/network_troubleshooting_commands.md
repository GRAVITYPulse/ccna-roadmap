# Top Network Troubleshooting Commands
(Cisco IOS - Must Know for CCNA / CCNP & Real World)

> **Identify → Analyze → Fix → Verify**
> *(Repeat if needed)*

---

### 1. Basic Connectivity & Interface

| Command | What it shows / Use |
| :--- | :--- |
| `ping <ip>` | Check reachability to a host. |
| `traceroute <ip>` | Shows path & where it stops. |
| `show ip interface brief` | Interface status (up/down). |
| `show interfaces` | Detailed interface info (errors, drops). |
| `show interfaces counters` | Packet errors, drops, CRC, etc. |
| `show cable-diagnostics tdr` | Check physical cable issue (switch). |
| `show controllers ethernet-controller` | Check hardware/port status. |

---

### 2. Routing Troubleshooting

| Command | What it shows / Use |
| :--- | :--- |
| `show ip route` | Routing table. |
| `show ip route <ip>` | Find route to specific IP. |
| `show ip protocols` | Routing protocol info. |
| `show running-config section router` | Check routing configuration. |
| `show ip ospf neighbor` | OSPF neighbors. |
| `show ip ospf database` | OSPF LSDB. |
| `show ip bgp summary` | BGP peers. |
| `show ip eigrp neighbors` | EIGRP neighbors. |

---

### 3. ARP, MAC & Switching

| Command | What it shows / Use |
| :--- | :--- |
| `show arp` | ARP table (IP - MAC). |
| `show mac address-table` | MAC address table (switch). |
| `show spanning-tree` | STP status. |
| `show spanning-tree vlan <vlan>` | STP info for specific VLAN. |
| `show vlan brief` | VLAN configuration. |
| `show cdp neighbors` | CDP neighbors (Cisco devices). |
| `show lldp neighbors` | LLDP neighbors (multi-vendor). |

---

### 4. NAT & Firewall (Security)

| Command | What it shows / Use |
| :--- | :--- |
| `show ip nat translations` | Active NAT sessions. |
| `show ip nat statistics` | NAT interface states. |
| `show access-lists` | ACL configuration. |
| `show run | section access-list` | ACL details. |
| `show ip access-lists` | ACL hit counts. |
| `show crypto isakmp sa` | IPsec Phase 1 status. |
| `show crypto ipsec sa` | IPsec Phase 2 status. |
| `show vpn-sessiondb` | VPN (if using DMVPN/AnyConnect). |

---

### 5. DNS, DHCP & Utilities

| Command | What it shows / Use |
| :--- | :--- |
| `show ip dhcp binding` | DHCP leased IPs. |
| `show ip dhcp server statistics` | DHCP server status. |
| `show hosts` | Local host entries. |
| `nslookup <domain>` | DNS resolution test. |
| `show running-config | include dns` | DNS configuration. |
| `show clock` | Check time (useful for logs). |

---

### 6. Debug & Logs

| Command | What it shows / Use |
| :--- | :--- |
| `debug ip packet` | IP packet flow (use carefully). |
| `debug ip ospf events` | OSPF events. |
| `debug ip nat` | NAT translation debug. |
| `debug crypto isakmp` | IKE debug. |
| `debug crypto ipsec` | IPsec debug. |
| `show logging` | System logs. |
| `show logging | include <text>` | Search logs for keyword. |

---

### 7. System & Performance

| Command | What it shows / Use |
| :--- | :--- |
| `show version` | IOS version & device info. |
| `show processes cpu` | CPU usage. |
| `show processes memory` | Memory usage. |
| `show inventory` | Hardware info. |
| `show environment` | Temperature, power, etc. |

---

### 8. Quick Troubleshooting Flow

1. Check physical link (cable, interface, power).
2. Check IP configuration (IP, mask, gateway).
3. Check routing table (static/dynamic).
4. Check ARP / MAC table.
5. Check ACL / Firewall / NAT.
6. Check routing protocol (EIGRP, OSPF, BGP).
7. Review logs & debugs (if needed).
8. Verify end-to-end connectivity (`ping`/`traceroute`).

---

### 💡 Pro Tips

* ✅ **Always check the basics first.**
* ✅ **Use `show` commands before `debug`.**
* ✅ **Debug can impact performance.**
* ✅ **Use filters (`| include` / `| section` / `| begin`).**
* ✅ **Keep a backup of running-config.**
* ✅ **Understand the topology & path flow.**
* ✅ **Be calm, analyze logically, then fix.**

---

**Right Command + Proper Analysis = Fast Resolution**