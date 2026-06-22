import React from 'react';
import './LoadingSpinner.css';

const LoadingSpinner = () => {
  return (
    <div className="loading-container">
      <div className="spinner"></div>
      <p>Generating your README...</p>
      <p className="loading-tips"><small>💡 May take a minute</small></p>
    </div>
  );
};

export default LoadingSpinner;
