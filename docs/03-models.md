# Модель данных

## Подход в Mnemosyne

Типы карточек:
- Front-to-Back
- Back-to-Front
- Front-to-Back and Back-to-Front
- Vocabulary

### Тип Vocabulary

2 тренировки:
- recognition
- prodiction

Поля:
- foreign word or phrase
- meaning
- prononciatation
- notes

## Выбранная модель данных

cards:
- foreign
- meaning
- pronunciation
- context (фраза на иностранном языке с употреблением слова)
- notes
- last_review 
- n (repetition number)
- i (interval)
- ef (Easiness Factor)

- The repetition number n, which is the number of times the card has been successfully recalled in a row since the last time it was not.
- The easiness factor EF, which loosely indicates how "easy" the card is (more precisely, it determines how quickly the inter-repetition interval grows). The initial value of EF is 2.5.
- The inter-repetition interval I, which is the length of time (in days) SuperMemo will wait after the previous review before asking the user to review the card again.

decks:
- creation_date
- name
- url
- description

tags:
- name
- description

state:
- stage (day)

Spaced repetitions comic: https://ncase.me/remember/

