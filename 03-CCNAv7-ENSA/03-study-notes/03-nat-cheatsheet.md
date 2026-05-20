# NAT

## Types
- Static NAT
- Dynamic NAT
- PAT (Overload)

## Example
ip nat inside source list 1 interface g0/0 overload

## Terms
Inside Local → private IP
Inside Global → public IP

## Verify
show ip nat translations