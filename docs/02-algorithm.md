# Алгоритмы интервальных повторений

- Система Лейтнера (источник: https://ncase.me/remember/ru.html#2)
- SuperMemo (разные версии, https://en.wikipedia.org/wiki/SuperMemo#Description_of_SM-2_algorithm)

## SuperMemo 2 (SM2)

В Anki используется SuperMemo 2 (источник: https://ru.wikipedia.org/wiki/Anki). Описание SuperMemo 2: https://en.wikipedia.org/wiki/SuperMemo#Description_of_SM-2_algorithm. 

The first computer-based SuperMemo algorithm (SM-2)[9] tracks three properties for each card being studied:

- The repetition number n, which is the number of times the card has been successfully recalled (meaning it was given a grade ≥ 3) in a row since the last time it was not.
- The easiness factor EF, which loosely indicates how "easy" the card is (more precisely, it determines how quickly the inter-repetition interval grows). The initial value of EF is 2.5.
- The inter-repetition interval I, which is the length of time (in days) SuperMemo will wait after the previous review before asking the user to review the card again.

Every time the user starts a review session, SuperMemo provides the user with the cards whose last review occurred at least I days ago. For each review, the user tries to recall the information and (after being shown the correct answer) specifies a grade q (from 0 to 5) indicating a self-evaluation the quality of their response, with each grade having the following meaning:

```
algorithm SM-2 is
    input:  user grade q
            repetition number n
            easiness factor EF
            interval I
    output: updated values of n, EF, and I

    if q > 0 (correct response) then
        if n = 0 then
            I ← 1
        else if n = 1 then
            I ← 6
        else
            I ← ⌈I × EF⌉
        end if
        EF ← EF + (0.1 − (5 − q) × (0.08 + (5 − q) × 0.02))
        if EF < 1.3 then
            EF ← 1.3
        end if
        increment n
    else (incorrect response)
        n ← 0
        I ← 1
    end if

    return (n, EF, I)
```

## Выбранный алгоритм

Буду использовать алгоритм SM2 с небольшим изменением: уменьшу количество вариантов grade (градация ответа) с 5 до 3:
- 0 - Incorrect response, 
- 1 - Correct response, after some hesitation.
- 2 - Correct response, with perfect recall.
