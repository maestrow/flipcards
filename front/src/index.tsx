import React, { useCallback, useState } from 'react';
import ReactDOM from "react-dom";
import { App } from './components/app';

function htmlToElement(html: string): HTMLElement {
  var template = document.createElement('template');
  html = html.trim(); // Never return a text node of whitespace as the result
  template.innerHTML = html;
  return template.content.firstChild as HTMLElement;
}

const id = 'vocab-k09asnd';

document.body.appendChild(htmlToElement(`<div id='${id}'></div>`));

ReactDOM.render(<App />, document.getElementById(id));