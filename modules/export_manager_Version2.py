"""
Export Manager for generating various output formats
"""

import json
from typing import Dict, List
from datetime import datetime

class ExportManager:
    """Handle export functionality for various formats"""
    
    def prepare_export(self, requirements: Dict, services: List[Dict], 
                      patterns: List[Dict], cost_analysis: Dict, 
                      diagram: Dict) -> Dict:
        """Prepare data for export"""
        
        export_data = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "version": "1.0",
                "tool": "Azure Architecture Designer"
            },
            "requirements": requirements,
            "services": [
                {
                    "name": s.get("name"),
                    "category": s.get("category"),
                    "score": s.get("total_score", 0),
                    "importance": s.get("architectural_importance")
                }
                for s in services
            ],
            "patterns": patterns,
            "cost_analysis": cost_analysis.get("summary", {}),
            "diagram": diagram.get("mermaid", "")
        }
        
        # Add ARM template
        export_data["arm_template"] = self._generate_arm_template(services)
        
        # Add Terraform
        export_data["terraform"] = self._generate_terraform(services)
        
        return export_data
    
    def _generate_arm_template(self, services: List[Dict]) -> str:
        """Generate ARM template"""
        template = {
            "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
            "contentVersion": "1.0.0.0",
            "parameters": {},
            "variables": {},
            "resources": [],
            "outputs": {}
        }
        return json.dumps(template, indent=2)
    
    def _generate_terraform(self, services: List[Dict]) -> str:
        """Generate Terraform configuration"""
        return """
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "main" {
  name     = "rg-architecture"
  location = "East US"
}
"""
