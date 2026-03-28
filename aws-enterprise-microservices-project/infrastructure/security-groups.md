Internet
   |
   v
Public ALB SG
Inbound:
80 from 0.0.0.0/0

Outbound:
5050 to frontend-sg
   |
   v
Frontend SG
Inbound:
5050 from public-alb-sg

Outbound:
80 to internal-alb-sg
   |
   v
Internal ALB SG
Inbound:
80 from frontend-sg

Outbound:
5050 to microservice-sg
   |
   v
Microservice SG
Inbound:
5050 from internal-alb-sg

Outbound:
All traffic