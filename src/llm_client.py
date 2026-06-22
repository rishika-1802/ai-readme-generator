import requests
import json
from typing import List, Dict, Optional

class OllamaClient:
    """Client for interacting with Ollama LLM."""
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.host = self.config.get("ollama_host", "http://localhost:11434")
        self.model = self.config.get("model", "mistral")
        self.temperature = self.config.get("temperature", 0.7)
        self.top_p = self.config.get("top_p", 0.9)
        self.max_tokens = self.config.get("max_tokens", 2048)
    
    def test_connection(self) -> bool:
        try:
            response = requests.get(f"{self.host}/api/tags", timeout=5)
            response.raise_for_status()
            return True
        except Exception as e:
            raise ConnectionError(f"Cannot connect to Ollama: {str(e)}")
    
    def list_models(self) -> List[str]:
        try:
            response = requests.get(f"{self.host}/api/tags", timeout=10)
            response.raise_for_status()
            data = response.json()
            models = [m["name"].split(":")[0] for m in data.get("models", [])]
            return list(set(models))
        except Exception as e:
            print(f"Error fetching models: {str(e)}")
            return []
    
    def generate(self, prompt: str, model: Optional[str] = None) -> str:
        model = model or self.model
        try:
            response = requests.post(
                f"{self.host}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "temperature": self.temperature,
                    "top_p": self.top_p,
                    "num_predict": self.max_tokens,
                    "stream": False
                },
                timeout=300
            )
            response.raise_for_status()
            data = response.json()
            return data.get("response", "").strip()
        except requests.exceptions.Timeout:
            raise TimeoutError("Generation timed out. Reduce max_tokens or use lighter model.")
        except Exception as e:
            raise RuntimeError(f"Error with Ollama: {str(e)}")
