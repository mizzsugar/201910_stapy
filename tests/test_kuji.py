import unittest
import unittest.mock

import src.kuji


class TestKuji(unittest.TestCase):
    @unittest.mock.patch('random.randrange')
    def test_win_if_multiple_of_2(self, mock_random_number):
        mock_random_number.return_value = 2
        actual = src.kuji.kuji()
        expected = 'あたり'
        self.assertEqual(expected, actual)

    @unittest.mock.patch('random.randrange')
    def test_lose(self, mock_random_number):
        mock_random_number.return_value = 1
        actual = src.kuji.kuji()
        expected = 'はずれ'
        self.assertEqual(expected, actual)
