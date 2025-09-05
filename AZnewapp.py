import streamlit as st
import pandas as pd
import json
from typing import Dict, List, Any, Tuple
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math

st.set_page_config(
    page_title="Azure Solution Architect Pro", 
    layout="wide", 
    page_icon="☁️",
    initial_sidebar_state="expanded"
)
# At the top of the file, after imports
st.set_page_config(
    page_title="Azure Solution Architect Pro", 
    layout="wide", 
    page_icon="☁️",
    initial_sidebar_state="expanded"
)

# Add custom CSS for professional styling
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
        background-color: #f0f2f6;
        border-radius: 5px;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #e0e2e6;
    }
    .metric-container {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #0078d4;
    }
</style>
""", unsafe_allow_html=True)

def calculate_comprehensive_score(service: Dict, requirements: Dict, architecture_context: Dict) -> Tuple[int, Dict]:
    """Enhanced scoring algorithm with improved use case alignment"""
    score_breakdown = {
        "use_case_alignment": 0,      # Increased weight: 0-30 points
        "capability_match": 0,         # 0-25 points
        "architectural_fit": 0,        # 0-15 points
        "integration_synergy": 0,      # 0-10 points
        "compliance_match": 0,         # 0-10 points
        "cost_efficiency": 0,          # 0-5 points
        "industry_relevance": 0,       # 0-5 points
    }
    
    use_case_text = requirements.get("use_case", "").lower()
    selected_capabilities = requirements.get("capabilities", {})
    industry = requirements.get("industry", "")
    
    # Enhanced use case keyword matching with weighted terms
    use_case_keywords = {
        # Data & Analytics keywords
        "analytics": ["synapse", "databricks", "data factory", "power bi", "stream analytics"],
        "data warehouse": ["synapse", "sql database", "data factory"],
        "real-time": ["stream analytics", "event hubs", "iot hub", "cosmos db"],
        "etl": ["data factory", "synapse", "databricks"],
        "data lake": ["data lake storage", "synapse", "databricks"],
        
        # AI/ML keywords
        "machine learning": ["machine learning", "databricks", "synapse", "cognitive services"],
        "ai": ["openai", "cognitive services", "machine learning", "bot service"],
        "chatbot": ["openai", "bot service", "cognitive services"],
        "generative": ["openai"],
        
        # Application keywords
        "web app": ["app service", "static web apps", "container apps"],
        "api": ["api management", "app service", "functions"],
        "microservices": ["aks", "container apps", "service bus", "api management"],
        "serverless": ["functions", "logic apps", "container apps", "event grid"],
        
        # Infrastructure keywords
        "containers": ["aks", "container registry", "container apps", "container instances"],
        "kubernetes": ["aks", "container registry"],
        "devops": ["devops", "container registry", "github actions"],
        
        # Storage keywords
        "storage": ["blob storage", "data lake storage", "files", "netapp files"],
        "database": ["sql database", "cosmos db", "postgresql", "mysql"],
        "nosql": ["cosmos db"],
        "cache": ["cache for redis"],
        
        # Security keywords
        "security": ["key vault", "defender", "sentinel", "firewall", "active directory"],
        "compliance": ["policy", "purview", "defender", "sentinel"],
        "governance": ["purview", "policy", "monitor"],
        
        # IoT keywords
        "iot": ["iot hub", "iot edge", "digital twins", "stream analytics"],
        "edge": ["iot edge", "arc"],
        
        # Integration keywords
        "integration": ["logic apps", "service bus", "event grid", "api management"],
        "messaging": ["service bus", "event grid", "event hubs"],
        "workflow": ["logic apps", "functions"]
    }
    
    # Calculate use case alignment score (0-30 points)
    service_name_lower = service["name"].lower()
    use_case_score = 0
    
    for keyword, relevant_services in use_case_keywords.items():
        if keyword in use_case_text:
            for relevant_service in relevant_services:
                if relevant_service in service_name_lower:
                    use_case_score += 6  # Strong match
                    break
    
    # Direct service name mention in use case
    if any(part in use_case_text for part in service_name_lower.split()):
        use_case_score += 10
    
    score_breakdown["use_case_alignment"] = min(30, use_case_score)
    
    # Capability matching (0-25 points)
    capability_score = 0
    service_use_cases = service.get("use_cases", [])
    
    for capability, selected in selected_capabilities.items():
        if selected:
            capability_lower = capability.lower().replace(" ", "_")
            # Check if capability matches service use cases
            if any(capability_lower in uc for uc in service_use_cases):
                capability_score += 5
            # Check category match
            if capability in service.get("description", ""):
                capability_score += 3
    
    score_breakdown["capability_match"] = min(25, capability_score)
    
    # Architectural importance (0-15 points)
    importance_map = {"critical": 15, "high": 10, "medium": 5, "low": 2}
    score_breakdown["architectural_fit"] = importance_map.get(
        service.get("architectural_importance", "medium"), 5
    )
    
    # Integration synergy (0-10 points)
    selected_services = architecture_context.get("selected_services", [])
    if selected_services:
        integration_partners = service.get("integrates_with", [])
        synergy_score = sum(2 for selected in selected_services 
                           if any(partner.lower() in selected.lower() 
                                 for partner in integration_partners))
        score_breakdown["integration_synergy"] = min(10, synergy_score)
    
    # Compliance matching (0-10 points)
    if industry and industry in INDUSTRY_COMPLIANCE:
        industry_reqs = INDUSTRY_COMPLIANCE[industry]
        service_compliance = set(service.get("compliance", []))
        required_frameworks = set(industry_reqs["compliance_frameworks"])
        
        compliance_overlap = len(service_compliance & required_frameworks)
        if service["name"] in industry_reqs["required_services"]:
            compliance_overlap += 2
        
        score_breakdown["compliance_match"] = min(10, compliance_overlap * 2)
    
    # Cost efficiency (0-5 points)
    cost_map = {"free": 5, "low": 4, "medium": 3, "high": 1, "variable": 2}
    score_breakdown["cost_efficiency"] = cost_map.get(service.get("cost_tier", "medium"), 3)
    
    # Industry relevance (0-5 points)
    if industry:
        # Industry-specific service priorities
        industry_priorities = {
            "healthcare": ["Security & Identity", "Monitoring & Management", "Analytics & BI"],
            "financial": ["Security & Identity", "Analytics & BI", "Monitoring & Management"],
            "retail": ["Analytics & BI", "AI & Machine Learning", "Integration & Messaging"],
            "manufacturing": ["IoT & Edge", "Analytics & BI", "AI & Machine Learning"],
            "technology": ["DevOps & Developer Tools", "Containers", "AI & Machine Learning"],
            "startup": ["Compute", "Databases", "DevOps & Developer Tools"]
        }
        
        if service["category"] in industry_priorities.get(industry, []):
            score_breakdown["industry_relevance"] = 5
        elif any(cat in service["category"] for cat in industry_priorities.get(industry, [])):
            score_breakdown["industry_relevance"] = 3
    
    total_score = sum(score_breakdown.values())
    return total_score, score_breakdown

# In the main() function, replace the tabs section:
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Recommended Services", 
    "Architecture Patterns", 
    "Cost Analysis", 
    "Architecture Diagram", 
    "Validation & Next Steps",
    "Business Value"
])

# Examples of replacements:
st.title("Azure Solution Architect Pro")  # Remove emoji
st.header("Requirements Gathering")  # Remove emoji
st.subheader("Scale & Requirements")  # Remove emoji

# For status indicators, use styled HTML instead of emojis:
def get_status_badge(status_type, message):
    colors = {
        "error": "#dc3545",
        "warning": "#ffc107", 
        "success": "#28a745",
        "info": "#17a2b8"
    }
    return f"""
    <div style="background-color: {colors.get(status_type, '#6c757d')}; 
                color: white; 
                padding: 0.5rem 1rem; 
                border-radius: 0.25rem; 
                margin: 0.5rem 0;">
        {message}
    </div>
    """
def display_service_card(service, index):
    """Display service in a professional card format"""
    st.markdown(f"""
    <div style="border: 1px solid #e0e0e0; 
                border-radius: 8px; 
                padding: 1.5rem; 
                margin-bottom: 1rem;
                background-color: #ffffff;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <h3 style="margin-top: 0; color: #0078d4;">
            {index}. {service['name']}
            <span style="float: right; font-size: 0.9em; color: #666;">
                Score: {service['total_score']}/100
            </span>
        </h3>
        <p><strong>Category:</strong> {service['category']} | 
           <strong>Cost Tier:</strong> {service['cost_tier'].title()}</p>
        <p>{service['description']}</p>
        <p><strong>Architectural Role:</strong> {service['data_role']}</p>
        <div style="margin-top: 1rem;">
            <a href="{service['docs']}" target="_blank" 
               style="margin-right: 1rem; color: #0078d4;">Documentation</a>
            <a href="{service['pricing']}" target="_blank" 
               style="color: #0078d4;">Pricing Details</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# In the cost analysis section:
fig = go.Figure(data=[
    go.Bar(
        x=list(cost_analysis['category_totals'].keys()),
        y=list(cost_analysis['category_totals'].values()),
        text=[f"${v:,.0f}" for v in cost_analysis['category_totals'].values()],
        textposition='auto',
        marker_color='#0078d4'
    )
])
fig.update_layout(
    title="Monthly Cost by Category",
    xaxis_title="Service Category",
    yaxis_title="Monthly Cost (USD)",
    showlegend=False,
    height=400,
    template="plotly_white"
)
st.plotly_chart(fig, use_container_width=True)


# Add at the beginning of the file
SCORING_THRESHOLDS = {
    "minimum_service_score": 15,  # Increased from 10
    "max_services_to_recommend": 15,  # Reduced from 20
    "pattern_minimum_coverage": 0.6,  # 60% coverage required
    "high_cost_threshold": 3  # Number of high-cost services to trigger warning
}
