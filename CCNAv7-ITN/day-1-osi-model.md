# OSI MODEL (Foundation)

## Why It Matters
- Helps troubleshoot networks
- Helps understand packet flow

* OSI 7 Layers:

  1. Application - user interaction (browser, apps)
  2. Presentation - encryption, encoding
  3. Session - session management
  4. Transport - TCP/UDP, reliability
  5. Network - IP addressing, routing
  6. Data Link - MAC addressing, switching
  7. Physical - cables, signals

## Key Idea
Data flows:
Top → Bottom → Network → Bottom → Top

* Devices:

  * Switch = Layer 2 (Data Link)
  * Router = Layer 3 (Network)

## 🧠 Explanation

The OSI Model is a **layered approach to communication**.

* Data flows:

  * Down the layers (sender)
  * Across the network
  * Up the layers (receiver)

👉 Each layer has a **specific responsibility**:

* L4 → reliability (TCP/UDP)
* L3 → IP routing
* L2 → MAC delivery

---

## 🧪 Lab

### 🎯 Goal:

Understand device roles and interfaces

### Topology:

PC → Switch → Router

---

## ⚙️ Commands

Router:

```
enable
show ip interface brief
```

Switch:

```
show mac address-table
```

---

## 🎯 Key Observations

* Interface status (up/down)
* MAC addresses learned by switch

---

# 🧪 LABS – OSI MODEL

## Packet Tracer Activities

- 3.5.5 Packet Tracer - Investigate the TCP-IP and OSI Models in Action
- 1.5.7 Packet Tracer - Network Representation

## Practice Tasks

- Identify device roles (PC, switch, router)
- Trace packet movement step-by-step
- Observe encapsulation and decapsulation
- Open Simulation Mode and track PDU flow
