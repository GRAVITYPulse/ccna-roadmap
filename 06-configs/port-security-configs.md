### `port-security-configs.md`

```markdown
# Port Security

Port security restricts which MAC addresses are allowed on a switchport.

Normally used on access ports.

---

# Basic Configuration

```cisco
interface GigabitEthernet0/1
 switchport mode access
 switchport access vlan 10
 switchport port-security
Maximum MAC Addresses
switchport port-security maximum 2
Sticky MAC
switchport port-security mac-address sticky

The switch can dynamically learn MAC addresses and add them as secure MAC addresses.

Violation Modes
switchport port-security violation protect
switchport port-security violation restrict
switchport port-security violation shutdown
Mode	General behavior
Protect	Drops violating traffic
Restrict	Drops violating traffic and records/logs the violation
Shutdown	Places the interface into an error-disabled state
Verification
show port-security
show port-security interface GigabitEthernet0/1
show port-security address
Troubleshooting Error-Disabled Port

Check:

show interfaces status
show port-security interface GigabitEthernet0/1

If the violation caused an error-disabled state, investigate the cause before restoring the port.

Possible recovery:

interface GigabitEthernet0/1
 shutdown
 no shutdown

The exact recovery behavior depends on the cause and platform configuration.

Best Practice

Port security should be used deliberately.

Consider:

Maximum allowed MAC addresses
Sticky vs manually configured MAC addresses
Violation mode
Voice VLAN requirements
Whether the port is actually an endpoint/access port