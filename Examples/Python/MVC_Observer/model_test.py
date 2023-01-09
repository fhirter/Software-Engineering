import unittest

from model import Model


class UiTest(unittest.TestCase):
    def test_get_random_word(self):
        words = ["foo", "bar", "fubar", "bazl"]
        model = Model(words)

        word = model.get_random_word()

        assert word in words
