# Inter-VLAN Routing

## Purpose
Allow VLANs to communicate

---

## Router-on-a-stick

interface g0/0.10
encapsulation dot1Q 10
ip address 192.168.10.1 255.255.255.0

interface g0/0.20
encapsulation dot1Q 20
ip address 192.168.20.1 255.255.255.0

* VLANs need routing to communicate

---

## 🧠 Explanation

Router uses **subinterfaces**:

* One interface, multiple VLANs

---

## 🧪 Lab

### 🎯 Goal:

Allow VLAN 10 and VLAN 20 to communicate

---

## ⚙️ Config

Router:

```id="routerstick"
interface g0/0.10
encapsulation dot1Q 10
ip address 192.168.10.1 255.255.255.0

interface g0/0.20
encapsulation dot1Q 20
ip address 192.168.20.1 255.255.255.0
```

Switch:

```id="trunk2"
interface fa0/24
switchport mode trunk
```

---

## 🎯 Test

* Ping between VLANs

---

# 🧪 LABS – INTER-VLAN ROUTING

## Packet Tracer Activities

- Router-on-a-Stick configuration lab

## Practice Tasks

- Create subinterfaces on router
- Assign VLAN tags (dot1Q)
- Enable inter-VLAN communication
- Test cross-VLAN ping