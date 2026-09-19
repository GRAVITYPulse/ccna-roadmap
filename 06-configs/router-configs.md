```markdown
# Router Configuration Guide

## Basic Configuration

```cisco
enable
configure terminal

hostname R1

no ip domain-lookup

enable secret <SECRET>

```

---

# Interface Configuration

```cisco
interface GigabitEthernet0/0
 description LAN
 ip address 192.168.10.1 255.255.255.0
 no shutdown

```

## Verify

```cisco
show ip interface brief

```

---

# Loopback Interface

```cisco
interface Loopback0
 ip address 1.1.1.1 255.255.255.255

```

Loopbacks are commonly used for router IDs, testing, and management.

---

# Routing

## Static Route

```cisco
ip route 192.168.20.0 255.255.255.0 10.0.12.2

```

## Default Route

```cisco
ip route 0.0.0.0 0.0.0.0 10.0.12.2

```

---

# SSH Management

```cisco
ip domain-name lab.local

username admin privilege 15 secret <SECRET>

crypto key generate rsa modulus 2048

ip ssh version 2

line vty 0 4
 login local
 transport input ssh

```

---

# Save Configuration

```cisco
copy running-config startup-config

```

or:

```cisco
write memory

```

---

# Verification

```cisco
show running-config
show ip interface brief
show ip route
show ip protocols
show version
show ip ssh

```

```

```