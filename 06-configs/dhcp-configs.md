### `dhcp-configs.md`

```markdown
# DHCP Configuration

DHCP dynamically provides hosts with network configuration.

## DHCP Provides

Common DHCP information includes:

- IP address
- Subnet mask
- Default gateway
- DNS server
- Lease information

---

# Cisco DHCP Server

```cisco
ip dhcp excluded-address 192.168.10.1 192.168.10.20

ip dhcp pool VLAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 8.8.8.8
Verification
show ip dhcp pool
show ip dhcp binding
show ip dhcp conflict
DHCP Relay

When the DHCP server is on another network:

interface GigabitEthernet0/1
 ip helper-address 192.168.100.10

ip helper-address forwards DHCP broadcasts toward the DHCP server.

Troubleshooting

Check:

show ip interface brief
show ip dhcp binding
show ip dhcp pool
show running-config | section dhcp

Verify:

DHCP pool network is correct
Default gateway is correct
DHCP server is reachable
Relay address is correct
Client VLAN is correct
Interfaces are up
No conflicting static addressing exists
DHCP Troubleshooting Flow
Client
 ↓
DHCP Discover
 ↓
Broadcast
 ↓
Local DHCP Server?
 ├── Yes → DHCP Server
 └── No → DHCP Relay
             ↓
          DHCP Server