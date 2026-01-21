# Checklist de Segurança e IAM

## 1. Princípio do Menor Privilégio (Least Privilege)
Em vez de dar `AdministratorAccess` ou `S3FullAccess` para o usuário do Airflow, devemos criar uma Policy personalizada:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject", "s3:ListBucket"],
            "Resource": [
                "arn:aws:s3:::nome-do-seu-bucket",
                "arn:aws:s3:::nome-do-seu-bucket/*"
            ]
        }
    ]
}