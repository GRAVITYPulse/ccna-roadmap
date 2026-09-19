### `layer-2-switching.md`

```markdown
# Layer 2 — Switching

Layer 2 is responsible for Ethernet frame forwarding within a broadcast domain.

## Major Topics

- MAC addresses
- Ethernet frames
- VLANs
- Access ports
- Trunks
- STP
- EtherChannel
- MAC address tables
- Broadcast domains

---

## MAC Address Learning

Switches learn source MAC addresses.

```text
Incoming Frame
      ↓
Source MAC learned
      ↓
Destination MAC lookup
      ↓
Forward / Flood

Verify:

show mac address-table
show mac address-table dynamic
Known Unicast

If the destination MAC exists in the MAC table:

Frame → Specific Port
Unknown Unicast

If the destination MAC is unknown:

Frame → Flood within VLAN

The frame is not normally forwarded back out the interface on which it was received.

Broadcast

Broadcast frames are flooded throughout the local VLAN unless a Layer-3 boundary or filtering mechanism stops them.

VLAN Verification
show vlan brief

Check:

VLAN exists
Correct ports assigned
Port is active
Trunk Verification
show interfaces trunk

Check:

Trunk status
Allowed VLANs
Native VLAN
Active VLANs
STP Verification
show spanning-tree
show spanning-tree vlan 10
show spanning-tree root

STP prevents Layer-2 loops by placing redundant paths into a non-forwarding state.

EtherChannel
show etherchannel summary

Check:

Correct channel-group
Member interfaces
LACP/PAgP state
Port-channel status
Layer 2 Troubleshooting Questions
Is the interface physically up?
Is the correct VLAN assigned?
Does the VLAN exist?
Is the trunk operational?
Is the VLAN allowed?
Is STP forwarding?
Is the MAC address learned?
Is EtherChannel correctly formed?
Useful Commands
show vlan brief
show interfaces switchport
show interfaces trunk
show mac address-table
show spanning-tree
show etherchannel summary