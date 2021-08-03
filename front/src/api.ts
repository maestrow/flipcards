import { ITerm } from "./models";

export class Api {
  
  private metaNames = ['description', 'keywords']

  private getMetas = () => {
    const metas = this.metaNames.reduce((acc: any, name) => {
      const el = document.querySelector(`meta[name=${name}]`)
      if (el) {
        acc[name] = el.getAttribute('content')
      }
      return acc;
    }, {});
    return metas;
  }

  public endpoint: string = 'http://127.0.0.1:8000/fcards'

  public sync = async (terms: ITerm[]) => {
  
    const data = {
      url: document.location.toString(),
      metas: this.getMetas(),
      terms
    }
  
    return fetch(`${this.endpoint}/sync`, { 
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data),
      // https://stackoverflow.com/questions/63157089/sending-post-request-with-fetch-after-closing-the-browser-with-beforeunload
      keepalive: true // this is important!
    }).then(res => res.json())
  }
  
  public fetch = async () => {
    const data = {
      url: document.location.toString()
    }
    return fetch(`${this.endpoint}/fetch`, { 
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    }).then(res => res.json())
  }
}




