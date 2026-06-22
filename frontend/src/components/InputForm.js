import React, { useState } from 'react';
import { FiGithub, FiFolder } from 'react-icons/fi';
import './InputForm.css';

const InputForm = ({
  onAnalyze,
  loading,
  models,
  selectedModel,
  onModelChange,
  selectedTemplate,
  onTemplateChange
}) => {
  const [input, setInput] = useState('');
  const [type, setType] = useState('local');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim()) {
      onAnalyze(input, type);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="input-form">
      <h2>📁 Project Analysis</h2>

      <div className="input-type">
        <label>
          <input type="radio" value="local" checked={type === 'local'} onChange={(e) => setType(e.target.value)} />
          <FiFolder /> Local Path
        </label>
        <label>
          <input type="radio" value="github" checked={type === 'github'} onChange={(e) => setType(e.target.value)} />
          <FiGithub /> GitHub URL
        </label>
      </div>

      <div className="form-group">
        <input
          type="text"
          placeholder={type === 'local' ? 'Enter project path' : 'Enter GitHub URL'}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          disabled={loading}
          className="input-field"
        />
      </div>

      <div className="form-group">
        <label>Model</label>
        <select value={selectedModel} onChange={(e) => onModelChange(e.target.value)} disabled={loading} className="select-field">
          {models.map((model) => (
            <option key={model} value={model}>{model}</option>
          ))}
        </select>
      </div>

      <div className="form-group">
        <label>Template</label>
        <select value={selectedTemplate} onChange={(e) => onTemplateChange(e.target.value)} disabled={loading} className="select-field">
          <option value="default">Default</option>
          <option value="detailed">Detailed</option>
          <option value="brief">Brief</option>
        </select>
      </div>

      <button type="submit" disabled={loading} className="submit-btn">
        {loading ? '⏳ Generating...' : '✨ Generate README'}
      </button>
    </form>
  );
};

export default InputForm;
