"""
Professional UI Components for Azure Architecture Designer
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, List, Optional
import pandas as pd
from datetime import datetime
import json

class UIComponents:
    """Professional UI component library"""
    
    def apply_professional_styling(self):
        """Apply professional CSS styling"""
        st.markdown("""
        <style>
            /* Professional Azure-inspired styling */
            :root {
                --primary: #0078D4;
                --secondary: #106EBE;
                --success: #107C10;
                --warning: #FFB900;
                --danger: #D83B01;
                --light: #F3F2F1;
                --dark: #323130;
            }
            
            /* Hide Streamlit branding */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            /* Professional typography */
            h1, h2, h3, h4, h5, h6 {
                font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
                color: var(--dark);
            }
            
            /* Button styling */
            .stButton > button {
                background-color: var(--primary);
                color: white;
                border: none;
                border-radius: 4px;
                padding: 0.5rem 1rem;
                font-weight: 600;
                transition: all 0.3s;
            }
            
            .stButton > button:hover {
                background-color: var(--secondary);
                transform: translateY(-1px);
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
        </style>
        """, unsafe_allow_html=True)
    
    def render_header(self):
        """Render professional header"""
        st.markdown("""
            <div style='padding: 2rem 0; border-bottom: 2px solid #0078D4;'>
                <h1 style='color: #323130; margin: 0; font-size: 2.5rem;'>
                    Azure Architecture Designer
                </h1>
                <p style='color: #605E5C; margin-top: 0.5rem; font-size: 1.1rem;'>
                    Enterprise-grade architecture recommendations powered by intelligent analysis
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    def render_requirements_form(self) -> Dict:
        """Render requirements gathering form"""
        with st.sidebar:
            st.markdown("### Requirements Analysis")
            
            use_case = st.text_area(
                "Business Requirements",
                placeholder="Describe your business needs...",
                height=120
            )
            
            industry = st.selectbox(
                "Industry Vertical",
                ["", "healthcare", "financial", "government", "retail", "manufacturing", "technology", "startup"]
            )
            
            st.markdown("### Scale & Performance")
            col1, col2 = st.columns(2)
            with col1:
                team_size = st.number_input("Team Size", 1, 1000, 10)
                data_volume = st.number_input("Data Volume (GB)", 10, 100000, 500)
            with col2:
                expected_users = st.number_input("Expected Users", 100, 10000000, 1000)
                transactions = st.number_input("Transactions/Day", 1000, 100000000, 10000)
            
            st.markdown("### Technical Capabilities")
            capabilities = {}
            capability_list = [
                "Data Warehousing", "Real-time Analytics", "Machine Learning",
                "Web Applications", "REST APIs", "Microservices"
            ]
            for cap in capability_list:
                capabilities[cap] = st.checkbox(cap)
            
            budget_sensitivity = st.select_slider(
                "Cost Sensitivity",
                options=["low", "medium", "high"],
                value="medium"
            )
            
            generate = st.button("Generate Architecture", type="primary", use_container_width=True)
            
            return {
                "use_case": use_case,
                "industry": industry,
                "capabilities": capabilities,
                "team_size": team_size,
                "expected_users": expected_users,
                "data_volume_gb": data_volume,
                "transactions_per_day": transactions,
                "budget_sensitivity": budget_sensitivity,
                "generate": generate
            }
    
    def render_welcome_screen(self):
        """Render welcome screen"""
        st.markdown("""
            <div style='background: linear-gradient(135deg, #0078D4 0%, #106EBE 100%);
                        padding: 3rem; border-radius: 8px; color: white; margin: 2rem 0;'>
                <h2 style='color: white; margin: 0;'>Welcome to Azure Architecture Designer</h2>
                <p style='color: white; margin-top: 1rem;'>
                    Design enterprise-grade Azure architectures with intelligent recommendations
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    def render_architecture_overview(self, services: List[Dict], patterns: List[Dict]):
        """Render architecture overview"""
        st.markdown("## Architecture Overview")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Services", len(services))
        with col2:
            st.metric("Critical Services", len([s for s in services if s.get("architectural_importance") == "critical"]))
        with col3:
            st.metric("Patterns Detected", len(patterns) if patterns else 0)
        with col4:
            st.metric("Categories", len(set(s.get("category", "") for s in services)))
    
    def render_service_recommendations(self, services: List[Dict]):
        """Render service recommendations"""
        st.markdown("## Recommended Services")
        for idx, service in enumerate(services[:10], 1):
            with st.expander(f"{idx}. {service['name']}"):
                st.write(f"**Category:** {service.get('category', 'N/A')}")
                st.write(f"**Description:** {service.get('description', 'N/A')}")
                if 'total_score' in service:
                    st.metric("Score", f"{service['total_score']:.0f}/100")
    
    def render_architecture_diagram(self, diagram: Dict):
        """Render architecture diagram"""
        st.markdown("## Architecture Diagram")
        st.code(diagram.get("mermaid", ""), language="mermaid")
    
    def render_cost_analysis(self, cost_analysis: Dict):
        """Render cost analysis"""
        st.markdown("## Cost Analysis")
        summary = cost_analysis.get("summary", {})
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Monthly Cost", f"${summary.get('monthly_estimate', 0):,.2f}")
        with col2:
            st.metric("Annual Cost", f"${summary.get('annual_estimate', 0):,.2f}")
        with col3:
            st.metric("Daily Rate", f"${summary.get('daily_rate', 0):,.2f}")
    
    def render_validation_results(self, validation: Dict):
        """Render validation results"""
        st.markdown("## Architecture Validation")
        if validation.get("critical_gaps"):
            for gap in validation["critical_gaps"]:
                st.error(gap)
        if validation.get("warnings"):
            for warning in validation["warnings"]:
                st.warning(warning)
        if validation.get("recommendations"):
            for rec in validation["recommendations"]:
                st.info(rec)
    
    def render_implementation_roadmap(self, services: List[Dict], patterns: List[Dict]):
        """Render implementation roadmap"""
        st.markdown("## Implementation Roadmap")
        phases = {
            "Phase 1: Foundation (Months 1-2)": [
                "Set up Azure landing zone",
                "Configure networking and security"
            ],
            "Phase 2: Core Services (Months 2-4)": [
                "Deploy compute resources",
                "Set up data layer"
            ]
        }
        for phase, tasks in phases.items():
            with st.expander(phase):
                for task in tasks:
                    st.write(f"• {task}")
    
    def render_export_options(self, export_data: Dict):
        """Render export options"""
        st.markdown("## Export Options")
        st.download_button(
            "Download JSON",
            json.dumps(export_data, indent=2),
            file_name=f"architecture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )
