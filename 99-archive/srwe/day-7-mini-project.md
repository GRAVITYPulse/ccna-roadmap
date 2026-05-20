* Review all topics

---

## 🧠 Explanation

This simulates a **real company network**

---

## 🧪 Lab (Mini Project)

### 🎯 Build:

* VLAN 10 (Sales)
* VLAN 20 (IT)
* Router-on-a-stick
* DHCP enabled
* NAT configured

---

## ⚙️ Full Config

Switch:

```id="fullswitch"
vlan 10
vlan 20

interface fa0/1
switchport access vlan 10

interface fa0/2
switchport access vlan 20

interface fa0/24
switchport mode trunk
```

Router:

```id="fullrouter"
interface g0/0.10
encapsulation dot1Q 10
ip address 192.168.10.1 255.255.255.0

interface g0/0.20
encapsulation dot1Q 20
ip address 192.168.20.1 255.255.255.0

ip dhcp pool VLAN10
network 192.168.10.0 255.255.255.0
default-router 192.168.10.1

ip dhcp pool VLAN20
network 192.168.20.0 255.255.255.0
default-router 192.168.20.1
```

---

## 🎯 Final Tests

```id="fulltest"
show vlan brief
show ip route
show ip dhcp binding
ping between VLANs
```

# 🧪 LABS – MINI PROJECT (FULL NETWORK)

## Packet Tracer Activities

- Combined enterprise network simulation

## Practice Tasks

- VLAN setup (10, 20)
- Trunk between switches
- Router-on-a-stick
- DHCP assignment
- NAT configuration
- End-to-end connectivity test
- Full troubleshooting simulation