from typing import Dict, List, Optional
from .base_manager import BaseManager

class IAMManager(BaseManager):
    """Manages IAM roles and policies"""
    
    def __init__(self):
        super().__init__()
        self.iam = self.session.client('iam')
        
    def create_role(self,
                   role_name: str,
                   assume_role_policy: Dict,
                   description: Optional[str] = None) -> Dict:
        """Create an IAM role"""
        try:
            params = {
                'RoleName': role_name,
                'AssumeRolePolicyDocument': str(assume_role_policy)
            }
            
            if description:
                params['Description'] = description
                
            return self.iam.create_role(**params)
            
        except Exception as e:
            self._handle_error(e, 'IAM', 'create_role')
            
    def attach_role_policy(self,
                          role_name: str,
                          policy_arn: str):
        """Attach a policy to an IAM role"""
        try:
            self.iam.attach_role_policy(
                RoleName=role_name,
                PolicyArn=policy_arn
            )
        except Exception as e:
            self._handle_error(e, 'IAM', 'attach_role_policy')
            
    def create_policy(self,
                     policy_name: str,
                     policy_document: Dict,
                     description: Optional[str] = None) -> Dict:
        """Create an IAM policy"""
        try:
            params = {
                'PolicyName': policy_name,
                'PolicyDocument': str(policy_document)
            }
            
            if description:
                params['Description'] = description
                
            return self.iam.create_policy(**params)
            
        except Exception as e:
            self._handle_error(e, 'IAM', 'create_policy')