import boto3
import logging
import yaml
from typing import Dict, Any
from pathlib import Path

class BaseManager:
    """Base class for AWS resource managers"""
    
    def __init__(self):
        self.config = self._load_config()
        self.logger = self._setup_logging()
        self.session = boto3.Session(
            profile_name=self.config['aws']['profile'],
            region_name=self.config['aws']['region']
        )
        
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from config.yaml"""
        config_path = Path('config.yaml')
        with open(config_path) as f:
            return yaml.safe_load(f)
            
    def _setup_logging(self) -> logging.Logger:
        """Configure logging"""
        logger = logging.getLogger(__name__)
        logger.setLevel(self.config['logging']['level'])
        
        handler = logging.FileHandler(self.config['logging']['file'])
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
        
    def _handle_error(self, error: Exception, resource_type: str, operation: str):
        """Handle and log AWS errors"""
        error_message = f"Error in {resource_type} during {operation}: {str(error)}"
        self.logger.error(error_message)
        raise Exception(error_message)