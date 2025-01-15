from typing import Dict, List, Optional
from .base_manager import BaseManager

class CloudWatchManager(BaseManager):
    """Manages CloudWatch metrics and alarms"""
    
    def __init__(self):
        super().__init__()
        self.cloudwatch = self.session.client('cloudwatch')
        
    def create_alarm(self,
                    alarm_name: str,
                    metric_name: str,
                    namespace: str,
                    comparison_operator: str,
                    threshold: float,
                    period: int,
                    evaluation_periods: int,
                    statistic: str,
                    actions: Optional[List[str]] = None) -> Dict:
        """Create a CloudWatch alarm"""
        try:
            params = {
                'AlarmName': alarm_name,
                'MetricName': metric_name,
                'Namespace': namespace,
                'ComparisonOperator': comparison_operator,
                'Threshold': threshold,
                'Period': period,
                'EvaluationPeriods': evaluation_periods,
                'Statistic': statistic
            }
            
            if actions:
                params['AlarmActions'] = actions
                
            return self.cloudwatch.put_metric_alarm(**params)
            
        except Exception as e:
            self._handle_error(e, 'CloudWatch', 'create_alarm')
            
    def put_metric_data(self,
                       namespace: str,
                       metric_data: List[Dict]):
        """Put custom metric data"""
        try:
            self.cloudwatch.put_metric_data(
                Namespace=namespace,
                MetricData=metric_data
            )
        except Exception as e:
            self._handle_error(e, 'CloudWatch', 'put_metric_data')