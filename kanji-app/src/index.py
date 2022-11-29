from ui.ui import UI


def main(kanjiset):
    kanjiapp = UI(kanjiset)
    kanjiapp.run()


if __name__ == "__main__":
    test_set = "src/data/kanji-list.json"
    main(test_set)
