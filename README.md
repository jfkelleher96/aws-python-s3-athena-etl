# AWS S3 & Python Data Pipeline (ETL to Athena)

An end-to-end cloud data pipeline built using Python, AWS S3, and AWS Athena.

## Features
- **Data Ingestion & Cleaning:** Used `pandas` to clean, normalize string formats, and calculate tax metrics on sample orders.
- **AWS S3 Integration:** Leveraged `boto3` to programmatically transfer transformed CSV data directly into an S3 storage bucket.
- **Data Warehousing & SQL Querying:** Configured AWS Athena to map an external table over S3 raw objects to perform ad-hoc SQL analysis.

## Tech Stack
- Python (`pandas`, `boto3`)
- AWS S3 (Cloud Storage)
- AWS Athena (Serverless SQL Query Engine)
