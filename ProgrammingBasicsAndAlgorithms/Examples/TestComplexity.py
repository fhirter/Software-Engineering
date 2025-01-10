import unittest

from ProgrammingBasicsAndAlgorithms.Examples.Complexity import return_first, search, find_doublettes, find_in_tree


class TestComplexity(unittest.TestCase):
    def test_return_first(self):
        values = ['foo', 'bar', 'bazl']

        value = return_first(values)

        self.assertEqual(values[0], value)

    def test_search(self):
        values = ['foo', 'bar', 'bazl'];
        value = search(values, 'foo')
        self.assertTrue(value)

    def test_find_doublettes(self):
        values = ['foo', 'bar', 'bazl', 'foo']
        doublettes = find_doublettes(values)

        self.assertEqual({'foo': 2}, doublettes)

    def test_find_in_tree(self):
        tree = {
            'value': 5,
            'greater': {
                'value': 8,
                'greater': {
                    'value': 9
                },
                'smaller': {
                    'value': 6
                }
            },
            'smaller': {
                'value': 3,
                'greater': {
                    'value': 4,
                },
                'smaller': {
                    'value': 2,
                }
            }
        }
        key = 9
        found = find_in_tree(tree, key)
        self.assertTrue(found)