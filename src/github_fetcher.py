import os
import tempfile
import subprocess
from pathlib import Path
from typing import Dict

class GitHubFetcher:
    """Fetches and analyzes GitHub repositories."""
    
    def __init__(self):
        self.temp_dir = tempfile.gettempdir()
    
    def fetch_and_analyze(self, github_url: str) -> Dict:
        parts = github_url.rstrip("/").split("/")
        if len(parts) < 2:
            raise ValueError(f"Invalid GitHub URL: {github_url}")
        
        owner = parts[-2]
        repo = parts[-1].replace(".git", "")
        local_path = Path(self.temp_dir) / f"github_{owner}_{repo}"
        
        if local_path.exists():
            subprocess.run(
                ["git", "pull"],
                cwd=str(local_path),
                capture_output=True,
                timeout=30
            )
        else:
            clone_url = f"https://github.com/{owner}/{repo}.git"
            subprocess.run(
                ["git", "clone", clone_url, str(local_path)],
                capture_output=True,
                timeout=60
            )
        
        return {
            "owner": owner,
            "repo": repo,
            "url": github_url,
            "local_path": str(local_path)
        }
