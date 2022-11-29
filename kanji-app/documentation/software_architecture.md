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

### Create Set - Creating a set of cards with a word list

Coming up


### Learn View - Browsing through a set of cards

### Review View - Writing meaning to each card on a set

### Learning Status View - How many cards completed, how many on circle