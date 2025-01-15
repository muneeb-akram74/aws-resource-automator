from typing import Dict, Optional
from .base_manager import BaseManager

class LambdaManager(BaseManager):
    """Manages Lambda functions"""
    
    def __init__(self):
        super().__init__()
        self.lambda_client = self.session.client('lambda')
        
    def create_function(self,
                       function_name: str,
                       runtime: str,
                       handler: str,
                       role_arn: str,
                       code: Dict,
                       environment: Optional[Dict] = None) -> Dict:
        """Create a new Lambda function"""
        try:
            params = {
                'FunctionName': function_name,
                'Runtime': runtime,
                'Role': role_arn,
                'Handler': handler,
                'Code': code,
                'Publish': True
            }
            
            if environment:
                params['Environment'] = {'Variables': environment}
                
            return self.lambda_client.create_function(**params)
            
        except Exception as e:
            self._handle_error(e, 'Lambda', 'create_function')
            
    def update_function_code(self,
                           function_name: str,
                           code: Dict) -> Dict:
        """Update Lambda function code"""
        try:
            return self.lambda_client.update_function_code(
                FunctionName=function_name,
                **code
            )
        except Exception as e:
            self._handle_error(e, 'Lambda', 'update_function_code')
            
    def delete_function(self, function_name: str):
        """Delete a Lambda function"""
        try:
            self.lambda_client.delete_function(FunctionName=function_name)
        except Exception as e:
            self._handle_error(e, 'Lambda', 'delete_function')