# IPv4 Subnetting Cheatsheet

## IPv4 Structure
- 32 bits total
- 4 octets (8 bits each)
- Example: 192.168.1.1

## CIDR Notation
- /24 = 255.255.255.0
- /25 = 255.255.255.128
- /26 = 255.255.255.192
- /27 = 255.255.255.224
- /28 = 255.255.255.240

## Hosts per Subnet
- /24 = 254 hosts
- /25 = 126 hosts
- /26 = 62 hosts
- /27 = 30 hosts
- /28 = 14 hosts

## Quick Formula
Hosts = 2^(host bits) - 2

## Private IP Ranges
- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16

## Wildcard Mask
- Inverse of subnet mask
- /24 → 0.0.0.255

## Common Mistakes
- Forgetting network & broadcast address
- Wrong mask conversion
- Mixing CIDR and decimal masks