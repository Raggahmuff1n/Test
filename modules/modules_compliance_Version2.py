"""
Compliance and Security Validation Module
"""

from typing import Dict, List

class ComplianceValidator:
    """Validate architecture compliance and security"""
    
    def validate(self, services: List[Dict], requirements: Dict) -> Dict:
        """Validate architecture compliance"""
        
        critical_gaps = []
        warnings = []
        recommendations = []
        
        service_names = [s["name"] for s in services]
        
        # Essential security checks
        if "Azure Key Vault" not in service_names:
            critical_gaps.append("Missing Azure Key Vault for secrets management")
            recommendations.append("Add Azure Key Vault to securely manage secrets and certificates")
        
        if not any("Azure Active Directory" in name or "Entra" in name for name in service_names):
            critical_gaps.append("Missing identity management service")
            recommendations.append("Add Azure Active Directory for identity and access management")
        
        if "Azure Monitor" not in service_names:
            warnings.append("No monitoring solution configured")
            recommendations.append("Add Azure Monitor for observability")
        
        # Network security checks
        has_compute = any(s.get("category") in ["Compute", "Containers"] for s in services)
        has_network_security = any("Firewall" in s["name"] or "Network Security" in s["name"] for s in services)
        
        if has_compute and not has_network_security:
            warnings.append("Compute resources without network security")
            recommendations.append("Consider adding Azure Firewall or Network Security Groups")
        
        return {
            "critical_gaps": critical_gaps,
            "warnings": warnings,
            "recommendations": recommendations,
            "compliance_score": self._calculate_compliance_score(services, requirements)
        }
    
    def _calculate_compliance_score(self, services: List[Dict], requirements: Dict) -> float:
        """Calculate overall compliance score"""
        score = 0.5  # Base score
        
        # Check for security services
        service_names = [s["name"] for s in services]
        if "Azure Key Vault" in service_names:
            score += 0.15
        if "Azure Monitor" in service_names:
            score += 0.15
        if any("Firewall" in name for name in service_names):
            score += 0.1
        if any("Defender" in name for name in service_names):
            score += 0.1
        
        return min(1.0, score)