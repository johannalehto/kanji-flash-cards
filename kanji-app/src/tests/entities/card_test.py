import unittest
from entities.card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card("山", "mountain")

    def test_meaning_call(self):
        self.assertEqual(self.card.meaning(), "mountain")
    
