from typing import Dict, Optional
from .base_manager import BaseManager

class RDSManager(BaseManager):
    """Manages RDS databases"""
    
    def __init__(self):
        super().__init__()
        self.rds = self.session.client('rds')
        
    def create_db_instance(self,
                          db_instance_identifier: str,
                          db_engine: str,
                          db_instance_class: str,
                          master_username: str,
                          master_password: str,
                          allocated_storage: int = 20) -> Dict:
        """Create a new RDS instance"""
        try:
            params = {
                'DBInstanceIdentifier': db_instance_identifier,
                'Engine': db_engine,
                'DBInstanceClass': db_instance_class,
                'MasterUsername': master_username,
                'MasterUserPassword': master_password,
                'AllocatedStorage': allocated_storage,
                'BackupRetentionPeriod': self.config['resources']['rds']['backup_retention_days'],
                'MultiAZ': self.config['resources']['rds']['multi_az'],
                'PubliclyAccessible': False,
                'AutoMinorVersionUpgrade': True,
                'StorageEncrypted': True
            }
            
            return self.rds.create_db_instance(**params)
            
        except Exception as e:
            self._handle_error(e, 'RDS', 'create_db_instance')
            
    def delete_db_instance(self,
                          db_instance_identifier: str,
                          skip_final_snapshot: bool = False,
                          final_snapshot_identifier: Optional[str] = None):
        """Delete an RDS instance"""
        try:
            params = {
                'DBInstanceIdentifier': db_instance_identifier,
                'SkipFinalSnapshot': skip_final_snapshot
            }
            
            if not skip_final_snapshot:
                if not final_snapshot_identifier:
                    final_snapshot_identifier = f"{db_instance_identifier}-final-snapshot"
                params['FinalDBSnapshotIdentifier'] = final_snapshot_identifier
                
            self.rds.delete_db_instance(**params)
            
        except Exception as e:
            self._handle_error(e, 'RDS', 'delete_db_instance')