import unittest
from entities.session import Session
from services.kanji_service import KanjiService


class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = Session()
        self.service = KanjiService()
    
    def test_add_point_adds_correctly(self):
        self.session.add_point()
        self.assertEqual(self.session.session_points(), 1)

