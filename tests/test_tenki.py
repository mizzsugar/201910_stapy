import dataclasses
import unittest
import unittest.mock
from typing import (
    Any,
    Dict,
)

import src.tenki


class TestTenki(unittest.TestCase):
    @unittest.mock.patch('requests.get')
    def test_go_on_a_picnic_if_sunny(self, mock_request):
        mock_request.return_value = unittest.mock.Mock(
            status_code=200
        )
        mock_request.return_value.json.return_value = {
            '郵便番号': '1050004',
            '都道府県': '東京都',
            '市区町村': '港区新橋',
            '天気': '晴れ'
        }
        actual = src.tenki.picnic(1050004)
        expected = 'ピクニックは決行'
        self.assertEqual(expected, actual)

    @unittest.mock.patch('requests.get')
    def test_put_off_picnic_if_not_sunny(self, mock_request):
        mock_request.return_value = unittest.mock.Mock(
            status_code=200
        )
        mock_request.return_value.json.return_value = {
            '郵便番号': '1050004',
            '都道府県': '東京都',
            '市区町村': '港区新橋',
            '天気': 'くもり'
        }
        actual = src.tenki.picnic(1050004)
        expected = 'ピクニックは延期'
        self.assertEqual(expected, actual)

    @unittest.mock.patch('requests.get')
    def test_invalid_postal_code(self, mock_request):
        mock_request.return_value = unittest.mock.Mock(
            status_code=404
        )
        with self.assertRaises(ValueError):
            src.tenki.picnic(0000000)


"""
テスト用に作成したMockResponseクラスのインスタンスを外部APIを利用したテストに使う方法も教えてもらったので
書いてみました。
"""
@dataclasses.dataclass(frozen=True)
class MockResponse:
    response: Dict[str, Any]
    status_code: int

    def json(self):
        return self.response


class TestTenkiUsingMockResponse(unittest.TestCase):
    @unittest.mock.patch('requests.get')
    def test_go_on_a_picnic_if_sunny(self, mock_request):
        mock_request.return_value = MockResponse(
            response={
                '郵便番号': '1050004',
                '都道府県': '東京都',
                '市区町村': '港区新橋',
                '天気': '晴れ'
            },
            status_code=200
        )

        actual = src.tenki.picnic(1050004)
        expected = 'ピクニックは決行'
        self.assertEqual(expected, actual)

    @unittest.mock.patch('requests.get')
    def test_put_off_picnic_if_not_sunny(self, mock_request):
        mock_request.return_value = MockResponse(
            response={
                '郵便番号': '1050004',
                '都道府県': '東京都',
                '市区町村': '港区新橋',
                '天気': '曇り'
            },
            status_code=200
        )
        actual = src.tenki.picnic(1050004)
        expected = 'ピクニックは延期'
        self.assertEqual(expected, actual)

    @unittest.mock.patch('requests.get')
    def test_invalid_postal_code(self, mock_request):
        mock_request.return_value = MockResponse(
            response={},
            status_code=404
        )
        with self.assertRaises(ValueError):
            src.tenki.picnic(0000000)
