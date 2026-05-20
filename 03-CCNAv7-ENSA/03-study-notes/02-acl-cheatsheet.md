# ACL Cheatsheet

## Types
Standard ACL → source only
Extended ACL → source + destination + ports

## Rules
- Top-down processing
- First match wins
- Implicit deny at end

## Example
access-list 10 permit 192.168.1.0 0.0.0.255

## Apply
ip access-group 10 in