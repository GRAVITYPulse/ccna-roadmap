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
* L3 → IP routing → Router
* L2 → MAC delivery → Switch
