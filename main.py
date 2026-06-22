import typer
import json
from pathlib import Path
from typing import Optional
from rich.console import Console
from src.analyzer import ProjectAnalyzer
from src.llm_client import OllamaClient
from src.generator import ReadmeGenerator
from src.github_fetcher import GitHubFetcher

app = typer.Typer(help="AI README Generator using Ollama")
console = Console()

@app.command()
def generate(
    path: Optional[str] = typer.Option(None, "--path"),
    github: Optional[str] = typer.Option(None, "--github"),
    output: str = typer.Option("README.md", "--output"),
    model: str = typer.Option("mistral", "--model"),
):
    if not path and not github:
        console.print("[red]Error: Provide --path or --github[/red]")
        raise typer.Exit(1)
    
    cfg = {"model": model, "temperature": 0.7}
    
    try:
        console.print("[cyan]🚀 AI README Generator[/cyan]")
        
        if github:
            console.print(f"[yellow]📥 Fetching: {github}[/yellow]")
            fetcher = GitHubFetcher()
            project_data = fetcher.fetch_and_analyze(github)
            project_path = project_data.get("local_path")
        else:
            project_path = path
        
        analyzer = ProjectAnalyzer(config=cfg)
        project_info = analyzer.analyze(project_path)
        console.print("[green]✓ Project analyzed[/green]")
        
        llm = OllamaClient(config=cfg)
        llm.test_connection()
        console.print("[green]✓ Ollama connected[/green]")
        
        console.print("[yellow]✨ Generating README...[/yellow]")
        generator = ReadmeGenerator(llm_client=llm, config=cfg)
        readme_content = generator.generate(project_info)
        
        with open(output, "w") as f:
            f.write(readme_content)
        console.print(f"[green]✓ README saved to {output}[/green]")
        
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)

@app.command()
def test():
    console.print("[cyan]🧪 Testing Ollama...[/cyan]")
    try:
        llm = OllamaClient()
        llm.test_connection()
        console.print("[green]✓ Ollama is running[/green]")
    except Exception as e:
        console.print(f"[red]✗ Failed: {str(e)}[/red]")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
