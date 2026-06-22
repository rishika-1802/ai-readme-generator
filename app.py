from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import traceback
from src.analyzer import ProjectAnalyzer
from src.llm_client import OllamaClient
from src.generator import ReadmeGenerator
from src.github_fetcher import GitHubFetcher

app = Flask(__name__)
CORS(app)

with open('config.json') as f:
    CONFIG = json.load(f)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "version": "1.0.0"})

@app.route('/api/models', methods=['GET'])
def list_models():
    try:
        llm = OllamaClient(config=CONFIG)
        models = llm.list_models()
        return jsonify({"success": True, "models": models})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/test-ollama', methods=['GET'])
def test_ollama():
    try:
        llm = OllamaClient(config=CONFIG)
        llm.test_connection()
        return jsonify({"success": True, "message": "Ollama is running"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        project_path = data.get('path')
        analyzer = ProjectAnalyzer(config=CONFIG)
        project_info = analyzer.analyze(project_path)
        return jsonify({"success": True, "data": project_info})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/github/fetch', methods=['POST'])
def fetch_github():
    try:
        data = request.json
        github_url = data.get('url')
        fetcher = GitHubFetcher()
        repo_data = fetcher.fetch_and_analyze(github_url)
        analyzer = ProjectAnalyzer(config=CONFIG)
        project_info = analyzer.analyze(repo_data['local_path'])
        return jsonify({"success": True, "data": project_info})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        project_info = data.get('project_info')
        template = data.get('template', 'default')
        model = data.get('model', CONFIG.get('model'))
        config = CONFIG.copy()
        config['model'] = model
        llm = OllamaClient(config=config)
        generator = ReadmeGenerator(llm_client=llm, config=config)
        readme_content = generator.generate(project_info, template)
        return jsonify({"success": True, "readme": readme_content})
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
