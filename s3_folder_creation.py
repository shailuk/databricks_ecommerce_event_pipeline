import boto3

s3_client = boto3.client('s3', region_name='us-east-1')
bucket_name = 'sample_s3_bucket'

# Create the bucket
s3_client.create_bucket(Bucket=bucket_name)

# Define your structure
folders = ['customer_data', 'inventory_data', 'orders_data', 'products_data', 'shipping_data']
sub_folders = ['source/', 'archive/']

# Create the folder placeholders
for folder in folders:
    for sub in sub_folders:
        folder_path = f"{folder}/{sub}"
        print(f"Creating path: {folder_path}")
        
        s3_client.put_object(
            Bucket=bucket_name, 
            Key=folder_path
        )