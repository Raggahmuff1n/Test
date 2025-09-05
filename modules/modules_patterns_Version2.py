"""
Architecture Pattern Detection Module
"""

from typing import Dict, List

class PatternDetector:
    """Detect and recommend architecture patterns"""
    
    def detect_patterns(self, selected_services: List[str], requirements: Dict) -> List[Dict]:
        """Detect architecture patterns based on selected services"""
        
        patterns = []
        
        # Microservices pattern
        if any("Kubernetes" in svc or "AKS" in svc for svc in selected_services):
            patterns.append({
                "name": "Microservices Architecture",
                "description": "Container-based microservices with Kubernetes orchestration",
                "completeness": "high" if len(selected_services) > 10 else "medium",
                "missing_required": [],
                "missing_recommended": ["Azure Service Bus", "Azure API Management"]
            })
        
        # Serverless pattern
        if any("Functions" in svc for svc in selected_services):
            patterns.append({
                "name": "Serverless Architecture",
                "description": "Event-driven serverless computing pattern",
                "completeness": "medium",
                "missing_required": [],
                "missing_recommended": ["Azure Event Grid", "Azure Logic Apps"]
            })
        
        # Data platform pattern
        if any("Synapse" in svc or "Data Factory" in svc for svc in selected_services):
            patterns.append({
                "name": "Modern Data Platform",
                "description": "Comprehensive data analytics and warehousing solution",
                "completeness": "medium",
                "missing_required": [],
                "missing_recommended": ["Azure Data Lake Storage", "Power BI"]
            })
        
        return patterns