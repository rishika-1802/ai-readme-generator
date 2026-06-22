# AI README Generator

An intelligent tool that automatically generates comprehensive README files for your projects using Ollama and local LLMs with a modern web UI.

## Features

- 🤖 **AI-Powered Generation** - Uses Ollama with local language models (no API keys needed)
- 📁 **Local Repository Analysis** - Scans your project files to understand structure and purpose
- 🌐 **GitHub Integration** - Fetch and analyze repositories directly from GitHub URLs
- 💻 **Web UI** - Beautiful, intuitive interface for easy README generation
- 📝 **Comprehensive Documentation** - Generates all sections
- 🎨 **Customizable Templates** - Adapt generated README to your needs
- ⚙️ **Model Flexibility** - Works with any Ollama-supported model

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/rishika-1802/ai-readme-generator.git
cd ai-readme-generator
```

### 2. Setup Backend
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Setup Frontend
```bash
cd frontend
npm install
```

### 4. Start Ollama
```bash
ollama serve
ollama pull mistral
```

### 5. Run Both Services

**Terminal 1:**
```bash
python app.py
```

**Terminal 2:**
```bash
cd frontend
npm start
```

Open http://localhost:3000 in your browser!

## Usage

### Web UI
1. Open http://localhost:3000
2. Choose input (Local path or GitHub URL)
3. Select model and template
4. Click "Generate README"
5. Download your README

### CLI
```bash
python main.py --path /path/to/project --output README.md
python main.py --github https://github.com/owner/repo
python main.py test  # Test Ollama connection
```

## Documentation

See [SETUP.md](SETUP.md) for detailed setup instructions.

## License

MIT License
