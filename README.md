# AWS Resource Automator

A comprehensive Python-based automation tool for managing the top 30 AWS resources using boto3. This tool follows AWS best practices and implements secure automation patterns.

## Features

- Automated management of key AWS resources:
  - EC2 instances
  - S3 buckets
  - RDS databases
  - Lambda functions
  - CloudFormation stacks
  - IAM roles and policies
  - VPC and networking
  - CloudWatch monitoring
  - ECS clusters
  - And more...

## Prerequisites

- Python 3.8+
- AWS CLI configured with appropriate credentials
- Required Python packages (see requirements.txt)

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

1. Ensure AWS credentials are properly configured:
   ```bash
   aws configure
   ```

2. Update `config.yaml` with your specific AWS settings and preferences.

## Usage

```python
from aws_automator import EC2Manager, S3Manager, RDSManager

# Example: EC2 instance management
ec2_manager = EC2Manager()
ec2_manager.list_instances()
```

## Security Best Practices

- Uses IAM roles with least privilege principle
- Implements AWS credential rotation
- Encrypts sensitive data at rest and in transit
- Follows AWS Well-Architected Framework guidelines
- Implements proper error handling and logging

## Contributing

Contributions are welcome! Please read the contributing guidelines first.

## License

MIT License - see LICENSE file for details.

## Author

Muneeb Akram# aws-resource-automator
# aws-resource-automator
