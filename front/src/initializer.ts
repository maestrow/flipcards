import { containerId } from './container-id';

let el = document.getElementById(containerId);
if (!el) {
    el = document.createElement('div');
    el.id = containerId;
    el.style.all = 'initial'
    el.attachShadow({ mode: 'open' });
    document.body.appendChild(el);
}