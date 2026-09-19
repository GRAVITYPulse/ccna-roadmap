```markdown
# Layer 3 — Routing

Layer 3 provides logical addressing and forwarding between IP networks.

## Core Concepts

- IPv4 addressing
- Subnetting
- Default gateway
- Routing table
- Static routes
- Dynamic routing
- Next hop
- Administrative distance
- Metric
- Default route

---

## Routing Table

```cisco
show ip route

```

Example:

```text
O 192.168.20.0/24 [110/2] via 10.0.12.2

```

Interpretation:

* **O** = OSPF
* **192.168.20.0/24** = Destination
* **110** = Administrative Distance
* **2** = Metric
* **10.0.12.2** = Next Hop

### Common Route Codes

| Code | Meaning |
| --- | --- |
| `C` | Connected |
| `L` | Local |
| `S` | Static |
| `O` | OSPF |
| `D` | EIGRP |
| `R` | RIP |
| `B` | BGP |
| `*` | Candidate default |

---

## Static Route Configuration

```cisco
ip route 192.168.20.0 255.255.255.0 10.0.12.2

```

**Verify:**

```cisco
show ip route

```

---

## Default Route Configuration

```cisco
ip route 0.0.0.0 0.0.0.0 <next-hop>

```

**Verify:**

```cisco
show ip route 0.0.0.0

```

---

## Routing Troubleshooting

```cisco
show ip route
show ip route <destination>
show ip interface brief
show arp

```

**Test:**

```cisco
ping <next-hop>
ping <destination>
traceroute <destination>

```

---

## Important Principle

Routing requires a valid path in both directions.

```text
Source
  ↓
Forward Path
  ↓
Destination
  ↓
Return Path
  ↓
Source

```

A missing return route can cause communication to fail even when the forward route exists.

```

---

### `ping-traceroute-analysis.md`

```markdown
# Ping and Traceroute Analysis

## Ping

`ping` uses ICMP Echo Request and Echo Reply messages to test IP reachability.

### Cisco Command

```cisco
ping 192.168.10.1

```

### Windows Command

```cmd
ping 192.168.10.1

```

---

## Progressive Ping

Do not immediately test the final destination.

### Test Order:

1. Local interface
2. Default gateway
3. Next-hop router
4. Remote router
5. Remote network gateway
6. Final host

### Path Example:

```text
PC
  ↓
192.168.10.1
  ↓
10.0.12.2
  ↓
10.0.23.2
  ↓
192.168.20.1
  ↓
192.168.20.10

```

The first failed test provides a strong clue about where the problem exists.

---

## Common Ping Results

### Success

```text
!!!!!

```

Indicates Echo Replies were received.

### Failure

```text
.....

```

Indicates no replies were received within the timeout.

### Possible Causes:

* Routing failure
* ACL
* Host firewall
* Interface failure
* Incorrect addressing
* Missing return path

```

```