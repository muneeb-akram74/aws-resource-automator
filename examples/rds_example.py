from aws_automator import RDSManager

def main():
    # Initialize RDS manager
    rds_manager = RDSManager()
    
    # Create a new RDS instance
    db_instance = rds_manager.create_db_instance(
        db_instance_identifier='my-database',
        db_engine='postgres',
        db_instance_class='db.t3.micro',
        master_username='admin',
        master_password='your-secure-password',  # Replace with secure password
        allocated_storage=20
    )
    print(f"Created new RDS instance: {db_instance['DBInstanceIdentifier']}")

if __name__ == '__main__':
    main()