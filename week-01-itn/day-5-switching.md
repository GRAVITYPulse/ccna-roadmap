# Switching Basics

## What is a Switch?
A device that connects devices in a LAN using MAC addresses

---

## MAC Address Table
Switch learns:
MAC → Port mapping

---

## Behavior
1. Unknown MAC → Flood
2. Known MAC → Direct forward

---

## Command
show mac address-table

---

* MAC Address
* Switch learning process

---

## 🧠 Explanation

Switch builds a **MAC Address Table**:

Format:

```
MAC Address → Port
```

---

## 🧪 Lab

### 🎯 Goal:

Observe MAC learning

---

## ⚙️ Command

```
show mac address-table
```

---

## 🎯 Behavior

* First ping → Flood
* Next ping → Direct forwarding

---
