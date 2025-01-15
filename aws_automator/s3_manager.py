from typing import List, Dict, Optional
from .base_manager import BaseManager

class S3Manager(BaseManager):
    """Manages S3 buckets"""
    
    def __init__(self):
        super().__init__()
        self.s3 = self.session.client('s3')
        
    def list_buckets(self) -> List[Dict]:
        """List all S3 buckets"""
        try:
            response = self.s3.list_buckets()
            return response['Buckets']
        except Exception as e:
            self._handle_error(e, 'S3', 'list_buckets')
            
    def create_bucket(self, 
                     bucket_name: str,
                     region: Optional[str] = None) -> Dict:
        """Create a new S3 bucket"""
        try:
            region = region or self.config['aws']['region']
            
            params = {
                'Bucket': bucket_name,
                'CreateBucketConfiguration': {
                    'LocationConstraint': region
                }
            }
            
            response = self.s3.create_bucket(**params)
            
            # Enable default encryption
            self.s3.put_bucket_encryption(
                Bucket=bucket_name,
                ServerSideEncryptionConfiguration={
                    'Rules': [
                        {
                            'ApplyServerSideEncryptionByDefault': {
                                'SSEAlgorithm': self.config['resources']['s3']['default_encryption']
                            }
                        }
                    ]
                }
            )
            
            # Enable versioning if configured
            if self.config['resources']['s3']['versioning'] == 'enabled':
                self.s3.put_bucket_versioning(
                    Bucket=bucket_name,
                    VersioningConfiguration={'Status': 'Enabled'}
                )
                
            return response
            
        except Exception as e:
            self._handle_error(e, 'S3', 'create_bucket')
            
    def delete_bucket(self, bucket_name: str, force: bool = False):
        """Delete an S3 bucket"""
        try:
            if force:
                # Delete all objects and versions first
                bucket = self.session.resource('s3').Bucket(bucket_name)
                bucket.objects.all().delete()
                bucket.object_versions.all().delete()
                
            self.s3.delete_bucket(Bucket=bucket_name)
            
        except Exception as e:
            self._handle_error(e, 'S3', 'delete_bucket')