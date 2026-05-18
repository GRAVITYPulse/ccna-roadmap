# VLANs

## What is VLAN?
Virtual LAN = logical network segmentation

---

## Purpose
- Security
- Reduce broadcast domains

---

## Example
- VLAN 10 = Sales
- VLAN 20 = IT

---

## Command
vlan 10
name SALES

* VLAN = Virtual LAN
* Purpose:

  * Separate networks logically
  * Improve security
  * Reduce broadcast domains

---

## 🧠 Explanation

A switch by default = **1 broadcast domain**

👉 VLANs split it into multiple:

* VLAN 10 → Dept A
* VLAN 20 → Dept B

Devices in different VLANs **CANNOT communicate** without a router.

---

## 🧪 Lab

### 🎯 Goal:

Create VLANs and assign ports

---

## ⚙️ Config

Switch:

```id="vlan1"
enable
conf t

vlan 10
name SALES

vlan 20
name IT

interface fa0/1
switchport mode access
switchport access vlan 10

interface fa0/2
switchport mode access
switchport access vlan 20
```

---

## 🎯 Test

* PC in VLAN 10 cannot ping PC in VLAN 20

---
