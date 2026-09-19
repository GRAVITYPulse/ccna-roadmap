### `inter-vlan-routing.md`

```markdown
# Inter-VLAN Routing

VLANs create separate Layer-2 broadcast domains.

Communication between different VLANs requires Layer-3 routing.

```text
VLAN 10 ──┐
          │
          ├── Layer 3 Router
          │
VLAN 20 ──┘
Router-on-a-Stick

A single physical router interface uses multiple subinterfaces.

Router
interface GigabitEthernet0/0
 no shutdown

interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0

interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
Switch
interface GigabitEthernet0/24
 switchport mode trunk
Hosts

VLAN 10:

IP: 192.168.10.x
Gateway: 192.168.10.1

VLAN 20:

IP: 192.168.20.x
Gateway: 192.168.20.1
Layer-3 Switch / SVI
ip routing

interface vlan 10
 ip address 192.168.10.1 255.255.255.0
 no shutdown

interface vlan 20
 ip address 192.168.20.1 255.255.255.0
 no shutdown
Verification
show ip interface brief
show interfaces trunk
show vlan brief
show ip route

Test:

ping 192.168.20.10
Troubleshooting Checklist
 VLAN exists
 Access port belongs to correct VLAN
 Trunk is operational
 VLAN is allowed on trunk
 Router subinterface/SVI exists
 Correct IP address
 Correct subnet mask
 Gateway configured on hosts
 Layer-3 interface is up