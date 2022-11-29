from ui import UI


def main(kanjiset):
    kanjiapp = UI(kanjiset)
    kanjiapp.start()


if __name__ == "__main__":
    test_set = [
        {
            "kanji": "山",
            "english": "mountain"
        },
        {
            "kanji": "木",
            "english": "tree"
        },
        {
            "kanji": "火",
            "english": "fire"
        },
        {
            "kanji": "女",
            "english": "woman"
        },
        {
            "kanji": "心",
            "english": "heart"
        }
    ]
    main(test_set)
