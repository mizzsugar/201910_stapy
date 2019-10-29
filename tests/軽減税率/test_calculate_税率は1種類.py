import unittest

import src.軽減税率.calculate_税率は1種類


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.item_1 = src.軽減税率.calculate_税率は1種類.Item(
            name='sample_1',
            price=500
        )
        self.item_2 = src.軽減税率.calculate_税率は1種類.Item(
            name='sample_2',
            price=1000
        )

    def test_calculate_sum(self):
        items = [self.item_1, self.item_2]
        actual = src.軽減税率.calculate_税率は1種類.price(items)
        expected = 1620
        self.assertEqual(expected, actual)
