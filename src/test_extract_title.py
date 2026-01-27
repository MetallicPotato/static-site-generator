import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_hello(self):
        text = "# Hello"
        extracted = extract_title(text)
        self.assertEqual(extracted, "Hello")