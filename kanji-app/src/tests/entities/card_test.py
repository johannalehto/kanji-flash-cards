import unittest
from entities.card import Card
from entities.card import Kanji
from services.kanji_service import KanjiService

# class KanjiStub:
#     def __init__(self):
#         self._character = "山"
#         self._english = "mountain"


class TestCard(unittest.TestCase):
    def setUp(self):
        self.received_kanji = ["山", "mountain"]
        self.card = Card(Kanji(self.received_kanji[0], self.received_kanji[1]))
        #self.service = KanjiService()

    def test_meaning_call(self):
        self.assertEqual(self.card.meaning(), "mountain")
    
