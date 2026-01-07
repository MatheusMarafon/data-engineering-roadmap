# AWS Setup - Week 10 ☁️

## IAM Progress
- **IAM User**: Created (`airflow-worker`)
- **Access Keys**: Generated and securely stored in a CSV file (not committed)
- **Permissions**: `S3FullAccess` and `RDSFullAccess` attached

## S3 Storage Structure (Data Lake)
- **Bucket Name**: [INSIRA-AQUI-O-NOME-DO-SEU-BUCKET]
- **Region**: us-east-1 (N. Virginia)
- **Layers**:
  - `raw/`: Folder for landing/unprocessed data.
  - `processed/`: Folder for cleaned/transformed data.
- **Security**: Public Access Blocked & SSE-S3 Encryption enabled.

## Status
- [x] AWS Account Active (Free Tier)
- [x] Identity Verified
- [x] IAM User & Permissions Configured
- [x] S3 Bucket & Folders Created