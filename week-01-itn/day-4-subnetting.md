# Subnetting Basics

## What is Subnetting?
Splitting one network into smaller networks

---

## CIDR Values
- /24 = 256 addresses
- /25 = 128 addresses
- /26 = 64 addresses

---

## Example
192.168.1.0/24 → split into:

- 192.168.1.0/26
- 192.168.1.64/26
- 192.168.1.128/26
- 192.168.1.192/26

---

## Why important
- Better network control
- Less broadcast traffic

* /24, /25, /26
* Subnet division

---

## 🧠 Explanation

Subnetting = dividing networks

Example:

```
192.168.1.0/24 → 4 subnets (/26)
```

Each subnet has:

* Network ID
* Host range
* Broadcast address

---

## 🧪 Lab

### 🎯 Goal:

Create 2 networks

### Networks:

* 192.168.1.0/25
* 192.168.1.128/25

---

## ⚙️ Config

```
interface g0/0
ip address 192.168.1.1 255.255.255.128
no shutdown

interface g0/1
ip address 192.168.1.129 255.255.255.128
no shutdown
```

---

## 🎯 Test

* Ping between networks

---