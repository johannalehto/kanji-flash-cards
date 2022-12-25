import unittest
from entities.card import Card
from entities.card import Kanji
from services.kanji_service import KanjiService




class TestCard(unittest.TestCase):
    def setUp(self):
        #self.kanji = Kanji("山", "mountain")
        self.card = Card("山", "mountain")
        #self.service = KanjiService()

    def test_meaning_call(self):
        self.assertEqual(self.card.meaning(), "mountain")
    
