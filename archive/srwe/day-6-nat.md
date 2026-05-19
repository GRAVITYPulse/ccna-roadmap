# NAT

## What is NAT?
Translates private IP → public IP

---

## Config

access-list 1 permit 192.168.1.0 0.0.0.255

interface g0/0
ip nat inside

interface g0/1
ip nat outside

ip nat inside source list 1 interface g0/1 overload

* NAT translates private IP → public IP

---

## 🧠 Explanation

Without NAT:

* Private IP cannot access internet

With NAT:

* Router translates IPs

---

## 🧪 Lab

### 🎯 Goal:

Enable internet simulation

---

## ⚙️ Config

```id="nat1"
access-list 1 permit 192.168.1.0 0.0.0.255

interface g0/0
ip nat inside

interface g0/1
ip nat outside

ip nat inside source list 1 interface g0/1 overload
```

---

## 🎯 Test

* Internal devices can reach external network

---

# 🧪 LABS – NAT

## Packet Tracer Activities

- NAT Overload (PAT) lab

## Practice Tasks

- Configure inside/outside interfaces
- Enable NAT overload
- Test internet simulation access
- Verify translated IPs