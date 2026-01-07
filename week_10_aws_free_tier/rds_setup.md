# RDS PostgreSQL Setup - Week 10 🐘

## Database Configuration
- **Instance Identifier**: `matheus-db-semana10`
- **Engine**: PostgreSQL 17.6 (Free Tier)
- **Endpoint**: `matheus-db-semana10.xxxx.us-east-2.rds.amazonaws.com`
- **Port**: 5432

## Security & Connectivity
- **Public Access**: Enabled (Yes)
- **Security Group**: `rds-sg-semana10`
- **Inbound Rules**: TCP 5432 allowed for my local IP.

## Status
- [x] Instance Created
- [x] Security Group Configured
- [x] Connection Tested via Python (psycopg2)