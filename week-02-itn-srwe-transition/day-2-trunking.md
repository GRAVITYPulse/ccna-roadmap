# VLAN Trunking

## What is Trunk?
A link that carries multiple VLANs

---

## Protocol
802.1Q tagging

---

## Command
interface fa0/24
switchport mode trunk

* Trunk = carries multiple VLANs
* Access port = single VLAN

---

## 🧠 Explanation

Trunk ports use **802.1Q tagging** to identify VLAN traffic.

---

## 🧪 Lab

### 🎯 Goal:

Connect 2 switches using trunk

---

## ⚙️ Config

```id="trunk1"
interface fa0/24
switchport mode trunk
```

---

## 🎯 Test

* VLANs pass between switches

---
