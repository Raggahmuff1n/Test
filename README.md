# Azure Architecture Designer

Professional enterprise-grade Azure architecture recommendation system with intelligent service selection, detailed cost analysis, and comprehensive architectural diagrams.

## Features

- **Intelligent Service Recommendations** - AI-powered scoring engine that analyzes requirements and recommends optimal Azure services
- **Detailed Architecture Diagrams** - Professional diagrams showing network topology, security layers, and data flow
- **Cost Analysis & Optimization** - Real-time cost estimates with optimization recommendations
- **Compliance & Security Validation** - Industry-specific compliance checking and security best practices
- **Export Capabilities** - Generate ARM templates, Terraform configs, and detailed documentation

## Installation

```bash
# Clone the repository
git clone https://github.com/Raggahmuff1n/Azure-Decider.git
cd Azure-Decider

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run main.py
```

## Architecture

The application is built with a modular architecture:

- **main.py** - Main application entry point
- **modules/** - Core functionality modules
  - **scoring_engine.py** - Intelligent service scoring and recommendation
  - **diagram_generator.py** - Architecture diagram generation
  - **cost_analyzer.py** - Cost calculation and optimization
  - **ui_components.py** - Professional UI components
  - **azure_services.py** - Azure service catalog
  - **export_manager.py** - Export functionality
- **config/** - Configuration files
- **templates/** - ARM and Terraform templates

## Usage

1. Launch the application
2. Enter your business requirements and technical needs
3. Select industry and compliance requirements
4. Configure scale and performance parameters
5. Generate architecture recommendations
6. Review and export your custom architecture

## Contributing

Contributions are welcome! Please read our contributing guidelines before submitting PRs.

## License

MIT License - see LICENSE file for details