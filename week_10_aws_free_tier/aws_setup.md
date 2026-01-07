# AWS Setup - Week 10 ☁️

## IAM Progress
- **IAM User**: Created (`airflow-worker`)
- **Access Keys**: Generated and securely stored in a CSV file (not committed)
- **Permissions**: `S3FullAccess` and `RDSFullAccess` attached

## S3 Storage Structure (Data Lake)
- **Bucket Name**: matheus-datalake-semana10
- **Region**: us-east-2 (Ohio)
- **Layers**:
  - `raw/`: Folder for landing/unprocessed data.
  - `processed/`: Folder for cleaned/transformed data.
- **Security**: Public Access Blocked & SSE-S3 Encryption enabled.

## S3 Programmatic Access (Wednesday)
- **Library**: `boto3` installed and configured.
- **Utilities**: `s3_utils.py` created with upload and download functions.
- **Environment**: Credentials secured via `.env` file (ignored by git).
- **Tests**: 
  - [x] Programmatic Upload to `raw/` successful.
  - [x] Programmatic Download from S3 successful.

## Status
- [x] AWS Account Active (Free Tier)
- [x] Identity Verified
- [x] IAM User & Permissions Configured
- [x] S3 Bucket & Folders Created
- [x] Boto3 Connection Tested (Put/Get)