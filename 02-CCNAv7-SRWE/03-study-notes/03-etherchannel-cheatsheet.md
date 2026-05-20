# EtherChannel

## Purpose
Combine multiple links into one logical link

## Protocols
- LACP (802.3ad)
- PAgP (Cisco)

## Config
channel-group 1 mode active

## Verification
show etherchannel summary

## Benefits
- Load balancing
- Redundancy
- Increased bandwidth