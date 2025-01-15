from aws_automator import S3Manager

def main():
    # Initialize S3 manager
    s3_manager = S3Manager()
    
    # List all buckets
    buckets = s3_manager.list_buckets()
    print("Current S3 buckets:")
    for bucket in buckets:
        print(f"Name: {bucket['Name']}, Created: {bucket['CreationDate']}")
        
    # Create a new bucket
    bucket_name = 'my-unique-bucket-name'  # Replace with your bucket name
    new_bucket = s3_manager.create_bucket(bucket_name)
    print(f"\nCreated new bucket: {bucket_name}")

if __name__ == '__main__':
    main()