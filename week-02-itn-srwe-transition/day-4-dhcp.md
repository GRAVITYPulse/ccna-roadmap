# DHCP

## What is DHCP?
Automatically assigns IP addresses

---

## Process
Discover → Offer → Request → Acknowledge

---

## Config

ip dhcp pool LAN
network 192.168.1.0 255.255.255.0
default-router 192.168.1.1
dns-server 8.8.8.8

* DHCP automatically assigns:

  * IP
  * Subnet
  * Gateway
  * DNS

---

## 🧠 Explanation

DHCP process:

1. Discover
2. Offer
3. Request
4. Acknowledge

---

## 🧪 Lab

### 🎯 Goal:

Auto assign IPs

---

## ⚙️ Config

Router:

```id="dhcp1"
ip dhcp pool LAN
network 192.168.1.0 255.255.255.0
default-router 192.168.1.1
dns-server 8.8.8.8
```

---

## 🎯 Test

* Set PC to DHCP → gets IP

---
