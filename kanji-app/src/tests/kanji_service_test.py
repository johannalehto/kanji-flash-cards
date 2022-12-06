import unittest
from services.kanji_service import KanjiService
from entities.card import Card
from entities.kanji import Kanji

class CardStub:
    def __init__(self):
        self.kanji = Kanji("山", "mountain")

    def meaning(self):
        return self.kanji.english
    


class TestKanjiService(unittest.TestCase):
    def setUp(self):
        self.service = KanjiService()

    def test_check_meaning_returns_true_when_answer_correct(self):
        card = CardStub()
        self.assertTrue(self.service.check_meaning("mountain", card))

    def test_check_meaning_returns_false_when_answer_incorrect(self):
        card = CardStub()
        self.assertFalse(self.service.check_meaning("yama", card))


    