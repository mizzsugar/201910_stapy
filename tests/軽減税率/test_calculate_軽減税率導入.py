import unittest

import src.軽減税率.calculate_軽減税率導入


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.item_1 = src.軽減税率.calculate_軽減税率導入.Item(
            name='sample_1',
            price=500
        )
        self.item_2 = src.軽減税率.calculate_軽減税率導入.Item(
            name='sample_2',
            price=1000
        )

    def test_calculate_sum_takeout(self):
        items = [self.item_1, self.item_2]
        actual = src.軽減税率.calculate_軽減税率導入.price(items, eat_in=False)
        expected = 1620
        self.assertEqual(expected, actual)

    def test_calculate_sum_eatin(self):
        items = [self.item_1, self.item_2]
        actual = src.軽減税率.calculate_軽減税率導入.price(items, eat_in=True)
        expected = 1650
        self.assertEqual(expected, actual)
