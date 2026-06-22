import React from 'react';
import ReactMarkdown from 'react-markdown';
import { FiDownload, FiCopy } from 'react-icons/fi';
import './Preview.css';

const Preview = ({ readme, onDownload }) => {
  const handleCopy = () => {
    navigator.clipboard.writeText(readme);
    alert('Copied to clipboard!');
  };

  return (
    <div className="preview">
      <div className="preview-header">
        <h2>📄 Preview</h2>
        <div className="preview-actions">
          <button onClick={handleCopy} className="action-btn" title="Copy">
            <FiCopy /> Copy
          </button>
          <button onClick={onDownload} className="action-btn primary" title="Download">
            <FiDownload /> Download
          </button>
        </div>
      </div>
      <div className="preview-content">
        <ReactMarkdown>{readme}</ReactMarkdown>
      </div>
    </div>
  );
};

export default Preview;
