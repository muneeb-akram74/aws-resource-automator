from typing import List, Dict, Optional
from .base_manager import BaseManager

class EC2Manager(BaseManager):
    """Manages EC2 instances"""
    
    def __init__(self):
        super().__init__()
        self.ec2 = self.session.client('ec2')
        
    def list_instances(self, filters: Optional[List[Dict]] = None) -> List[Dict]:
        """List EC2 instances with optional filters"""
        try:
            if filters:
                response = self.ec2.describe_instances(Filters=filters)
            else:
                response = self.ec2.describe_instances()
                
            instances = []
            for reservation in response['Reservations']:
                instances.extend(reservation['Instances'])
            return instances
            
        except Exception as e:
            self._handle_error(e, 'EC2', 'list_instances')
            
    def create_instance(self, 
                       ami_id: str,
                       instance_type: Optional[str] = None,
                       key_name: Optional[str] = None,
                       security_group_ids: Optional[List[str]] = None) -> Dict:
        """Create a new EC2 instance"""
        try:
            instance_type = instance_type or self.config['resources']['ec2']['default_instance_type']
            
            params = {
                'ImageId': ami_id,
                'InstanceType': instance_type,
                'MaxCount': 1,
                'MinCount': 1
            }
            
            if key_name:
                params['KeyName'] = key_name
            if security_group_ids:
                params['SecurityGroupIds'] = security_group_ids
                
            response = self.ec2.run_instances(**params)
            return response['Instances'][0]
            
        except Exception as e:
            self._handle_error(e, 'EC2', 'create_instance')
            
    def stop_instance(self, instance_id: str):
        """Stop an EC2 instance"""
        try:
            self.ec2.stop_instances(InstanceIds=[instance_id])
        except Exception as e:
            self._handle_error(e, 'EC2', 'stop_instance')
            
    def start_instance(self, instance_id: str):
        """Start an EC2 instance"""
        try:
            self.ec2.start_instances(InstanceIds=[instance_id])
        except Exception as e:
            self._handle_error(e, 'EC2', 'start_instance')
            
    def terminate_instance(self, instance_id: str):
        """Terminate an EC2 instance"""
        try:
            self.ec2.terminate_instances(InstanceIds=[instance_id])
        except Exception as e:
            self._handle_error(e, 'EC2', 'terminate_instance')