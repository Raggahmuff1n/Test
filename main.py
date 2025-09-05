"""
Azure Architecture Designer - Main Application
Enterprise-grade Azure architecture recommendation system
"""

import streamlit as st
import json
from datetime import datetime
from modules.scoring_engine import IntelligentScoringEngine
from modules.diagram_generator import ArchitectureDiagramGenerator
from modules.cost_analyzer import CostAnalyzer
from modules.ui_components import UIComponents
from modules.azure_services import AzureServiceCatalog
from modules.export_manager import ExportManager
from modules.compliance import ComplianceValidator
from modules.patterns import PatternDetector

# Page configuration
st.set_page_config(
    page_title="Azure Architecture Designer",
    layout="wide",
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# Initialize components
@st.cache_resource
def initialize_components():
    """Initialize all application components"""
    return {
        'scoring_engine': IntelligentScoringEngine(),
        'diagram_generator': ArchitectureDiagramGenerator(),
        'cost_analyzer': CostAnalyzer(),
        'ui': UIComponents(),
        'catalog': AzureServiceCatalog(),
        'export_manager': ExportManager(),
        'compliance': ComplianceValidator(),
        'pattern_detector': PatternDetector()
    }

def main():
    """Main application entry point"""
    
    # Initialize components
    components = initialize_components()
    ui = components['ui']
    
    # Apply professional styling
    ui.apply_professional_styling()
    
    # Render header
    ui.render_header()
    
    # Get requirements from sidebar
    requirements = ui.render_requirements_form()
    
    # Main content area
    if requirements['generate'] and requirements['use_case']:
        process_architecture_request(components, requirements)
    elif requirements['generate']:
        st.error("Please provide a use case description to generate recommendations.")
    else:
        ui.render_welcome_screen()

def process_architecture_request(components, requirements):
    """Process architecture generation request"""
    
    with st.spinner("Analyzing requirements and generating architecture..."):
        # Get Azure services
        all_services = components['catalog'].get_all_services()
        
        # Score services
        scored_services = []
        context = {"selected_services": [], "requirements": requirements}
        
        for service in all_services:
            score, breakdown = components['scoring_engine'].calculate_score(
                service, requirements, context
            )
            if score > 20:  # Minimum threshold
                service_copy = service.copy()
                service_copy['total_score'] = score
                service_copy['score_breakdown'] = breakdown
                scored_services.append(service_copy)
        
        # Sort and select top services
        scored_services.sort(key=lambda x: x['total_score'], reverse=True)
        top_services = scored_services[:25]
        
        # Update context
        context['selected_services'] = [s['name'] for s in top_services]
        
        # Detect patterns
        patterns = components['pattern_detector'].detect_patterns(
            context['selected_services'], requirements
        )
        
        # Generate cost analysis
        cost_analysis = components['cost_analyzer'].analyze(top_services, requirements)
        
        # Validate architecture
        validation_results = components['compliance'].validate(
            top_services, requirements
        )
        
        # Generate architecture diagram
        architecture_diagram = components['diagram_generator'].generate_detailed_diagram(
            top_services, patterns, requirements
        )
    
    # Display results in tabs
    render_results(
        components, 
        top_services, 
        patterns, 
        cost_analysis, 
        validation_results,
        architecture_diagram,
        requirements
    )

def render_results(components, services, patterns, cost_analysis, validation, diagram, requirements):
    """Render analysis results"""
    
    tabs = st.tabs([
        "Architecture Overview",
        "Services",
        "Network Diagram", 
        "Cost Analysis",
        "Validation",
        "Implementation",
        "Export"
    ])
    
    with tabs[0]:
        components['ui'].render_architecture_overview(services, patterns)
    
    with tabs[1]:
        components['ui'].render_service_recommendations(services)
    
    with tabs[2]:
        components['ui'].render_architecture_diagram(diagram)
    
    with tabs[3]:
        components['ui'].render_cost_analysis(cost_analysis)
    
    with tabs[4]:
        components['ui'].render_validation_results(validation)
    
    with tabs[5]:
        components['ui'].render_implementation_roadmap(services, patterns)
    
    with tabs[6]:
        export_data = components['export_manager'].prepare_export(
            requirements, services, patterns, cost_analysis, diagram
        )
        components['ui'].render_export_options(export_data)

if __name__ == "__main__":
    main()