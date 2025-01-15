from typing import Dict, List, Optional
from .base_manager import BaseManager

class VPCManager(BaseManager):
    """Manages VPC and networking resources"""
    
    def __init__(self):
        super().__init__()
        self.ec2 = self.session.client('ec2')
        
    def create_vpc(self,
                  cidr_block: str,
                  instance_tenancy: str = 'default',
                  tags: Optional[List[Dict]] = None) -> Dict:
        """Create a VPC"""
        try:
            params = {
                'CidrBlock': cidr_block,
                'InstanceTenancy': instance_tenancy
            }
            
            if tags:
                params['TagSpecifications'] = [{
                    'ResourceType': 'vpc',
                    'Tags': tags
                }]
                
            return self.ec2.create_vpc(**params)
            
        except Exception as e:
            self._handle_error(e, 'VPC', 'create_vpc')
            
    def create_subnet(self,
                     vpc_id: str,
                     cidr_block: str,
                     availability_zone: Optional[str] = None,
                     tags: Optional[List[Dict]] = None) -> Dict:
        """Create a subnet in a VPC"""
        try:
            params = {
                'VpcId': vpc_id,
                'CidrBlock': cidr_block
            }
            
            if availability_zone:
                params['AvailabilityZone'] = availability_zone
                
            if tags:
                params['TagSpecifications'] = [{
                    'ResourceType': 'subnet',
                    'Tags': tags
                }]
                
            return self.ec2.create_subnet(**params)
            
        except Exception as e:
            self._handle_error(e, 'VPC', 'create_subnet')