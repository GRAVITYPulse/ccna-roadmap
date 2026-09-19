```markdown
# VLAN Configuration

A VLAN creates a logical Layer-2 broadcast domain.

---

# Create a VLAN

```cisco
vlan 10
 name SALES

vlan 20
 name IT

vlan 99
 name MANAGEMENT

```

## Verify

```cisco
show vlan brief

```

---

# Assign Access Port

```cisco
interface GigabitEthernet0/1
 switchport mode access
 switchport access vlan 10

```

## Verify

```cisco
show interfaces GigabitEthernet0/1 switchport

```

---

# Assign Multiple Access Ports

```cisco
interface range GigabitEthernet0/1-5
 switchport mode access
 switchport access vlan 10

```

---

# Management VLAN

```cisco
vlan 99
 name MANAGEMENT

interface vlan 99
 ip address 192.168.99.2 255.255.255.0
 no shutdown

```

For a Layer-2 switch:

```cisco
ip default-gateway 192.168.99.1

```

---

# Verification

```cisco
show vlan brief
show interfaces switchport
show ip interface brief

```

---

# VLAN Troubleshooting

## Check:

* Does the VLAN exist?
* Is the port assigned to the correct VLAN?
* Is the port operational?
* Is the VLAN allowed across trunks?
* Is STP forwarding?
* Does the host have the correct IP/subnet?

---

# VLAN vs Subnet

They are related but not identical.

* **VLAN:** Layer-2 broadcast domain
* **Subnet:** Layer-3 IP network

A common design maps one VLAN to one IP subnet, but the concepts should not be treated as the same thing.

---

# Example Addressing

| VLAN | Name | Network | Gateway |
| --- | --- | --- | --- |
| **10** | SALES | 192.168.10.0/24 | 192.168.10.1 |
| **20** | IT | 172.16.20.0/24 | 172.16.20.1 |
| **99** | MANAGEMENT | 172.16.99.0/24 | 172.16.99.1 |

```

```