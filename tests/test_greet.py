import datetime
import unittest
import unittest.mock

from freezegun import freeze_time

import src.greet


"""
Cpythonで実行すると失敗します。
失敗する例としてのテストコードなのでコメントアウトしています。
"""
# class TestFail(unittest.TestCase):
#     @unittest.mock.patch('datetime.datetime.now')
#     def test_fail(self, mock_datetime):
#         mock_datetime.return_value = datetime.datetime(
#             2019, 10, 1, 5, 0, 0, 0
#         )
#         expected = 'おはようございます'
#         self.assertEqual(
#             expected,
#             src.greet.greet()
#         )


class TestGreet(unittest.TestCase):
    @freeze_time('2019-10-01 05:00:00')
    def test_morning(self):
        expected = 'おはようございます'
        self.assertEqual(
            expected,
            src.greet.greet()
        )

    @freeze_time('2019-10-01 12:00:00')
    def test_noon(self):
        expected = 'こんにちは'
        self.assertEqual(
            expected,
            src.greet.greet()
        )

    @freeze_time('2019-10-01 18:00:00')
    def test_night(self):
        expected = 'こんばんは'
        self.assertEqual(
            expected,
            src.greet.greet()
        )


class TestGreet引数に渡す(unittest.TestCase):
    def test_morning(self):
        expected = 'おはようございます'
        self.assertEqual(
            expected,
            src.greet.greet_現在時刻を引数に持たせる(
                datetime.datetime(2019, 10, 1, 5, 0, 0, 0)
            )
        )

    def test_noon(self):
        expected = 'こんにちは'
        self.assertEqual(
            expected,
            src.greet.greet_現在時刻を引数に持たせる(
                datetime.datetime(2019, 10, 1, 12, 0, 0, 0)
            )
        )

    def test_night(self):
        expected = 'こんばんは'
        self.assertEqual(
            expected,
            src.greet.greet_現在時刻を引数に持たせる(
                datetime.datetime(2019, 10, 1, 18, 0, 0, 0)
            )
        )
