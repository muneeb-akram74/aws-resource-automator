from aws_automator import EC2Manager

def main():
    # Initialize EC2 manager
    ec2_manager = EC2Manager()
    
    # List all instances
    instances = ec2_manager.list_instances()
    print("Current EC2 instances:")
    for instance in instances:
        print(f"ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
        
    # Create a new instance
    new_instance = ec2_manager.create_instance(
        ami_id='ami-12345678',  # Replace with actual AMI ID
        instance_type='t2.micro',
        key_name='my-key-pair'  # Replace with your key pair name
    )
    print(f"\nCreated new instance: {new_instance['InstanceId']}")

if __name__ == '__main__':
    main()