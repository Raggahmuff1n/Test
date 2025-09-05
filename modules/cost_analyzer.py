"""
Advanced Cost Analysis Module
Provides detailed cost estimation and optimization recommendations
"""

from typing import Dict, List, Optional
import math
from datetime import datetime
import json

class CostAnalyzer:
    """Comprehensive cost analysis for Azure architectures"""
    
    def __init__(self):
        # Updated Azure pricing (simplified for demonstration)
        self.base_pricing = {
            # Compute
            "Azure Virtual Machines": {"hourly": 0.096, "monthly": 70},
            "Azure App Service": {"hourly": 0.075, "monthly": 55},
            "Azure Functions": {"per_million_requests": 0.20, "gb_seconds": 0.000016},
            "Azure Container Apps": {"vcpu_hour": 0.024, "memory_gb_hour": 0.003},
            "Azure Kubernetes Service (AKS)": {"node_hour": 0.10, "monthly": 73},
            
            # Storage
            "Azure Blob Storage": {"gb_month": 0.0184, "transactions_10k": 0.065},
            "Azure Data Lake Storage": {"gb_month": 0.023, "transactions_10k": 0.065},
            "Azure Files": {"gb_month": 0.058, "transactions_10k": 0.065},
            
            # Databases
            "Azure SQL Database": {"dtu_hour": 0.1518, "monthly": 110},
            "Azure Cosmos DB": {"ru_hour": 0.008, "gb_month": 0.25},
            "Azure Database for PostgreSQL": {"vcpu_hour": 0.034, "gb_month": 0.115},
            "Azure Cache for Redis": {"cache_hour": 0.022, "monthly": 16},
            
            # Analytics
            "Azure Synapse Analytics": {"dwu_hour": 1.20, "monthly": 876},
            "Azure Databricks": {"dbu_hour": 0.15, "vm_hour": 0.096},
            "Power BI": {"per_user_month": 10},
            "Azure Data Factory": {"pipeline_run": 0.001, "activity_run": 0.001},
            
            # AI/ML
            "Azure OpenAI Service": {"per_1k_tokens": 0.002},
            "Azure Machine Learning": {"compute_hour": 0.096, "monthly": 70},
            "Azure Cognitive Services": {"per_1k_transactions": 1.00},
            "Azure AI Search": {"hour": 0.336, "monthly": 245},
            
            # Networking
            "Azure Application Gateway": {"hour": 0.025, "gb_processed": 0.008},
            "Azure Load Balancer": {"hour": 0.025, "rules": 0.005},
            "Azure Firewall": {"hour": 1.25, "gb_processed": 0.016},
            "Azure Front Door": {"hour": 0.024, "gb_transferred": 0.01},
            "Azure CDN": {"gb_transferred": 0.081},
            
            # Security
            "Azure Key Vault": {"operations_10k": 0.03, "keys": 0.03},
            "Microsoft Defender for Cloud": {"vm_hour": 0.02, "monthly": 15},
            "Microsoft Sentinel": {"gb_ingested": 2.46},
            
            # Monitoring
            "Azure Monitor": {"gb_ingested": 2.30, "metrics": 0.10},
            "Application Insights": {"gb_ingested": 2.30},
            "Log Analytics": {"gb_ingested": 2.30, "gb_retained": 0.10}
        }
        
        self.discount_tiers = {
            "dev_test": 0.20,
            "reserved_1year": 0.30,
            "reserved_3year": 0.50,
            "spot_instances": 0.60,
            "hybrid_benefit": 0.40
        }
    
    def analyze(self, services: List[Dict], requirements: Dict) -> Dict:
        """
        Perform comprehensive cost analysis
        
        Args:
            services: List of selected Azure services
            requirements: User requirements including scale parameters
            
        Returns:
            Detailed cost analysis with breakdowns and recommendations
        """
        
        # Extract scale parameters
        scale = self._extract_scale_parameters(requirements)
        
        # Calculate costs for each service
        service_costs = self._calculate_service_costs(services, scale)
        
        # Calculate category totals
        category_totals = self._calculate_category_totals(service_costs)
        
        # Generate cost optimization recommendations
        optimizations = self._generate_optimizations(service_costs, scale)
        
        # Calculate potential savings
        savings = self._calculate_savings_opportunities(service_costs, scale)
        
        # Create cost forecast
        forecast = self._generate_cost_forecast(service_costs, scale)
        
        return {
            "summary": {
                "monthly_estimate": sum(s["monthly_cost"] for s in service_costs),
                "annual_estimate": sum(s["annual_cost"] for s in service_costs),
                "hourly_rate": sum(s["hourly_cost"] for s in service_costs),
                "daily_rate": sum(s["hourly_cost"] for s in service_costs) * 24
            },
            "service_breakdown": service_costs,
            "category_totals": category_totals,
            "optimization_recommendations": optimizations,
            "savings_opportunities": savings,
            "forecast": forecast,
            "assumptions": scale,
            "generated_at": datetime.now().isoformat()
        }
    
    def _extract_scale_parameters(self, requirements: Dict) -> Dict:
        """Extract and normalize scale parameters"""
        
        return {
            "users": requirements.get("expected_users", 1000),
            "transactions_per_day": requirements.get("transactions_per_day", 10000),
            "data_volume_gb": requirements.get("data_volume_gb", 500),
            "team_size": requirements.get("team_size", 10),
            "availability": requirements.get("availability", "standard"),  # standard, high, maximum
            "environment": requirements.get("environment", "production"),  # dev, staging, production
            "regions": requirements.get("regions", 1),
            "backup_retention_days": requirements.get("backup_retention", 30),
            "compliance_level": requirements.get("compliance_level", "standard")
        }
    
    def _calculate_service_costs(self, services: List[Dict], scale: Dict) -> List[Dict]:
        """Calculate costs for each service based on scale"""
        
        service_costs = []
        
        for service in services:
