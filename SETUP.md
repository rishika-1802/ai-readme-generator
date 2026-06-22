# Setup Guide for AI README Generator

## Prerequisites

- Python 3.8+
- Node.js 14+
- [Ollama](https://ollama.ai)
- Git

## Installation Steps

### 1. Clone Repository
```bash
git clone https://github.com/rishika-1802/ai-readme-generator.git
cd ai-readme-generator
```

### 2. Backend Setup
```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Frontend Setup
```bash
cd frontend
npm install
cd ..
```

### 4. Start Ollama
```bash
# Terminal 1
ollama serve

# Terminal 2 - Pull a model
ollama pull mistral
```

### 5. Run Application

**Terminal 3 - Backend:**
```bash
python app.py
# Backend runs on http://localhost:5000
```

**Terminal 4 - Frontend:**
```bash
cd frontend
npm start
# Frontend runs on http://localhost:3000
```

Open http://localhost:3000 in your browser!

## Docker Setup

```bash
# Using Docker Compose (easiest)
docker-compose up

# Access at http://localhost:3000
```

## CLI Usage

```bash
# Generate from local path
python main.py --path /path/to/project --output README.md

# Generate from GitHub
python main.py --github https://github.com/owner/repo

# Test Ollama connection
python main.py test
```

## Troubleshooting

**Ollama Connection Error**
- Make sure Ollama is running: `ollama serve`
- Check host in config.json

**Model Not Found**
- Pull model: `ollama pull mistral`
- List models: `ollama list`

**Port Already in Use**
- Change port in app.py or frontend/.env

## API Endpoints

- `GET /api/health` - Health check
- `GET /api/models` - List available models
- `GET /api/test-ollama` - Test Ollama connection
- `POST /api/analyze` - Analyze local project
- `POST /api/github/fetch` - Fetch GitHub repo
- `POST /api/generate` - Generate README
