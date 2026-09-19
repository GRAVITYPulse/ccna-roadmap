### `switch-configs.md`

```markdown
# Switch Configuration Guide

## Basic Configuration

```cisco
enable
configure terminal

hostname SW1

no ip domain-lookup

enable secret <SECRET>
Management SVI
vlan 99
 name MANAGEMENT

interface vlan 99
 ip address 192.168.99.2 255.255.255.0
 no shutdown

For a Layer-2 switch, configure the default gateway:

ip default-gateway 192.168.99.1
Access Port
interface GigabitEthernet0/1
 description USER-PC
 switchport mode access
 switchport access vlan 10
Trunk
interface GigabitEthernet0/24
 description UPLINK
 switchport mode trunk

Where supported and appropriate:

switchport trunk allowed vlan 10,20,99
Shutdown Unused Ports

Example:

interface range GigabitEthernet0/10-23
 shutdown

Unused ports should be documented and secured according to the network's security policy.

Verification
show vlan brief
show interfaces status
show interfaces switchport
show interfaces trunk
show mac address-table
show ip interface brief
Save
copy running-config startup-config