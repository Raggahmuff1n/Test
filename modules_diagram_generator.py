"""
Advanced Architecture Diagram Generator
Creates detailed Azure architecture diagrams with networking components
"""

from typing import Dict, List, Optional
from datetime import datetime
import json

class ArchitectureDiagramGenerator:
    """Generate professional Azure architecture diagrams"""
    
    def __init__(self):
        self.diagram_styles = {
            "azure": {
                "colors": {
                    "primary": "#0078D4",
                    "secondary": "#106EBE",
                    "network": "#E3F2FD",
                    "security": "#FFEBEE",
                    "compute": "#F3E5F5",
                    "data": "#E8F5E9",
                    "monitoring": "#FFF3E0"
                },
                "fonts": {
                    "title": "Segoe UI",
                    "label": "Segoe UI Light"
                }
            }
        }
    
    def generate_detailed_diagram(self, services: List[Dict], patterns: List[Dict], 
                                requirements: Dict) -> Dict:
        """
        Generate comprehensive architecture diagram similar to Azure reference architectures
        
        Returns:
            Dictionary containing diagram code and metadata
        """
        
        # Categorize services
        categorized = self._categorize_services(services)
        
        # Determine architecture type
        arch_type = self._determine_architecture_type(patterns, requirements)
        
        # Generate appropriate diagram
        if arch_type == "microservices":
            diagram = self._generate_microservices_diagram(categorized, requirements)
        elif arch_type == "data_platform":
            diagram = self._generate_data_platform_diagram(categorized, requirements)
        elif arch_type == "ai_solution":
            diagram = self._generate_ai_solution_diagram(categorized, requirements)
        elif arch_type == "hybrid":
            diagram = self._generate_hybrid_diagram(categorized, requirements)
        else:
            diagram = self._generate_standard_diagram(categorized, requirements)
        
        return {
            "mermaid": diagram["mermaid"],
            "svg": self._generate_svg_diagram(categorized, arch_type),
            "metadata": {
                "type": arch_type,
                "generated": datetime.now().isoformat(),
                "service_count": len(services)
            }
        }
    
    def _categorize_services(self, services: List[Dict]) -> Dict:
        """Categorize services by layer and function"""
        
        categorized = {
            "frontend": [],
            "api_gateway": [],
            "compute": [],
            "containers": [],
            "data": [],
            "storage": [],
            "ai_ml": [],
            "integration": [],
            "security": [],
            "networking": [],
            "monitoring": [],
            "identity": []
        }
        
        for service in services:
            category = service.get("category", "")
            name = service.get("name", "")
            
            # Map services to architectural layers
            if "CDN" in name or "Front Door" in name:
                categorized["frontend"].append(service)
            elif "API Management" in name or "Application Gateway" in name:
                categorized["api_gateway"].append(service)
            elif category == "Compute":
                categorized["compute"].append(service)
            elif category == "Containers":
                categorized["containers"].append(service)
            elif category == "Databases":
                categorized["data"].append(service)
            elif category == "Storage":
                categorized["storage"].append(service)
            elif "AI" in category or "Machine Learning" in category:
                categorized["ai_ml"].append(service)
            elif category == "Integration & Messaging":
                categorized["integration"].append(service)
            elif category == "Security & Identity":
                if "Active Directory" in name:
                    categorized["identity"].append(service)
                else:
                    categorized["security"].append(service)
            elif category == "Networking":
                categorized["networking"].append(service)
            elif category == "Monitoring & Management":
                categorized["monitoring"].append(service)
        
        return categorized
    
    def _determine_architecture_type(self, patterns: List[Dict], requirements: Dict) -> str:
        """Determine the type of architecture to generate"""
        
        # Check patterns for architecture type
        pattern_names = [p.get("name", "").lower() for p in patterns]
        
        if any("microservice" in p for p in pattern_names):
            return "microservices"
        elif any("data" in p or "analytics" in p for p in pattern_names):
            return "data_platform"
        elif any("ai" in p or "machine learning" in p for p in pattern_names):
            return "ai_solution"
        elif any("hybrid" in p for p in pattern_names):
            return "hybrid"
        else:
            return "standard"
    
    def _generate_microservices_diagram(self, categorized: Dict, requirements: Dict) -> Dict:
        """Generate microservices architecture diagram"""
        
        lines = [
            "graph TB",
            "    %% Microservices Architecture",
            f"    %% Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "",
            "    %% External Layer",
            "    subgraph External[External Access]",
            "        Internet[Internet Users]",
            "        Mobile[Mobile Apps]",
            "        Partners[Partner Systems]",
            "    end",
            "",
            "    %% CDN and WAF Layer",
            "    subgraph CDN_WAF[Content Delivery & Security]",
            "        CDN[Azure CDN]",
            "        FrontDoor[Azure Front Door]",
            "        WAF[Web Application Firewall]",
            "    end",
            "",
            "    %% API Gateway Layer",
            "    subgraph APIGateway[API Management]",
            "        APIM[Azure API Management]",
            "        AppGW[Application Gateway]",
            "    end",
            "",
            "    %% Container Orchestration",
            "    subgraph Kubernetes[Container Platform]",
            "        subgraph AKS[Azure Kubernetes Service]",
            "            subgraph Ingress[Ingress Controller]",
            "                NGINX[NGINX Ingress]",
            "            end",
            "            subgraph Services[Microservices]",
            "                Auth[Auth Service]",
            "                Product[Product Service]",
            "                Order[Order Service]",
            "                Payment[Payment Service]",
            "                Notification[Notification Service]",
            "            end",
            "        end",
            "    end",
            "",
            "    %% Data Layer",
            "    subgraph DataLayer[Data Services]",
            "        subgraph Databases[Databases]",
            "            SQL[Azure SQL]",
            "            Cosmos[Cosmos DB]",
            "            Redis[Azure Cache for Redis]",
            "        end",
            "        subgraph Storage[Storage]",
            "            Blob[Blob Storage]",
            "            Files[Azure Files]",
            "        end",
            "    end",
            "",
            "    %% Integration Layer",
            "    subgraph Integration[Integration Services]",
            "        ServiceBus[Service Bus]",
            "        EventGrid[Event Grid]",
            "        Functions[Azure Functions]",
            "    end",
            "",
            "    %% Security & Identity",
            "    subgraph Security[Security Layer]",
            "        AAD[Azure Active Directory]",
            "        KeyVault[Key Vault]",
            "        Defender[Microsoft Defender]",
            "    end",
            "",
            "    %% Monitoring",
            "    subgraph Monitoring[Observability]",
            "        Monitor[Azure Monitor]",
            "        AppInsights[Application Insights]",
            "        LogAnalytics[Log Analytics]",
            "    end",
            "",
            "    %% Connections",
            "    Internet --> CDN",
            "    Mobile --> FrontDoor",
            "    Partners --> WAF",
            "    CDN --> APIM",
            "    FrontDoor --> APIM",
            "    WAF --> AppGW",
            "    APIM --> NGINX",
            "    AppGW --> NGINX",
            "    NGINX --> Auth",
            "    NGINX --> Product",
            "    NGINX --> Order",
            "    Auth --> KeyVault",
            "    Product --> SQL",
            "    Product --> Redis",
            "    Order --> Cosmos",
            "    Order --> ServiceBus",
            "    Payment --> ServiceBus",
            "    ServiceBus --> Functions",
            "    Functions --> Notification",
            "    Notification --> EventGrid",
            "    AKS --> Monitor",
            "    Services --> AppInsights",
            "    AAD --> APIM",
            "    AAD --> AKS",
            "",
            "    %% Styling",
            "    classDef external fill:#FFE6CC,stroke:#D79B00,stroke-width:2px",
            "    classDef network fill:#DAE8FC,stroke:#6C8EBF,stroke-width:2px",
            "    classDef compute fill:#E1D5E7,stroke:#9673A6,stroke-width:2px",
            "    classDef data fill:#D5E8D4,stroke:#82B366,stroke-width:2px",
            "    classDef security fill:#F8CECC,stroke:#B85450,stroke-width:2px",
            "    classDef monitoring fill:#FFF2CC,stroke:#D6B656,stroke-width:2px",
            "",
            "    class Internet,Mobile,Partners external",
            "    class CDN,FrontDoor,WAF,APIM,AppGW network",
            "    class AKS,Services,Auth,Product,Order,Payment,Notification compute",
            "    class SQL,Cosmos,Redis,Blob,Files data",
            "    class AAD,KeyVault,Defender security",
            "    class Monitor,AppInsights,LogAnalytics monitoring"
        ]
        
        return {"mermaid": "\n".join(lines)}
    
    def _generate_data_platform_diagram(self, categorized: Dict, requirements: Dict) -> Dict:
        """Generate data platform architecture diagram"""
        
        lines = [
            "graph LR",
            "    %% Data Platform Architecture",
            f"    %% Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "",
            "    %% Data Sources",
            "    subgraph Sources[Data Sources]",
            "        OnPrem[On-Premises Data]",
            "        SaaS[SaaS Applications]",
            "        IoT[IoT Devices]",
            "        Streaming[Streaming Data]",
            "    end",
            "",
            "    %% Ingestion Layer",
            "    subgraph Ingestion[Data Ingestion]",
            "        DataFactory[Azure Data Factory]",
            "        EventHubs[Event Hubs]",
            "        IoTHub[IoT Hub]",
            "    end",
            "",
            "    %% Storage Layer",
            "    subgraph Storage[Storage Layer]",
            "        DataLake[Data Lake Storage Gen2]",
            "        subgraph Zones[Data Zones]",
            "            Raw[Raw Zone]",
            "            Curated[Curated Zone]",
            "            Enriched[Enriched Zone]",
            "        end",
            "    end",
            "",
            "    %% Processing Layer",
            "    subgraph Processing[Data Processing]",
            "        Synapse[Azure Synapse Analytics]",
            "        Databricks[Azure Databricks]",
            "        StreamAnalytics[Stream Analytics]",
            "    end",
            "",
            "    %% Serving Layer",
            "    subgraph Serving[Data Serving]",
            "        SQL[Azure SQL]",
            "        Cosmos[Cosmos DB]",
            "        Analysis[Analysis Services]",
            "    end",
            "",
            "    %% Analytics & AI",
            "    subgraph Analytics[Analytics & AI]",
            "        PowerBI[Power BI]",
            "        MachineLearning[Azure Machine Learning]",
            "        CognitiveServices[Cognitive Services]",
            "    end",
            "",
            "    %% Governance",
            "    subgraph Governance[Data Governance]",
            "        Purview[Microsoft Purview]",
            "        Catalog[Data Catalog]",
            "        Lineage[Data Lineage]",
            "    end",
            "",
            "    %% Security",
            "    subgraph Security[Security & Compliance]",
            "        KeyVault[Key Vault]",
            "        AAD[Azure Active Directory]",
            "        PrivateEndpoints[Private Endpoints]",
            "    end",
            "",
            "    %% Connections",
            "    OnPrem --> DataFactory",
            "    SaaS --> DataFactory",
            "    IoT --> IoTHub",
            "    Streaming --> EventHubs",
            "    DataFactory --> Raw",
            "    IoTHub --> Raw",
            "    EventHubs --> StreamAnalytics",
            "    StreamAnalytics --> Raw",
            "    Raw --> Databricks",
            "    Raw --> Synapse",
            "    Databricks --> Curated",
            "    Synapse --> Curated",
            "    Curated --> Enriched",
            "    Enriched --> SQL",
            "    Enriched --> Cosmos",
            "    Enriched --> Analysis",
            "    SQL --> PowerBI",
            "    Analysis --> PowerBI",
            "    Enriched --> MachineLearning",
            "    MachineLearning --> CognitiveServices",
            "    DataLake --> Purview",
            "    Purview --> Catalog",
            "    Catalog --> Lineage",
            "    AAD --> Synapse",
            "    AAD --> Databricks",
            "    KeyVault --> DataFactory",
            "",
            "    %% Styling",
            "    classDef source fill:#FFE6CC,stroke:#D79B00,stroke-width:2px",
            "    classDef ingestion fill:#DAE8FC,stroke:#6C8EBF,stroke-width:2px",
            "    classDef storage fill:#D5E8D4,stroke:#82B366,stroke-width:2px",
            "    classDef processing fill:#E1D5E7,stroke:#9673A6,stroke-width:2px",
            "    classDef serving fill:#F8CECC,stroke:#B85450,stroke-width:2px",
            "    classDef analytics fill:#FFF2CC,stroke:#D6B656,stroke-width:2px",
            "",
            "    class OnPrem,SaaS,IoT,Streaming source",
            "    class DataFactory,EventHubs,IoTHub ingestion",
            "    class DataLake,Raw,Curated,Enriched storage",
            "    class Synapse,Databricks,StreamAnalytics processing",
            "    class SQL,Cosmos,Analysis serving",
            "    class PowerBI,MachineLearning,CognitiveServices analytics"
        ]
        
        return {"mermaid": "\n".join(lines)}
    
    def _generate_ai_solution_diagram(self, categorized: Dict, requirements: Dict) -> Dict:
        """Generate AI solution architecture diagram similar to the provided image"""
        
        lines = [
            "graph TB",
            "    %% AI Solution Architecture - Chat with Your Data Pattern",
            f"    %% Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "",
            "    %% Document Ingestion Layer",
            "    subgraph Ingestion[Document Ingestion & Management]",
            "        subgraph DataSources[Data Sources]",
            "            Storage[Azure Storage<br/>Documents & Files]",
            "            SQL[Azure SQL Database<br/>Structured Data]",
            "            Cosmos[Azure Cosmos DB<br/>NoSQL Data]",
            "        end",
            "        ",
            "        subgraph Processing[Document Processing]",
            "            DocIntel[Azure AI Document<br/>Intelligence]",
            "            Functions[Azure Functions<br/>Processing Pipeline]",
            "        end",
            "    end",
            "",
            "    %% AI Processing Layer",
            "    subgraph AILayer[AI Processing]",
            "        OpenAI[Azure OpenAI Service<br/>GPT-4 Models]",
            "        AISearch[Azure AI Search<br/>Vector Store & Indexing]",
            "        Embeddings[Embedding Service<br/>Text Vectorization]",
            "    end",
            "",
            "    %% Application Layer",
            "    subgraph Application[Application Services]",
            "        AdminUI[Admin UI<br/>Streamlit/Python]",
            "        ChatAPI[Chat Backend<br/>Python FastAPI]",
            "        WebApp[Web Application<br/>React/TypeScript]",
            "    end",
            "",
            "    %% User Interface Layer",
            "    subgraph UserInterface[User Experience]",
            "        SpeechService[Azure Speech Service<br/>Voice Interface]",
            "        Users[End Users<br/>Chat Interface]",
            "    end",
            "",
            "    %% Supporting Services",
            "    subgraph Support[Supporting Services]",
            "        KeyVault[Azure Key Vault<br/>Secrets Management]",
            "        AAD[Azure Active Directory<br/>Authentication]",
            "        Monitor[Azure Monitor<br/>Observability]",
            "    end",
            "",
            "    %% Data Flow - Ingestion",
            "    Storage --> DocIntel",
            "    SQL --> Functions",
            "    Cosmos --> Functions",
            "    DocIntel --> Functions",
            "    Functions -->|Extract & Chunk| Embeddings",
            "    Embeddings -->|Create Vectors| AISearch",
            "",
            "    %% Data Flow - Query Processing",
            "    Users --> WebApp",
            "    WebApp --> ChatAPI",
            "    ChatAPI -->|User Query| Embeddings",
            "    Embeddings -->|Query Vector| AISearch",
            "    AISearch -->|Relevant Docs| ChatAPI",
            "    ChatAPI -->|Context + Query| OpenAI",
            "    OpenAI -->|Generated Response| ChatAPI",
            "    ChatAPI --> WebApp",
            "    WebApp --> Users",
            "",
            "    %% Voice Integration",
            "    Users -.->|Voice Input| SpeechService",
            "    SpeechService -.-> ChatAPI",
            "    ChatAPI -.-> SpeechService",
            "    SpeechService -.->|Voice Output| Users",
            "",
            "    %% Admin Flow",
            "    AdminUI --> Functions",
            "    AdminUI --> AISearch",
            "",
            "    %% Security Flow",
            "    AAD --> WebApp",
            "    AAD --> ChatAPI",
            "    AAD --> AdminUI",
            "    KeyVault --> ChatAPI",
            "    KeyVault --> Functions",
            "    Monitor --> Application",
            "",
            "    %% Styling",
            "    classDef storage fill:#E8F5E9,stroke:#4CAF50,stroke-width:2px",
            "    classDef ai fill:#E3F2FD,stroke:#2196F3,stroke-width:2px",
            "    classDef app fill:#F3E5F5,stroke:#9C27B0,stroke-width:2px",
            "    classDef user fill:#FFF3E0,stroke:#FF9800,stroke-width:2px",
            "    classDef security fill:#FFEBEE,stroke:#F44336,stroke-width:2px",
            "",
            "    class Storage,SQL,Cosmos storage",
            "    class OpenAI,AISearch,Embeddings,DocIntel ai",
            "    class AdminUI,ChatAPI,WebApp,Functions app",
            "    class SpeechService,Users user",
            "    class KeyVault,AAD,Monitor security"
        ]
        
        return {"mermaid": "\n".join(lines)}
    
    def _generate_hybrid_diagram(self, categorized: Dict, requirements: Dict) -> Dict:
        """Generate hybrid cloud architecture diagram"""
        
        lines = [
            "graph TB",
            "    %% Hybrid Cloud Architecture",
            f"    %% Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "",
            "    %% On-Premises Environment",
            "    subgraph OnPrem[On-Premises Data Center]",
            "        subgraph OnPremApps[Applications]",
            "            LegacyApp[Legacy Applications]",
            "            Database[SQL Server]",
            "            FileServer[File Servers]",
            "        end",
            "        subgraph OnPremInfra[Infrastructure]",
            "            AD[Active Directory]",
            "            VMware[VMware vSphere]",
            "            Storage[SAN Storage]",
            "        end",
            "    end",
            "",
            "    %% Connectivity Layer",
            "    subgraph Connectivity[Hybrid Connectivity]",
            "        ExpressRoute[Azure ExpressRoute]",
            "        VPNGateway[VPN Gateway]",
            "        ArcServer[Azure Arc Servers]",
            "    end",
            "",
            "    %% Azure Environment",
            "    subgraph Azure[Azure Cloud]",
            "        subgraph Management[Hybrid Management]",
            "            Arc[Azure Arc]",
            "            Policy[Azure Policy]",
            "            Monitor[Azure Monitor]",
            "        end",
            "        subgraph CloudApps[Cloud Applications]",
            "            AppService[App Service]",
            "            AKS[Azure Kubernetes]",
            "            Functions[Azure Functions]",
            "        end",
            "        subgraph Data[Data Services]",
            "            SQLManaged[SQL Managed Instance]",
            "            DataSync[Azure File Sync]",
            "            Backup[Azure Backup]",
            "        end",
            "    end",
            "",
            "    %% Disaster Recovery",
            "    subgraph DR[Disaster Recovery]",
            "        SiteRecovery[Azure Site Recovery]",
            "        BackupVault[Recovery Services Vault]",
            "    end",
            "",
            "    %% Connections",
            "    LegacyApp --> ExpressRoute",
            "    Database --> VPNGateway",
            "    FileServer --> DataSync",
            "    AD --> AAD",
            "    VMware --> ArcServer",
            "    Storage --> Backup",
            "    ExpressRoute --> Azure",
            "    VPNGateway --> Azure",
            "    ArcServer --> Arc",
            "    Arc --> Policy",
            "    Arc --> Monitor",
            "    Database --> SQLManaged",
            "    FileServer --> DataSync",
            "    OnPremApps --> SiteRecovery",
            "    SiteRecovery --> BackupVault",
            "",
            "    %% Styling",
            "    classDef onprem fill:#FFE6CC,stroke:#D79B00,stroke-width:2px",
            "    classDef connect fill:#DAE8FC,stroke:#6C8EBF,stroke-width:2px",
            "    classDef azure fill:#E1D5E7,stroke:#9673A6,stroke-width:2px",
            "    classDef dr fill:#F8CECC,stroke:#B85450,stroke-width:2px",
            "",
            "    class LegacyApp,Database,FileServer,AD,VMware,Storage onprem",
            "    class ExpressRoute,VPNGateway,ArcServer connect",
            "    class Arc,Policy,Monitor,AppService,AKS,Functions,SQLManaged,DataSync,Backup azure",
            "    class SiteRecovery,BackupVault dr"
        ]
        
        return {"mermaid": "\n".join(lines)}
    
    def _generate_standard_diagram(self, categorized: Dict, requirements: Dict) -> Dict:
        """Generate standard three-tier architecture diagram"""
        
        lines = [
            "graph TB",
            "    %% Standard Three-Tier Architecture",
            f"    %% Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "",
            "    %% External Access",
            "    Internet[Internet Users]",
            "",
            "    %% Network Security",
            "    subgraph NetworkSecurity[Network Security]",
            "        WAF[Web Application Firewall]",
            "        DDoS[DDoS Protection]",
            "    end",
            "",
            "    %% Virtual Network",
            "    subgraph VNet[Azure Virtual Network]",
            "        %% Public Subnet",
            "        subgraph PublicSubnet[Public Subnet - 10.0.1.0/24]",
            "            AppGW[Application Gateway]",
            "            Bastion[Azure Bastion]",
            "            PublicLB[Public Load Balancer]",
            "        end",
            "        ",
            "        %% Web Tier",
            "        subgraph WebTier[Web Tier Subnet - 10.0.2.0/24]",
            "            WebVMs[Web VMs<br/>Scale Set]",
            "            AppService[App Service<br/>Web Apps]",
            "        end",
            "        ",
            "        %% Application Tier",
            "        subgraph AppTier[App Tier Subnet - 10.0.3.0/24]",
            "            AppVMs[App VMs<br/>Scale Set]",
            "            Functions[Azure Functions]",
            "            InternalLB[Internal Load Balancer]",
            "        end",
            "        ",
            "        %% Data Tier",
            "        subgraph DataTier[Data Tier Subnet - 10.0.4.0/24]",
            "            SQLServer[Azure SQL Database]",
            "            Storage[Storage Account]",
            "            Redis[Azure Cache for Redis]",
            "        end",
            "        ",
            "        %% Management Subnet",
            "        subgraph MgmtSubnet[Management Subnet - 10.0.5.0/24]",
            "            JumpBox[Jump Box VM]",
            "            DevOps[DevOps Agent]",
            "        end",
            "    end",
            "",
            "    %% Security & Identity",
            "    subgraph Security[Security Services]",
            "        AAD[Azure Active Directory]",
            "        KeyVault[Key Vault]",
            "        NSG[Network Security Groups]",
            "    end",
            "",
            "    %% Monitoring",
            "    subgraph Monitoring[Monitoring & Management]",
            "        Monitor[Azure Monitor]",
            "        AppInsights[Application Insights]",
            "        LogAnalytics[Log Analytics]",
            "    end",
            "",
            "    %% Connections",
            "    Internet --> WAF",
            "    WAF --> AppGW",
            "    AppGW --> PublicLB",
            "    PublicLB --> WebVMs",
            "    PublicLB --> AppService",
            "    WebVMs --> InternalLB",
            "    AppService --> InternalLB",
            "    InternalLB --> AppVMs",
            "    InternalLB --> Functions",
            "    AppVMs --> SQLServer",
            "    AppVMs --> Storage",
            "    AppVMs --> Redis",
            "    Functions --> SQLServer",
            "    Bastion --> JumpBox",
            "    JumpBox --> WebVMs",
            "    JumpBox --> AppVMs",
            "    AAD --> VNet",
            "    KeyVault --> AppTier",
            "    NSG --> WebTier",
            "    NSG --> AppTier",
            "    NSG --> DataTier",
            "    VNet --> Monitor",
            "    AppService --> AppInsights",
            "    AppVMs --> LogAnalytics",
            "",
            "    %% Styling",
            "    classDef internet fill:#FFE6CC,stroke:#D79B00,stroke-width:2px",
            "    classDef network fill:#DAE8FC,stroke:#6C8EBF,stroke-width:2px",
            "    classDef compute fill:#E1D5E7,stroke:#9673A6,stroke-width:2px",
            "    classDef data fill:#D5E8D4,stroke:#82B366,stroke-width:2px",
            "    classDef security fill:#F8CECC,stroke:#B85450,stroke-width:2px",
            "    classDef monitoring fill:#FFF2CC,stroke:#D6B656,stroke-width:2px",
            "",
            "    class Internet internet",
            "    class WAF,DDoS,AppGW,PublicLB,InternalLB,Bastion network",
            "    class WebVMs,AppService,AppVMs,Functions,JumpBox,DevOps compute",
            "    class SQLServer,Storage,Redis data",
            "    class AAD,KeyVault,NSG security",
            "    class Monitor,AppInsights,LogAnalytics monitoring"
        ]
        
        return {"mermaid": "\n".join(lines)}
    
    def _generate_svg_diagram(self, categorized: Dict, arch_type: str) -> str:
        """Generate SVG diagram for better visual representation"""
        
        # This would generate an SVG similar to the Azure reference architecture image
        # For brevity, returning a placeholder - in production, this would use a library
        # like drawsvg or generate complex SVG markup
        
        svg_template = """
        <svg viewBox="0 0 1200 800" xmlns="http://www.w3.org/2000/svg">
            <!-- Background -->
            <rect width="1200" height="800" fill="#f5f5f5"/>
            
            <!-- Title -->
            <text x="600" y="40" font-family="Segoe UI" font-size="24" 
                  text-anchor="middle" fill="#0078D4">
                Azure Architecture: {arch_type}
            </text>
            
            <!-- Network Security Layer -->
            <g id="network-layer">
                <rect x="50" y="80" width="1100" height="100" 
                      fill="#E3F2FD" stroke="#0078D4" stroke-width="2" rx="5"/>
                <text x="600" y="110" font-family="Segoe UI" font-size="14" 
                      text-anchor="middle" fill="#323130">
                    Network Security Layer
                </text>
                <!-- Add specific components based on categorized services -->
            </g>
            
            <!-- Compute Layer -->
            <g id="compute-layer">
                <rect x="50" y="200" width="1100" height="200" 
                      fill="#F3E5F5" stroke="#9C27B0" stroke-width="2" rx="5"/>
                <text x="600" y="230" font-family="Segoe UI" font-size="14" 
                      text-anchor="middle" fill="#323130">
                    Compute & Application Layer
                </text>
                <!-- Add specific components based on categorized services -->
            </g>
            
            <!-- Data Layer -->
            <g id="data-layer">
                <rect x="50" y="420" width="1100" height="150" 
                      fill="#E8F5E9" stroke="#4CAF50" stroke-width="2" rx="5"/>
                <text x="600" y="450" font-family="Segoe UI" font-size="14" 
                      text-anchor="middle" fill="#323130">
                    Data & Storage Layer
                </text>
                <!-- Add specific components based on categorized services -->
            </g>
            
            <!-- Monitoring Layer -->
            <g id="monitoring-layer">
                <rect x="50" y="590" width="1100" height="100" 
                      fill="#FFF3E0" stroke="#FF9800" stroke-width="2" rx="5"/>
                <text x="600" y="620" font-family="Segoe UI" font-size="14" 
                      text-anchor="middle" fill="#323130">
                    Monitoring & Management
                </text>
                <!-- Add specific components based on categorized services -->
            </g>
            
            <!-- Add connection lines -->
            <g id="connections">
                <!-- Add arrows and connection lines between layers -->
            </g>
        </svg>
        """
        
        return svg_template.format(arch_type=arch_type.replace("_", " ").title())