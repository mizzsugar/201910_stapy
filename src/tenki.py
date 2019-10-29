import http

import requests


def picnic(postal_code: str) -> str:
    request_url = f'https://tenki.example.com/today/{postal_code}'
    response = requests.get(request_url)
    if response.status_code == http.HTTPStatus.NOT_FOUND:
        raise ValueError
    if response.json().get('天気') == '晴れ':
        return 'ピクニックは決行'
    return 'ピクニックは延期'
