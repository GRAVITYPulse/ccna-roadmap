### `nat-configs.md`

```markdown
# NAT Configuration

Network Address Translation changes IP addressing between inside and outside networks.

## NAT Terminology

| Term | Meaning |
|---|---|
| Inside Local | Inside host address before translation |
| Inside Global | Public/global address representing the inside host |
| Outside Local | Outside host address as seen from inside |
| Outside Global | Actual outside host address |

---

# Static NAT

One inside address maps to one global address.

```cisco
ip nat inside source static 192.168.10.10 203.0.113.10
Dynamic NAT

Create a pool:

ip nat pool PUBLIC 203.0.113.10 203.0.113.20 netmask 255.255.255.0

Define which inside addresses can be translated:

access-list 1 permit 192.168.10.0 0.0.0.255

Configure:

ip nat inside source list 1 pool PUBLIC
PAT / NAT Overload

Multiple inside hosts share one global address.

access-list 1 permit 192.168.10.0 0.0.0.255

ip nat inside source list 1 interface GigabitEthernet0/1 overload
Define NAT Interfaces

Inside:

interface GigabitEthernet0/0
 ip nat inside

Outside:

interface GigabitEthernet0/1
 ip nat outside
Verification
show ip nat translations
show ip nat statistics
Troubleshooting

Check:

show running-config | include ip nat
show ip nat translations
show ip nat statistics
show access-lists
show ip interface brief

Verify:

Correct inside interface
Correct outside interface
Correct ACL
Correct NAT pool
Correct route toward outside network
Return traffic can reach the translated address
Important

NAT and routing are different functions.

Routing → decides where the packet goes
NAT     → modifies addressing information
PAT     → uses ports to allow many flows to share an address