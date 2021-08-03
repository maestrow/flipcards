// https://stackoverflow.com/questions/26714426/what-is-the-meaning-of-google-translate-query-params
import { makeCancelable } from "./cancelable-promise";

const urlTpl = "https://translate.googleapis.com/translate_a/single?dt=t&dt=bd&dt=qc&dt=rm&dt=ex&client=gtx&hl=ru&sl=auto&tl=ru&q=handbook&dj=1"

var getBaseParams = () => [
  ['dt', 't'],
  ['dt', 'bd'],
  ['dt', 'qc'],
  ['dt', 'rm'],
  ['dt', 'ex'],
  ['client', 'gtx'],
  ['hl', 'ru'],
  ['sl', 'auto'],
  ['tl', 'ru'],
  ['dj', '1']
]

export const mockTranslate = (text: string) => {
  return makeCancelable<string>(new Promise((res, rej) => {
    setTimeout(() => {
      res(text.toUpperCase());
    }, 2000);
  }));
}

export const translate = (text: string) => {
  const params = getBaseParams()
  params.push(['q', text])
  const url = new URL('https://translate.googleapis.com/translate_a/single')
  url.search = new URLSearchParams(params).toString();
  return fetch(url as any, { method: 'GET' }).then(res => res.json())
}

