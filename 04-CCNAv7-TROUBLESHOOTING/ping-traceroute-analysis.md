```markdown
## Traceroute

### Cisco Command

```cisco
traceroute 192.168.20.10

```

### Windows Command

```cmd
tracert 192.168.20.10

```

Traceroute uses increasing TTL values to reveal Layer-3 hops.

---

## Important

A `*` does not automatically mean the router is broken.

### Possible Reasons Include:

* ICMP filtering
* Rate limiting
* Control-plane protection
* Device configured not to respond
* Actual forwarding failure

Therefore, correlate traceroute with:

```cisco
ping
show ip route
show arp
show interfaces

```

---

## Troubleshooting Principle

Use **ping** to answer:

> Can the destination be reached?

Use **traceroute** to help answer:

> Where does the path stop responding?

Then use Cisco **show commands** to determine *why*.

```

```