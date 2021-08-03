export interface ISimpleTranslation {
  orig: string,   // original
  trans: string,  // translation
  dict?: Array<{
    pos: string,     // part of speech
    terms: string[]
  }>
}

export const simplify = (json: any): ISimpleTranslation | undefined => {
  try {
    return {
      orig: json.sentences[0].orig,
      trans: json.sentences[0].trans,
      dict: json.dict?.map((d: any) => ({
        pos: d.pos,
        terms: d.terms
      }))
    }
  } catch (error) {
    return undefined
  }
}

export interface ITerm {
  foreign: string
  meaning: string
  context: string
  // data?: {
  //   simplified?: ISimpleTranslation,
  //   all: any
  // }
}
