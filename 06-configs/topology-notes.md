### `topology-notes.md`

```markdown
# Topology Notes

Documentation for lab topology design, addressing, VLANs, routing, and dependencies.

---

# Topology

```text
                R1
             /      \
           SW1      SW2
          /  \      /  \
      VLAN10 VLAN20 VLAN30 VLAN99

Replace the example with the actual topology.

Device Naming

Recommended naming convention:

R1
R2
R3

SW-CORE1
SW-ACCESS1
SW-ACCESS2

Use names that communicate the device's role.

Addressing Table
Device	Interface	IP Address	Mask	Purpose
R1	G0/0	192.168.10.1	/24	VLAN 10 Gateway
R1	G0/1	10.0.12.1	/30	R1-R2
R2	G0/0	10.0.12.2	/30	R1-R2
VLAN Table
VLAN	Name	Network	Gateway
10	SALES	192.168.10.0/24	192.168.10.1
20	IT	172.16.20.0/24	172.16.20.1
99	MANAGEMENT	172.16.99.0/24	172.16.99.1
Routing

Document:

Routing Protocol:
OSPF / Static / Other

Router IDs:

Networks Advertised:

Default Route:
Dependencies

Document what must work before another feature can work.

Example:

Physical Link
     ↓
VLAN
     ↓
Trunk
     ↓
Inter-VLAN Routing
     ↓
Routing
     ↓
NAT
     ↓
End-to-End Connectivity
Testing Plan
1. Test local host connectivity
2. Test default gateway
3. Test inter-VLAN connectivity
4. Test router-to-router connectivity
5. Test remote networks
6. Test Internet/NAT connectivity
7. Test management access
Change Log
Date	Change	Reason
YYYY-MM-DD	Added VLAN 20	Lab requirement