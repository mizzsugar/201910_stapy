import unittest

import src.軽減税率.calculate_キャッシュレス導入


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.item_1 = src.軽減税率.calculate_キャッシュレス導入.Item(
            name='sample_1',
            price=500
        )
        self.item_2 = src.軽減税率.calculate_キャッシュレス導入.Item(
            name='sample_2',
            price=1000
        )

    def test_calculate_sum_eatin_cache(self):
        items = [self.item_1, self.item_2]
        actual = src.軽減税率.calculate_キャッシュレス導入.price(
            items,
            eat_in=False,
            cache_less=False
        )
        expected = 1620
        self.assertEqual(expected, actual)

    def test_calculate_takeout_cache(self):
        items = [self.item_1, self.item_2]
        actual = src.軽減税率.calculate_キャッシュレス導入.price(
            items,
            eat_in=True,
            cache_less=False
        )
        expected = 1650
        self.assertEqual(expected, actual)

    def test_calculate_sum_eatin_cache_less(self):
        items = [self.item_1, self.item_2]
        actual = src.軽減税率.calculate_キャッシュレス導入.price(
            items,
            eat_in=False,
            cache_less=True
        )
        expected = 1539
        self.assertEqual(expected, actual)

    def test_calculate_takeout_cache_less(self):
        items = [self.item_1, self.item_2]
        actual = src.軽減税率.calculate_キャッシュレス導入.price(
            items,
            eat_in=True,
            cache_less=True
        )
        expected = 1567
        self.assertEqual(expected, actual)
