# Broken Network Scenarios

A troubleshooting practice file for intentionally broken Cisco networks.

## Troubleshooting Methodology

Use this order:

1. Identify the symptom
2. Determine the affected hosts/networks
3. Start at Layer 1
4. Check Layer 2
5. Check Layer 3
6. Check services
7. Check security/filtering
8. Identify the root cause
9. Apply the smallest required fix
10. Verify end-to-end connectivity

---

## Scenario 1 — PC Cannot Reach Default Gateway

### Symptoms

- PC has an IP address
- PC cannot ping its default gateway

### Check

```cisco
show ip interface brief
show vlan brief
show interfaces switchport
show interfaces status
Possible Causes
Incorrect access VLAN
Interface shutdown
Wrong IP address/subnet mask
Incorrect default gateway
VLAN does not exist
Physical link failure
Verification
PC → Switch → Default Gateway

The first failed hop identifies the likely problem area.

Scenario 2 — Same VLAN Hosts Cannot Communicate
Check
show vlan brief
show mac address-table
show interfaces switchport
Possible Causes
Ports assigned to different VLANs
VLAN missing
Interface shutdown
Incorrect cabling
Port security violation
Scenario 3 — VLAN Works Locally but Not Across Switches
Check
show interfaces trunk
show vlan brief
Possible Causes
Trunk not configured
VLAN not allowed on trunk
Native VLAN mismatch
VLAN does not exist on the required switch
Scenario 4 — Inter-VLAN Routing Fails
Check
show ip interface brief
show interfaces trunk
show ip route
Possible Causes
Incorrect SVI/subinterface IP
Missing encapsulation dot1Q
Router interface shutdown
Switch-to-router link is not a trunk
Incorrect default gateway
Missing VLAN
Scenario 5 — Remote Network Cannot Be Reached
Check
show ip route
show arp
ping <next-hop>
ping <destination>
traceroute <destination>
Possible Causes
Missing route
Incorrect next hop
Routing protocol problem
Missing return route
ACL filtering traffic
Root-Cause Documentation

For every scenario, document:

Symptom:
Root Cause:
Evidence:
Configuration Error:
Fix:
Verification:

The goal is to identify why the network failed, not simply make the ping succeed.