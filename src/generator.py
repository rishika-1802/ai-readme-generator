from typing import Dict, Optional
from src.llm_client import OllamaClient

class ReadmeGenerator:
    """Generates README content using LLM."""
    
    def __init__(self, llm_client: OllamaClient, config: Optional[Dict] = None):
        self.llm = llm_client
        self.config = config or {}
    
    def generate(self, project_info: Dict, template: str = "default") -> str:
        content = f"# {project_info.get('name', 'Project')}\n\n"
        
        # Description
        languages = ", ".join(project_info.get("languages", []))
        prompt = f"Create a brief 2-3 sentence description for a {languages} project named {project_info['name']}. Only return the description."
        desc = self.llm.generate(prompt)
        content += f"## Description\n\n{desc}\n\n"
        
        # Installation
        prompt = f"Create installation instructions for a {languages} project. Use code blocks."
        install = self.llm.generate(prompt)
        content += f"## Installation\n\n{install}\n\n"
        
        # Usage
        prompt = f"Create a usage guide for a {languages} project with examples."
        usage = self.llm.generate(prompt)
        content += f"## Usage\n\n{usage}\n\n"
        
        # Contributing
        prompt = "Create contributing guidelines for an open source project."
        contrib = self.llm.generate(prompt)
        content += f"## Contributing\n\n{contrib}\n\n"
        
        # License
        license_file = project_info.get("license")
        if license_file:
            prompt = f"Create a license section mentioning {license_file}."
        else:
            prompt = "Create a MIT license section."
        lic = self.llm.generate(prompt)
        content += f"## License\n\n{lic}\n\n"
        
        return content
