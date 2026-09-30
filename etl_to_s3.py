import io
import boto3
import pandas as pd

# 1. Credentials & Configuration
AWS_ACCESS_KEY = "YOUR_AWS_ACCESS_KEY_ID"
AWS_SECRET_KEY = "YOUR_AWS_SECRET_ACCESS_KEY"
AWS_REGION = "us-east-1"
BUCKET_NAME = "john-kelleher-aws-python-project"

# 2. Raw Sample Data
raw_data = {
    "order_id": [101, 102, 103, 104, 105],
    "customer_name": [
        "  john doe ",
        "JANE SMITH",
        "bob johnson ",
        " Alice Brown",
        "charlie DAVIS",
    ],
    "order_amount": [150.50, 89.99, 45.00, 210.00, 12.50],
    "status": ["PENDING", "COMPLETED", "completed", "PENDING", "CANCELLED"],
}

df = pd.DataFrame(raw_data)
print("--- Raw Data ---")
print(df)

# 3. Clean & Transform with Pandas
df["customer_name"] = df["customer_name"].str.strip().str.title()
df["status"] = df["status"].str.upper().str.strip()
df["tax_amount"] = (df["order_amount"] * 0.0625).round(2)

print("\n--- Transformed Data ---")
print(df)

# 4. Save to Memory Buffer
csv_buffer = io.StringIO()
df.to_csv(csv_buffer, index=False)

# 5. Upload to S3 via Boto3
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION,
)

s3_key = "data/cleaned_orders.csv"

try:
    s3_client.put_object(
        Bucket=BUCKET_NAME, Key=s3_key, Body=csv_buffer.getvalue()
    )
    print(f"\nSuccess! Uploaded cleaned data to s3://{BUCKET_NAME}/{s3_key}")
except Exception as e:
    print(f"\nUpload failed: {e}")
