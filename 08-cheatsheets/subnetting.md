# SUBNETTING CHEATSHEET

## CIDR
 * /24 = 256 IPs
 * /25 = 128 IPs
 * /26 = 64 IPs
 * /27 = 32 IPs
 * /28 = 16 IPs

👉 CIDR refers to a method used to allocate IP addresses and route internet traffic.

---

## Formula
Hosts = 2^n - 2

---

## Example
/26 = 64 - 2 = 62 usable hosts

## Subnetting Reference Guide

Subnet Mask        |    CIDR   |                 Binary Notation               |   Available Addresses
-------------------|-----------|-----------------------------------------------|--------------------------
255.255.255.255    |     /32   |      11111111.11111111.11111111.11111111      |           1
255.255.255.254    |     /31   |      11111111.11111111.11111111.11111110      |           2
255.255.255.252    |     /30   |      11111111.11111111.11111111.11111100      |           4
255.255.255.248    |     /29   |      11111111.11111111.11111111.11111000      |           8
255.255.255.240    |     /28   |      11111111.11111111.11111111.11110000      |           16
255.255.255.224    |     /27   |      11111111.11111111.11111111.11100000      |           32
255.255.255.192    |     /26   |      11111111.11111111.11111111.11000000      |           64
255.255.255.128    |     /25   |      11111111.11111111.11111111.10000000      |           128
255.255.255.0      |     /24   |      11111111.11111111.11111111.00000000      |           256
255.255.254.0      |     /23   |      11111111.11111111.11111110.00000000      |           512
255.255.252.0      |     /22   |      11111111.11111111.11111100.00000000      |           "1,024"
255.255.248.0      |     /21   |      11111111.11111111.11111000.00000000      |           "2,048"
255.255.240.0      |     /20   |      11111111.11111111.11110000.00000000      |           "4,096"
255.255.224.0      |     /19   |      11111111.11111111.11100000.00000000      |           "8,192"
255.255.192.0      |     /18   |      11111111.11111111.11000000.00000000      |           "16,384"
255.255.128.0      |     /17   |      11111111.11111111.10000000.00000000      |           "32,768"
255.255.0.0        |     /16   |      11111111.11111111.00000000.00000000      |           "65,536"
255.254.0.0        |     /15   |      11111111.11111110.00000000.00000000      |           "131,072"
255.252.0.0        |     /14   |      11111111.11111100.00000000.00000000      |           "262,144"
255.248.0.0        |     /13   |      11111111.11111000.00000000.00000000      |           "524,288"
255.240.0.0        |     /12   |      11111111.11110000.00000000.00000000      |           "1,048,576"
255.224.0.0        |     /11   |      11111111.11100000.00000000.00000000      |           "2,097,152"
255.192.0.0        |     /10   |      11111111.11000000.00000000.00000000      |           "4,194,304"
255.128.0.0        |     /9    |      11111111.10000000.00000000.00000000      |           "8,388,608"
255.0.0.0          |     /8    |      11111111.00000000.00000000.00000000      |           "16,777,216"
254.0.0.0          |     /7    |      11111110.00000000.00000000.00000000      |           "33,554,432"
252.0.0.0          |     /6    |      11111100.00000000.00000000.00000000      |           "67,108,864"
248.0.0.0          |     /5    |      11111000.00000000.00000000.00000000      |           "134,217,728"
240.0.0.0          |     /4    |      11110000.00000000.00000000.00000000      |           "268,435,456"
224.0.0.0          |     /3    |      11100000.00000000.00000000.00000000      |           "536,870,912"
192.0.0.0          |     /2    |      11000000.00000000.00000000.00000000      |           "1,073,741,824"
128.0.0.0          |     /1    |      10000000.00000000.00000000.00000000      |           "2,147,483,648"
0.0.0.0            |     /0    |      00000000.00000000.00000000.00000000      |           "4,294,967,296"

---

# IPv4 Subnetting Reference Guide

This comprehensive reference guide covers IPv4 subnet sizes, private IP ranges, binary calculations, classes, and a complete CIDR subnetting table.

---

## Subnets Size (Visual Breakdown)

A visual representation of how a single network block splits into smaller subnets:
* **/25**: Consumes 50% of the space (128 addresses)
* **/26**: Consumes 25% of the space (64 addresses)
* **/27**: Consumes 12.5% of the space (32 addresses)
* **/28**: Consumes 6.25% of the space (16 addresses)
* **/29, /31, etc.**: Remaining fractional allocations

---

## Private IPv4 Ranges

| Prefix | Ranges |
| :--- | :--- |
| **10.0.0.0/8** | 10.0.0.0 – 10.255.255.255 |
| **172.16.0.0/12** | 172.16.0.0 – 172.31.255.255 |
| **192.168.0.0/16** | 192.168.0.0 – 192.168.255.255 |

---

## Binary Calculation

| Subnet Mask Octet | Binary Equivalent | Wildcard Octet | Binary Equivalent |
| :--- | :--- | :--- | :--- |
| **255** | `1111 1111` | **0** | `0000 0000` |
| **254** | `1111 1111` | **1** | `0000 0001` |
| **252** | `1111 1100` | **3** | `0000 0011` |
| **248** | `1111 1000` | **7** | `0000 0111` |
| **240** | `1111 0000` | **15** | `0000 1111` |
| **224** | `1110 0000` | **31** | `0001 1111` |
| **192** | `1100 0000` | **63** | `0011 1111` |
| **128** | `1000 0000` | **127** | `0111 1111` |
| **0** | `0000 0000` | **255** | `1111 1111` |

---

## IPv4 Classes

| Classes | Ranges |
| :--- | :--- |
| **A** | 0.0.0.0 – 127.255.255.255 |
| **B** | 128.0.0.0 – 191.255.255.255 |
| **C** | 192.0.0.0 – 223.255.255.255 |

---

## Subnetting Table (CIDR Reference)

| CIDR | Subnet Mask | Wildcard | Total Addresses |
| :--- | :--- | :--- | :--- |
| **/32** | 255.255.255.255 | 0.0.0.0 | 1 |
| **/31** | 255.255.255.254 | 0.0.0.1 | 2 |
| **/30** | 255.255.255.252 | 0.0.0.3 | 4 |
| **/29** | 255.255.255.248 | 0.0.0.7 | 8 |
| **/28** | 255.255.255.240 | 0.0.0.15 | 16 |
| **/27** | 255.255.255.224 | 0.0.0.31 | 32 |
| **/26** | 255.255.255.192 | 0.0.0.63 | 64 |
| **/25** | 255.255.255.128 | 0.0.0.127 | 128 |
| **/24** | 255.255.255.0 | 0.0.0.255 | 256 |
| **/23** | 255.255.254.0 | 0.0.1.255 | 512 |
| **/22** | 255.255.252.0 | 0.0.3.255 | 1,024 |
| **/21** | 255.255.248.0 | 0.0.7.255 | 2,048 |
| **/20** | 255.255.240.0 | 0.0.15.255 | 4,096 |
| **/19** | 255.255.224.0 | 0.0.31.255 | 8,192 |
| **/18** | 255.255.192.0 | 0.0.63.255 | 16,384 |
| **/17** | 255.255.128.0 | 0.0.127.255 | 32,768 |
| **/16** | 255.255.0.0 | 0.0.255.255 | 65,536 |
| **/15** | 255.254.0.0 | 0.1.255.255 | 131,072 |
| **/14** | 255.252.0.0 | 0.3.255.255 | 262,144 |
| **/13** | 255.248.0.0 | 0.7.255.255 | 524,288 |
| **/12** | 255.240.0.0 | 0.15.255.255 | 1,048,576 |
| **/11** | 255.224.0.0 | 0.31.255.255 | 2,097,152 |
| **/10** | 255.192.0.0 | 0.63.255.255 | 4,194,304 |
| **/9** | 255.128.0.0 | 0.127.255.255 | 8,388,608 |
| **/8** | 255.0.0.0 | 0.255.255.255 | 16,777,216 |
| **/7** | 254.0.0.0 | 1.255.255.255 | 33,554,432 |
| **/6** | 252.0.0.0 | 3.255.255.255 | 67,108,864 |
| **/5** | 248.0.0.0 | 7.255.255.255 | 134,217,728 |
| **/4** | 240.0.0.0 | 15.255.255.255 | 268,435,456 |
| **/3** | 224.0.0.0 | 31.255.255.255 | 536,870,912 |
| **/2** | 192.0.0.0 | 63.255.255.255 | 1,073,874,824 |
| **/1** | 128.0.0.0 | 127.255.255.255 | 2,147,483,648 |
| **/0** | 0.0.0.0 | 255.255.255.255 | 4,294,967,296 |

---


# Subnet Mask Cheat Sheet
Your quick reference guide to subnet masks, CIDR, and IP ranges.

---

## What is a Subnet Mask?
A subnet mask divides an IP address into two parts: **Network Portion** and **Host Portion**.

* **Network Portion:** Identifies the network.
* **Host Portion:** Identifies the hosts on that network.

### Example
* **IP Address:** 192.168.1.10
* **Subnet Mask:** 255.255.255.0 (/24)

       Network (24 bits)              Host (8 bits)
┌───────────────────────────────┐ ┌───────────┐
11000000 . 10101000 . 00000001 .   00001010



---

## How to Read a Subnet Mask

1. Count the 1s $\rightarrow$ Network bits
2. Count the 0s $\rightarrow$ Host bits
3. CIDR = number of 1s
4. Usable Hosts = $2^{\text{host bits}} - 2$

### Example: 255.255.255.192

* **Binary:** `11111111.11111111.11111111.11000000`
* **CIDR:** /26 (26 ones)
* **Host bits:** 6
* **Usable Hosts:** $2^6 - 2 = 62$

> **NOTE:** /31 and /32 are special cases.
> * `/31` is commonly used for point-to-point links and has 2 usable addresses.
> * `/32` represents a single host address.
> 
> 

---

## Subnet Mask Reference Table

| CIDR Notation | Subnet Mask | Wildcard Mask (Used in ACL) | Total IPs per Subnet | Usable Hosts per Subnet | Use Case Example |
| --- | --- | --- | --- | --- | --- |
| **/32** | 255.255.255.255 | 0.0.0.0 | 1 | 1 | Loopback |
| **/31** | 255.255.255.254 | 0.0.0.1 | 2 | 2 | Point-to-Point |
| **/30** | 255.255.255.252 | 0.0.0.3 | 4 | 2 | P2P Links |
| **/29** | 255.255.255.248 | 0.0.0.7 | 8 | 6 | Small Networks |
| **/28** | 255.255.255.240 | 0.0.0.15 | 16 | 14 | Small LAN |
| **/27** | 255.255.255.224 | 0.0.0.31 | 32 | 30 | Small Office |
| **/26** | 255.255.255.192 | 0.0.0.63 | 64 | 62 | Department LAN |
| **/25** | 255.255.255.128 | 0.0.0.127 | 128 | 126 | Large LAN |
| **/24** | 255.255.255.0 | 0.0.0.255 | 256 | 254 | Default Class C |
| **/23** | 255.255.254.0 | 0.0.1.255 | 512 | 510 | Large Network |
| **/22** | 255.255.252.0 | 0.0.3.255 | 1,024 | 1,022 | Large Network |
| **/21** | 255.255.248.0 | 0.0.7.255 | 2,048 | 2,046 | Large Network |
| **/20** | 255.255.240.0 | 0.0.15.255 | 4,096 | 4,094 | Large Network |
| **/19** | 255.255.224.0 | 0.0.31.255 | 8,192 | 8,190 | Large Network |
| **/17** | 255.255.192.0 | 0.0.63.255 | 16,384 | 16,382 | Large Network |
| **/17** | 255.255.128.0 | 0.0.127.255 | 32,768 | 32,766 | Large Network |
| **/16** | 255.255.0.0 | 0.0.255.255 | 65,536 | 65,534 | Default Class B |
| **/8** | 255.0.0.0 | 0.255.255.255 | 16,777,216 | 16,777,214 | Default Class A |
| **/0** | 0.0.0.0 | 255.255.255.255 | All IPv4 addresses | N/A | Default Route |

---

## Block Size (Magic Number) Explained

$$\text{Magic Number} = 256 - \text{subnet mask value in the changing octet}$$


It tells you how subnet ranges increase.

### Example 1: /26 $\rightarrow$ 255.255.255.192

* Changing octet: 4th octet
* Magic Number: $256 - 192 = 64$
* Subnet ranges increase by 64:

```text
0              64             128            192            255
├── Subnet 1 ──┼── Subnet 2 ──┼── Subnet 3 ──┼── Subnet 4 ──┤
│    0 - 63    │   64 - 127   │  128 - 191   │  192 - 255   │

```

### Example 2: /23 $\rightarrow$ 255.255.254.0

* Changing octet: 3rd octet
* Magic Number: $256 - 254 = 2$
* Subnet ranges increase by 2 in the 3rd octet:
`192.168.0.0/23`, `192.168.2.0/23`, `192.168.4.0/23`, `192.168.6.0/23` ...

---

## Subnet Calculation Example

* **Given Network:** 192.168.1.0/26
* **Subnet Mask:** 255.255.255.192
* **Total IPs:** 64
* **Usable Hosts:** 62 per subnet
* **Magic Number:** 64

| Subnet | Network ID (First IP) | Usable Host Range | Broadcast ID (Last IP) |
| --- | --- | --- | --- |
| **1** | 192.168.1.0 | 192.168.1.1 – 192.168.1.62 | 192.168.1.63 |
| **2** | 192.168.1.64 | 192.168.1.65 – 192.168.1.126 | 192.168.1.127 |
| **3** | 192.168.1.128 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191 |
| **4** | 192.168.1.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255 |

---

## Subnet Mask to CIDR Quick Lookup

| Subnet Mask | CIDR | Wildcard Mask | Usable Hosts | Total IPs |
| --- | --- | --- | --- | --- |
| 255.255.255.252 | /30 | 0.0.0.3 | 2 | 4 |
| 255.255.255.248 | /29 | 0.0.0.7 | 6 | 8 |
| 255.255.255.240 | /28 | 0.0.0.15 | 14 | 16 |
| 255.255.255.224 | /27 | 0.0.0.31 | 30 | 32 |
| 255.255.255.192 | /26 | 0.0.0.63 | 62 | 64 |
| 255.255.255.128 | /25 | 0.0.0.127 | 126 | 128 |
| 255.255.255.0 | /24 | 0.0.0.255 | 254 | 256 |

---

## Subnet Mask vs. Wildcard Mask

### Subnet Mask

* Used to separate network portion and host portion.
* **1s** identify network bits.
* **0s** identify host bits.
* *Example:* `255.255.255.0 (/24)`

### Wildcard Mask

* Used in ACLs, OSPF, EIGRP, and route matching.
* **0s** mean the bit must match.
* **1s** mean the bit can vary.
* *Example:* `0.0.0.255`

$$\text{FORMULA: Wildcard Mask} = 255.255.255.255 - \text{Subnet Mask}$$

$$\text{Example: } 255.255.255.255 - 255.255.255.0 = 0.0.0.255$$

---

## Common Defaults

* **Class A Default Mask:** /8 $\rightarrow$ `255.0.0.0`
* **Class B Default Mask:** /16 $\rightarrow$ `255.255.0.0`
* **Class C Default Mask:** /24 $\rightarrow$ `255.255.255.0`
* **Loopback Range:** `127.0.0.0/8`
* **Default Route:** `0.0.0.0/0`

---

## Private IP Address Ranges

| Range | Address Range |
| --- | --- |
| **10.0.0.0/8** | 10.0.0.0 – 10.255.255.255 |
| **172.16.0.0/12** | 172.16.0.0 – 172.31.255.255 |
| **192.168.0.0/16** | 192.168.0.0 – 192.168.255.255 |

---

## Tips for Success

* Memorize common masks: `/24`, `/25`, `/26`, `/27`, `/28`, `/29`, `/30`
* Use the magic number to find subnet ranges quickly.
* Always identify Network ID and Broadcast ID first.
* Usable hosts are between the Network ID and Broadcast ID.
* For VLSM, always assign the largest host requirement first.
* Double-check subnet ranges to avoid overlap.

## Pro Tip

1. List host requirements.
2. Sort from largest to smallest.
3. Choose the smallest subnet that fits each requirement.
4. Write down Network ID, usable range, and Broadcast ID.
5. Check that no subnet overlaps.