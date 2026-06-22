import os
import json
from pathlib import Path
from typing import Dict, List, Optional, Set

class ProjectAnalyzer:
    """Analyzes project structure and content."""
    
    LANGUAGE_EXTENSIONS = {
        "Python": [".py"],
        "JavaScript": [".js", ".jsx"],
        "TypeScript": [".ts", ".tsx"],
        "Java": [".java"],
        "C++": [".cpp", ".cc", ".cxx", ".h"],
        "Go": [".go"],
        "Rust": [".rs"],
        "Ruby": [".rb"],
        "PHP": [".php"],
    }
    
    CONFIG_FILES = {
        "package.json": "Node.js",
        "requirements.txt": "Python",
        "setup.py": "Python",
        "Dockerfile": "Docker",
        "docker-compose.yml": "Docker",
        "Gemfile": "Ruby",
        "Cargo.toml": "Rust",
        "go.mod": "Go",
    }
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.exclude_dirs = [".git", "__pycache__", "node_modules", ".venv", "venv", "dist", "build"]
    
    def analyze(self, project_path: str) -> Dict:
        project_path = Path(project_path)
        if not project_path.exists():
            raise FileNotFoundError(f"Project path not found: {project_path}")
        
        return {
            "name": project_path.name,
            "path": str(project_path),
            "description": self._extract_description(project_path),
            "languages": self._detect_languages(project_path),
            "file_count": self._count_files(project_path),
            "config_files": self._find_config_files(project_path),
            "main_files": self._find_main_files(project_path),
            "license": self._detect_license(project_path),
        }
    
    def _extract_description(self, project_path: Path) -> str:
        readme = project_path / "README.md"
        if readme.exists():
            try:
                with open(readme, encoding='utf-8') as f:
                    for line in f.readlines()[:10]:
                        if line.strip() and not line.startswith("#"):
                            return line.strip()[:200]
            except:
                pass
        return "A project"
    
    def _detect_languages(self, project_path: Path) -> List[str]:
        languages: Set[str] = set()
        for root, dirs, files in os.walk(project_path):
            dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
            for file in files:
                ext = Path(file).suffix.lower()
                for lang, extensions in self.LANGUAGE_EXTENSIONS.items():
                    if ext in extensions:
                        languages.add(lang)
        return sorted(list(languages))
    
    def _count_files(self, project_path: Path) -> int:
        count = 0
        for root, dirs, files in os.walk(project_path):
            dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
            count += len(files)
        return count
    
    def _find_config_files(self, project_path: Path) -> Dict[str, str]:
        found = {}
        for config_file, desc in self.CONFIG_FILES.items():
            if (project_path / config_file).exists():
                found[config_file] = desc
        return found
    
    def _find_main_files(self, project_path: Path) -> List[str]:
        main_files = ["main.py", "index.js", "app.py", "server.js", "main.go"]
        found = []
        for f in main_files:
            if (project_path / f).exists():
                found.append(f)
        return found
    
    def _detect_license(self, project_path: Path) -> Optional[str]:
        for license_file in ["LICENSE", "LICENSE.md", "COPYING"]:
            if (project_path / license_file).exists():
                return license_file
        return None
