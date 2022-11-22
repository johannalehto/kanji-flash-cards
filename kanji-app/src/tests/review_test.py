import unittest
from review import Review

class KanjisetStub:
    def get_kanjilist(self):
        return [
        {
        "kanji": "山",
        "english": "mountain"
        },
        {
        "kanji": "木",
        "english": "tree"
        }
        ]

class TestReview(unittest.TestCase):
    def setUp(self):
        self.kanjiset = Review(KanjisetStub())

    def test_check_cards_check_meaning_correct_answer(self):
        card_answer = "mountain"
        user_answer = "mountain"
        correct_answer = self.kanjiset.check_meaning(user_answer, card_answer)
        self.assertEqual(correct_answer, "Correct!")
