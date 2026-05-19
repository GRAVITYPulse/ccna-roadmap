# TCP vs UDP

* TCP vs UDP
* Ports:

  * 80 → HTTP
  * 443 → HTTPS
  * 22 → SSH
  * 53 → DNS

## TCP
- Reliable
- Connection-oriented
- Uses 3-way handshake:
  SYN → SYN-ACK → ACK

Used for:
- Web (HTTP/HTTPS)
- Email
- SSH

## UDP
- Fast
- No guarantee delivery
- No handshake

Used for:
- Gaming
- Streaming
- DNS
---

## 🧠 Explanation

* TCP = reliable (uses acknowledgements)
* UDP = fast (no guarantee)

## 🧪 Lab

### 🎯 Goal:

Test connectivity

### Setup:

* PC: 192.168.1.2
* Router: 192.168.1.1

---

## ⚙️ Config

Router:

```
enable
configure terminal
interface g0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
```

PC:

* IP: 192.168.1.2
* Gateway: 192.168.1.1

---

## 🎯 Test

```
ping 192.168.1.1
```

# 🧪 LABS – TCP / UDP

## Packet Tracer Activities

- 14.8.1 Packet Tracer - TCP and UDP Communications
- 2.7.6 Packet Tracer - Implement Basic Connectivity

## Practice Tasks

- Compare TCP vs UDP traffic in Simulation Mode
- Observe 3-way handshake (SYN, SYN-ACK, ACK)
- Test ping vs UDP-style traffic behavior
- Identify ports used in communication