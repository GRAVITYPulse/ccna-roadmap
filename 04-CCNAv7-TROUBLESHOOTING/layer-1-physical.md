### `layer-1-physical.md`

```markdown
# Layer 1 — Physical Layer Troubleshooting

Layer 1 concerns the physical transmission of bits.

## Common Components

- Copper Ethernet cables
- Fiber cables
- SFP/SFP+ modules
- Network interfaces
- Transceivers
- Power
- Physical ports

---

## Interface Status

```cisco
show ip interface brief
show interfaces
show interfaces status
Common States
Status	Meaning
up/up	Interface is operational
administratively down/down	Interface is shut down
down/down	Physical/link problem is likely
Bring an Interface Up
interface GigabitEthernet0/1
 no shutdown

Verify:

show ip interface brief
Check Errors
show interfaces GigabitEthernet0/1

Look for:

Input errors
CRC errors
Frame errors
Output errors
Collisions
Late collisions
Runts
Giants
Interface resets
Speed and Duplex
show interfaces GigabitEthernet0/1

Possible configuration:

interface GigabitEthernet0/1
 speed 1000
 duplex full

Use manual speed/duplex settings only when required by the environment.

Physical Troubleshooting Checklist
 Cable connected
 Correct cable type
 Interface enabled
 Link LEDs active
 Correct SFP installed
 SFP supported
 Speed compatible
 Duplex compatible
 No excessive errors
 Correct interface being used
Key Principle

If Layer 1 is broken, higher-layer troubleshooting is premature.

Start with:

show interfaces
show interfaces status
show ip interface brief