Example CIDR:

```
VPC: 10.0.0.0/16
```

Subnets:

```
Public Subnet
10.0.1.0/24
10.0.4.0/24

Private Subnet
10.0.2.0/24
10.0.3.0/24
```

Public subnet contains:

```
Public ALB
Bastion Host
```

Private subnet contains:

```
Frontend App Server
Users Service
Payments Service
Internal ALB
```