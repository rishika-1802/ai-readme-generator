import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import InputForm from './components/InputForm';
import Preview from './components/Preview';
import LoadingSpinner from './components/LoadingSpinner';
import ErrorAlert from './components/ErrorAlert';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

function App() {
  const [projectInfo, setProjectInfo] = useState(null);
  const [readme, setReadme] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [models, setModels] = useState(['mistral', 'neural-chat', 'llama2']);
  const [selectedModel, setSelectedModel] = useState('mistral');
  const [selectedTemplate, setSelectedTemplate] = useState('default');

  useEffect(() => {
    checkOllamaConnection();
    fetchModels();
  }, []);

  const checkOllamaConnection = async () => {
    try {
      await axios.get(`${API_URL}/api/test-ollama`);
    } catch (err) {
      setError('⚠️ Ollama is not running. Start Ollama first!');
    }
  };

  const fetchModels = async () => {
    try {
      const response = await axios.get(`${API_URL}/api/models`);
      if (response.data.success) {
        setModels(response.data.models);
      }
    } catch (err) {
      console.error('Error fetching models:', err);
    }
  };

  const handleAnalyze = async (input, type) => {
    setLoading(true);
    setError(null);
    setReadme('');

    try {
      let response;
      if (type === 'local') {
        response = await axios.post(`${API_URL}/api/analyze`, { path: input });
      } else {
        response = await axios.post(`${API_URL}/api/github/fetch`, { url: input });
      }

      if (response.data.success) {
        setProjectInfo(response.data.data);
        await generateReadme(response.data.data);
      } else {
        setError(response.data.error || 'Failed');
      }
    } catch (err) {
      setError(err.response?.data?.error || err.message);
    } finally {
      setLoading(false);
    }
  };

  const generateReadme = async (info) => {
    setLoading(true);
    try {
      const response = await axios.post(`${API_URL}/api/generate`, {
        project_info: info,
        template: selectedTemplate,
        model: selectedModel
      });
      if (response.data.success) {
        setReadme(response.data.readme);
      }
    } catch (err) {
      setError(err.response?.data?.error || err.message);
    } finally {
      setLoading(false);
    }
  };

  const downloadReadme = () => {
    const element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(readme));
    element.setAttribute('download', 'README.md');
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  };

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <h1>🤖 AI README Generator</h1>
          <p>Generate comprehensive READMEs with AI</p>
        </header>

        {error && <ErrorAlert message={error} onClose={() => setError(null)} />}

        <div className="main-content">
          <div className="left-panel">
            <InputForm
              onAnalyze={handleAnalyze}
              loading={loading}
              models={models}
              selectedModel={selectedModel}
              onModelChange={setSelectedModel}
              selectedTemplate={selectedTemplate}
              onTemplateChange={setSelectedTemplate}
            />
          </div>
          <div className="right-panel">
            {loading ? (
              <LoadingSpinner />
            ) : readme ? (
              <Preview readme={readme} onDownload={downloadReadme} />
            ) : (
              <div className="empty-state">
                <p>👈 Start by analyzing a project</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
