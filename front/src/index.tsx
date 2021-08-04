import React, { useCallback, useState } from 'react';
import ReactDOM from "react-dom";
import { App } from './components/app';
import { containerId } from './container-id';

const attachToExistedShadow = () => {
  const container = document.getElementById(containerId);
  if (container) {
    const target = document.createElement('div');
    if (container.shadowRoot) {
      container.shadowRoot.appendChild(target)
      ReactDOM.render(<App />, target);
    }
  }
}

attachToExistedShadow();