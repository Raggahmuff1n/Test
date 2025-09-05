"""
Intelligent Scoring Engine for Azure Service Recommendations
"""

from typing import Dict, List, Tuple
import math

class IntelligentScoringEngine:
    """Advanced scoring engine with ML-inspired weighting algorithms"""
    
    def __init__(self):
        self.weight_matrix = {
            "functional_alignment": 0.30,
            "architectural_fit": 0.20,
            "compliance_match": 0.15,
            "integration_synergy": 0.15,
            "cost_efficiency": 0.10,
            "industry_relevance": 0.05,
            "innovation_factor": 0.05
        }
        
        self.requirement_patterns = {
            "high_availability": [
                "load_balancer", "failover", "redundancy", "backup", 
                "disaster_recovery", "availability_zones", "geo_redundancy"
            ],
            "security_focused": [
                "firewall", "encryption", "identity", "compliance",
                "zero_trust", "private_endpoints", "key_vault"
            ],
            "data_intensive": [
                "analytics", "big_data", "warehouse", "etl",
                "data_lake", "synapse", "databricks", "streaming"
            ],
            "modern_apps": [
                "microservices", "containers", "serverless", "api",
                "kubernetes", "docker", "functions", "app_service"
            ],
            "ai_ml": [
                "machine_learning", "cognitive", "openai", "prediction",
                "computer_vision", "nlp", "deep_learning"
            ],
            "iot_edge": [
                "iot", "edge", "telemetry", "device", "digital_twins",
                "time_series", "streaming", "event_hub"
            ],
            "hybrid_cloud": [
                "arc", "hybrid", "on_premises", "vpn", "expressroute",
                "site_recovery", "backup"
            ]
        }
        
        self.service_criticality = {
            "networking": ["Azure Virtual Network", "Azure Firewall", "Azure Application Gateway"],
            "security": ["Azure Key Vault", "Azure Active Directory", "Microsoft Defender"],
            "monitoring": ["Azure Monitor", "Application Insights", "Log Analytics"],
            "data": ["Azure SQL Database", "Azure Cosmos DB", "Azure Storage"]
        }
    
    def calculate_score(self, service: Dict, requirements: Dict, context: Dict) -> Tuple[float, Dict]:
        """
        Calculate comprehensive score with detailed breakdown
        
        Args:
            service: Azure service details
            requirements: User requirements
            context: Current architecture context
            
        Returns:
            Tuple of (total_score, score_breakdown)
        """
        
        # Detect patterns in requirements
        detected_patterns = self._detect_patterns(requirements)
        
        # Calculate individual scores
        scores = {
            "functional_alignment": self._calculate_functional_alignment(
                service, requirements, detected_patterns
            ),
            "architectural_fit": self._calculate_architectural_fit(
                service, context, detected_patterns
            ),
            "compliance_match": self._calculate_compliance_score(
                service, requirements
            ),
            "integration_synergy": self._calculate_integration_score(
                service, context
            ),
            "cost_efficiency": self._calculate_cost_efficiency(
                service, requirements
            ),
            "industry_relevance": self._calculate_industry_relevance(
                service, requirements
            ),
            "innovation_factor": self._calculate_innovation_score(
                service, detected_patterns
            )
        }
        
        # Apply dynamic weighting based on requirements
        adjusted_weights = self._adjust_weights(requirements, detected_patterns)
        
        # Calculate weighted total
        total_score = sum(
            scores[metric] * adjusted_weights[metric] 
            for metric in scores
        )
        
        return total_score * 100, scores
    
    def _detect_patterns(self, requirements: Dict) -> List[str]:
        """Detect requirement patterns from user input"""
        detected = []
        use_case = requirements.get("use_case", "").lower()
        capabilities = requirements.get("capabilities", {})
        
        for pattern, keywords in self.requirement_patterns.items():
            # Check use case text
            if any(keyword in use_case for keyword in keywords):
                detected.append(pattern)
            
            # Check selected capabilities
            for cap, selected in capabilities.items():
                if selected and any(keyword in cap.lower() for keyword in keywords):
                    if pattern not in detected:
                        detected.append(pattern)
        
        return detected
    
    def _calculate_functional_alignment(self, service: Dict, requirements: Dict, patterns: List) -> float:
        """Calculate how well service aligns with functional requirements"""
        score = 0.0
        
        # Direct use case matching
        service_use_cases = service.get("use_cases", [])
        use_case_text = requirements.get("use_case", "").lower()
        
        for use_case in service_use_cases:
            if use_case.lower() in use_case_text:
                score += 0.2
        
        # Capability matching
        capabilities = requirements.get("capabilities", {})
        capability_matches = 0
        for cap, selected in capabilities.items():
            if selected:
                cap_lower = cap.lower().replace(" ", "_")
                if any(cap_lower in uc.lower() for uc in service_use_cases):
                    capability_matches += 1
        
        if capabilities:
            score += (capability_matches / len([c for c in capabilities.values() if c])) * 0.4
        
        # Pattern bonus
        pattern_bonus = 0
        for pattern in patterns:
            pattern_keywords = self.requirement_patterns.get(pattern, [])
            if any(keyword in str(service_use_cases).lower() for keyword in pattern_keywords):
                pattern_bonus += 0.1
        
        score += min(0.4, pattern_bonus)
        
        return min(1.0, score)
    
    def _calculate_architectural_fit(self, service: Dict, context: Dict, patterns: List) -> float:
        """Calculate architectural importance and fit"""
        
        # Base importance score
        importance_scores = {
            "critical": 1.0,
            "high": 0.75,
            "medium": 0.5,
            "low": 0.25
        }
        
        base_score = importance_scores.get(
            service.get("architectural_importance", "medium"), 0.5
        )
        
        # Check if service is critical for any detected pattern
        service_name = service.get("name", "")
        
        # Critical service bonus
        for category, critical_services in self.service_criticality.items():
            if service_name in critical_services:
                base_score = max(base_score, 0.9)
        
        # Pattern-specific adjustments
        if "high_availability" in patterns:
            if service.get("category") == "Networking" or "load_balancer" in service.get("use_cases", []):
                base_score *= 1.2
        
        if "security_focused" in patterns:
            if service.get("category") == "Security & Identity":
                base_score *= 1.3
        
        if "data_intensive" in patterns:
            if service.get("category") in ["Analytics & BI", "Databases", "Storage"]:
                base_score *= 1.2
        
        return min(1.0, base_score)
    
    def _calculate_compliance_score(self, service: Dict, requirements: Dict) -> float:
        """Calculate compliance and regulatory alignment"""
        
        industry = requirements.get("industry", "")
        
        if not industry:
            return 0.5  # Neutral score if no industry specified
        
        # Industry compliance requirements (simplified)
        industry_compliance = {
            "healthcare": ["HIPAA", "HITECH", "FDA"],
            "financial": ["PCI DSS", "SOX", "GDPR"],
            "government": ["FedRAMP", "FISMA", "ITAR"],
            "retail": ["PCI DSS", "GDPR", "CCPA"]
        }
        
        required_frameworks = industry_compliance.get(industry, [])
        service_compliance = service.get("compliance", [])
        
        if not required_frameworks:
            return 0.5
        
        # Calculate compliance match
        matches = sum(1 for framework in required_frameworks if framework in service_compliance)
        score = matches / len(required_frameworks) if required_frameworks else 0.5
        
        # Bonus for security services in regulated industries
        if industry in ["healthcare", "financial", "government"]:
            if service.get("category") == "Security & Identity":
                score = min(1.0, score + 0.2)
        
        return score
    
    def _calculate_integration_score(self, service: Dict, context: Dict) -> float:
        """Calculate integration synergy with selected services"""
        
        selected_services = context.get("selected_services", [])
        integrations = service.get("integrates_with", [])
        
        if not selected_services:
            return 0.5  # Neutral score for first service
        
        # Count integration points
        integration_count = 0
        for selected in selected_services:
            if any(integration in selected or selected in integration 
                   for integration in integrations):
                integration_count += 1
        
        # Calculate synergy score
        if len(selected_services) > 0:
            synergy_ratio = integration_count / len(selected_services)
            score = 0.3 + (synergy_ratio * 0.7)
        else:
            score = 0.5
        
        return min(1.0, score)
    
    def _calculate_cost_efficiency(self, service: Dict, requirements: Dict) -> float:
        """Calculate cost efficiency based on budget sensitivity"""
        
        cost_tier = service.get("cost_tier", "medium")
        budget_sensitivity = requirements.get("budget_sensitivity", "medium")
        
        # Base cost scores
        cost_scores = {
            "free": 1.0,
            "low": 0.8,
            "medium": 0.6,
            "high": 0.4,
            "variable": 0.5
        }
        
        base_score = cost_scores.get(cost_tier, 0.5)
        
        # Adjust based on budget sensitivity
        sensitivity_multipliers = {
            "high": {"free": 1.2, "low": 1.1, "medium": 0.8, "high": 0.5, "variable": 0.7},
            "medium": {"free": 1.1, "low": 1.0, "medium": 1.0, "high": 0.9, "variable": 0.9},
            "low": {"free": 1.0, "low": 1.0, "medium": 1.0, "high": 1.0, "variable": 1.0}
        }
        
        multiplier = sensitivity_multipliers.get(budget_sensitivity, {}).get(cost_tier, 1.0)
        
        return min(1.0, base_score * multiplier)
    
    def _calculate_industry_relevance(self, service: Dict, requirements: Dict) -> float:
        """Calculate industry-specific relevance"""
        
        industry = requirements.get("industry", "")
        
        # Industry category priorities
        industry_priorities = {
            "healthcare": {
                "Security & Identity": 0.9,
                "Analytics & BI": 0.8,
                "Compliance": 0.9,
                "AI & Machine Learning": 0.7
            },
            "financial": {
                "Security & Identity": 0.9,
                "Analytics & BI": 0.9,
                "Databases": 0.8,
                "Compliance": 0.9
            },
            "retail": {
                "Analytics & BI": 0.9,
                "AI & Machine Learning": 0.8,
                "Integration & Messaging": 0.7,
                "Compute": 0.7
            },
            "manufacturing": {
                "IoT & Edge": 0.9,
                "Analytics & BI": 0.8,
                "AI & Machine Learning": 0.8,
                "Storage": 0.7
            },
            "technology": {
                "DevOps & Developer Tools": 0.9,
                "Containers": 0.9,
                "AI & Machine Learning": 0.8,
                "Compute": 0.8
            },
            "government": {
                "Security & Identity": 1.0,
                "Compliance": 1.0,
                "Monitoring & Management": 0.8,
                "Backup & Disaster Recovery": 0.8
            }
        }
        
        if industry in industry_priorities:
            service_category = service.get("category", "")
            return industry_priorities[industry].get(service_category, 0.5)
        
        return 0.5  # Neutral score if no industry match
    
    def _calculate_innovation_score(self, service: Dict, patterns: List) -> float:
        """Calculate innovation and modernization factor"""
        
        # Innovative services list
        innovative_services = [
            "Azure OpenAI Service",
            "Microsoft Fabric",
            "Azure Container Apps",
            "Azure Arc",
            "Azure Synapse Analytics",
            "Azure Digital Twins",
            "Azure Machine Learning"
        ]
        
        service_name = service.get("name", "")
        
        # Check if service is innovative
        if service_name in innovative_services:
            return 1.0
        
        # Check for modern patterns
        if "ai_ml" in patterns and "AI" in service.get("category", ""):
            return 0.8
        
        if "modern_apps" in patterns:
            if service.get("subcategory", "") in ["Serverless", "Containers", "Microservices"]:
                return 0.7
        
        # Check for cutting-edge categories
        modern_categories = ["AI & Machine Learning", "IoT & Edge", "Containers"]
        if service.get("category", "") in modern_categories:
            return 0.6
        
        return 0.3  # Base innovation score
    
    def _adjust_weights(self, requirements: Dict, patterns: List) -> Dict[str, float]:
        """Dynamically adjust weights based on requirements"""
        
        weights = self.weight_matrix.copy()
        
        # Adjust for security-focused requirements
        if "security_focused" in patterns:
            weights["compliance_match"] *= 1.3
            weights["architectural_fit"] *= 1.2
            
        # Adjust for cost-sensitive requirements
        if requirements.get("budget_sensitivity") == "high":
            weights["cost_efficiency"] *= 1.5
            
        # Adjust for innovation focus
        if "ai_ml" in patterns or "modern_apps" in patterns:
            weights["innovation_factor"] *= 1.4
        
        # Normalize weights to sum to 1.0
        total = sum(weights.values())
        return {k: v/total for k, v in weights.items()}
