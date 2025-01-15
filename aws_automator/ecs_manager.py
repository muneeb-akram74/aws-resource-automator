from typing import Dict, List, Optional
from .base_manager import BaseManager

class ECSManager(BaseManager):
    """Manages ECS clusters and services"""
    
    def __init__(self):
        super().__init__()
        self.ecs = self.session.client('ecs')
        
    def create_cluster(self,
                      cluster_name: str,
                      tags: Optional[List[Dict]] = None) -> Dict:
        """Create an ECS cluster"""
        try:
            params = {
                'clusterName': cluster_name
            }
            
            if tags:
                params['tags'] = tags
                
            return self.ecs.create_cluster(**params)
            
        except Exception as e:
            self._handle_error(e, 'ECS', 'create_cluster')
            
    def create_service(self,
                      cluster: str,
                      service_name: str,
                      task_definition: str,
                      desired_count: int,
                      launch_type: str = 'FARGATE',
                      network_configuration: Optional[Dict] = None) -> Dict:
        """Create an ECS service"""
        try:
            params = {
                'cluster': cluster,
                'serviceName': service_name,
                'taskDefinition': task_definition,
                'desiredCount': desired_count,
                'launchType': launch_type
            }
            
            if network_configuration:
                params['networkConfiguration'] = network_configuration
                
            return self.ecs.create_service(**params)
            
        except Exception as e:
            self._handle_error(e, 'ECS', 'create_service')