"""
Comprehensive Azure Service Catalog
"""

class AzureServiceCatalog:
    """Azure service catalog with all services"""
    
    def get_all_services(self):
        """Return comprehensive list of Azure services"""
        return [
            {
                "name": "Azure Virtual Network",
                "category": "Networking",
                "subcategory": "Core Infrastructure",
                "cost_tier": "low",
                "use_cases": ["network_isolation", "hybrid_connectivity", "security", "subnets"],
                "integrates_with": ["Virtual Machines", "AKS", "Application Gateway", "Firewall"],
                "compliance": ["SOC", "HIPAA", "ISO", "FedRAMP"],
                "description": "Software-defined networking for resource isolation and connectivity",
                "architectural_importance": "critical",
                "pricing_model": "VPN Gateway + bandwidth"
            },
            {
                "name": "Azure Application Gateway",
                "category": "Networking",
                "subcategory": "Application Delivery",
                "cost_tier": "medium",
                "use_cases": ["load_balancer", "ssl_termination", "waf", "routing"],
                "integrates_with": ["Virtual Network", "AKS", "App Service", "Key Vault"],
                "compliance": ["SOC", "ISO", "PCI DSS"],
                "description": "Layer 7 load balancer with WAF capabilities",
                "architectural_importance": "high",
                "pricing_model": "Gateway hours + data processing"
            },
            {
                "name": "Azure Functions",
                "category": "Compute",
                "subcategory": "Serverless",
                "cost_tier": "low",
                "use_cases": ["serverless", "event_driven", "microservices", "api"],
                "integrates_with": ["Event Grid", "Service Bus", "Cosmos DB", "API Management"],
                "compliance": ["SOC", "ISO"],
                "description": "Event-driven serverless compute",
                "architectural_importance": "medium",
                "pricing_model": "Per execution"
            },
            {
                "name": "Azure Kubernetes Service",
                "category": "Containers",
                "subcategory": "Container Orchestration",
                "cost_tier": "medium",
                "use_cases": ["microservices", "containers", "kubernetes", "scalability"],
                "integrates_with": ["Container Registry", "Monitor", "Key Vault", "Virtual Network"],
                "compliance": ["SOC", "HIPAA", "ISO"],
                "description": "Managed Kubernetes service",
                "architectural_importance": "high",
                "pricing_model": "Node pools"
            },
            {
                "name": "Azure SQL Database",
                "category": "Databases",
                "subcategory": "Relational",
                "cost_tier": "medium",
                "use_cases": ["relational_database", "sql", "transactions", "analytics"],
                "integrates_with": ["App Service", "Functions", "Data Factory", "Synapse"],
                "compliance": ["SOC", "HIPAA", "ISO", "FedRAMP"],
                "description": "Fully managed relational database",
                "architectural_importance": "high",
                "pricing_model": "DTU or vCore"
            },
            {
                "name": "Azure Cosmos DB",
                "category": "Databases",
                "subcategory": "NoSQL",
                "cost_tier": "high",
                "use_cases": ["nosql", "global_distribution", "multi_model", "real_time"],
                "integrates_with": ["Functions", "App Service", "Synapse", "Stream Analytics"],
                "compliance": ["SOC", "HIPAA", "ISO"],
                "description": "Globally distributed multi-model database",
                "architectural_importance": "high",
                "pricing_model": "RU/s + Storage"
            },
            {
                "name": "Azure Key Vault",
                "category": "Security & Identity",
                "subcategory": "Secrets Management",
                "cost_tier": "low",
                "use_cases": ["secrets", "keys", "certificates", "encryption"],
                "integrates_with": ["All Azure Services"],
                "compliance": ["SOC", "HIPAA", "ISO", "FedRAMP"],
                "description": "Secure secrets management",
                "architectural_importance": "critical",
                "pricing_model": "Operations-based"
            },
            {
                "name": "Azure Monitor",
                "category": "Monitoring & Management",
                "subcategory": "Observability",
                "cost_tier": "medium",
                "use_cases": ["monitoring", "logging", "metrics", "alerting"],
                "integrates_with": ["All Azure Services"],
                "compliance": ["SOC", "ISO"],
                "description": "Full-stack monitoring service",
                "architectural_importance": "critical",
                "pricing_model": "Data ingestion"
            }
            # Add more services as needed...
        ]
