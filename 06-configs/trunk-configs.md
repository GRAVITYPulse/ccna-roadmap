```markdown
# Trunk Configuration

An Ethernet trunk carries traffic for multiple VLANs across a single physical link.

Cisco switches commonly use IEEE 802.1Q VLAN tagging.

---

# Basic Trunk

```cisco
interface GigabitEthernet0/24
 switchport mode trunk

```

## Allowed VLANs

```cisco
interface GigabitEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30

```

Add a VLAN:

```cisco
switchport trunk allowed vlan add 40

```

Remove a VLAN:

```cisco
switchport trunk allowed vlan remove 40

```

---

# Native VLAN

Example:

```cisco
interface GigabitEthernet0/24
 switchport trunk native vlan 99

```

The native VLAN is sent untagged on an 802.1Q trunk.

Both ends should normally be configured consistently.

---

# Verification

```cisco
show interfaces trunk
show interfaces GigabitEthernet0/24 switchport

```

## Check:

* Operational mode
* Trunking status
* Native VLAN
* Allowed VLANs
* Active VLANs

---

# Troubleshooting

If VLAN traffic does not cross the trunk:

```cisco
show interfaces trunk
show vlan brief

```

## Check:

* Trunk actually formed
* VLAN exists
* VLAN allowed
* Native VLAN consistency
* Correct interfaces connected

---

# Common Failure

```text
Switch A
 VLAN 10
    |
    | Trunk
    |
Switch B
 VLAN 10

```

If VLAN 10 is not permitted on the trunk, VLAN 10 traffic cannot cross that link even if VLAN 10 exists on both switches.

```

```