# Software Architecture Description 

## Structure

The package diagram for the current structure of the application 

![Package diagram](./img/kanji-app-package.png)

## User interface

User interface is currently command line -based and it has a menu, offering two options for either displaying the Learn -view or Review -view. Both are separate classes called in UI-class. 

## Application logic

```mermaid
classDiagram
    Card "*" --> "1" Pile
    class Pile{
        id
    }
    class Card{
        id
        kanji
        level1
        level2
        level3
    }
    Kanji "1" --> "1" Card
    class Kanji{
        id
        character
        english
        onyomi
        kunyomi
    }
```

## Repositories

Coming up.

## Files 

Coming up. 

## Main Functionalities

### Creating a set of cards from a .csv-file

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant KanjiService
  participant Pile
  participant Card
  participant Kanji
  User->>UI: Press ENTER to use a default card set
  UI->>KanjiService: create_new_pile()
  KanjiService->>Pile: create_cardset_from_file(word_file)
  Pile->>Card: add_kanji(word)
  Card->>Kanji: Kanji(word[0], word[1])
  Kanji-->>Card: Card(kanji)
  Card-->>Pile: cards.append(Card)
  Pile-->>KanjiService: new_pile
```


### Learn View - Browsing through a set of cards

### Review View - Writing meaning to each card on a set

### Learning Status View - How many cards completed, how many on circle
