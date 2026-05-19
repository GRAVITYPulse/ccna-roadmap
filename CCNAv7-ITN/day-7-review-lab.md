# Week 1 Review Lab

* OSI Model
* TCP/UDP
* IP + Subnet
* Switching
* Routing

---

## 🧠 Explanation

End-to-end communication:

PC → Switch → Router → Network

---

## 🧪 Lab (Mini Project)

### 🎯 Topology:

* 2 PCs
* 1 Switch
* 1 Router

---

## ⚙️ Full Config

Router:

```
enable
conf t

interface g0/0
ip address 192.168.1.1 255.255.255.0
no shutdown

interface g0/1
ip address 192.168.2.1 255.255.255.0
no shutdown
```

PC1:

* IP: 192.168.1.2
* Gateway: 192.168.1.1

PC2:

* IP: 192.168.2.2
* Gateway: 192.168.2.1

---

## 🎯 Final Tests

```
ping 192.168.2.2
show ip interface brief
show ip route
show mac address-table
```

---

## Topology
- 2 PCs
- 1 Switch
- 1 Router

---

## Goal
- Understand full packet flow

---

## Commands
show ip interface brief
show ip route
show mac address-table

---

## Test
Ping between devices