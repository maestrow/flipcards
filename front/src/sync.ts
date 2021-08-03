import { ITerm } from "./models";

const metaNames = ['description', 'keywords']

const getMetas = () => {
  const metas = metaNames.reduce((acc: any, name) => {
    const el = document.querySelector(`meta[name=${name}]`)
    if (el) {
      acc[name] = el.getAttribute('content')
    }
    return acc;
  }, {});
  return metas;
}

export const sync = async (terms: ITerm[]) => {
  
  const data = {
    url: document.location.toString(),
    metas: getMetas(),
    terms
  }

  return fetch('http://127.0.0.1:8000/fcards/sync', { 
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  }).then(res => res.json())
}