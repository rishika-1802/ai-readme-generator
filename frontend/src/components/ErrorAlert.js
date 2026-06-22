import React from 'react';
import { FiX } from 'react-icons/fi';
import './ErrorAlert.css';

const ErrorAlert = ({ message, onClose }) => {
  return (
    <div className="error-alert">
      <div className="error-content">
        <span className="error-icon">⚠️</span>
        <span className="error-message">{message}</span>
      </div>
      <button onClick={onClose} className="error-close"><FiX /></button>
    </div>
  );
};

export default ErrorAlert;
