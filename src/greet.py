import datetime


def greet_現在時刻を引数に持たせる(now: datetime.datetime) -> str:
    if 5 <= now.hour < 12:
        return 'おはようございます'
    elif 12 <= now.hour < 18:
        return 'こんにちは'
    return 'こんばんは'


def greet() -> str:
    # 説明を簡潔にするためにこの関数ではタイムゾーンは考慮しないとしています。
    now = datetime.datetime.now()
    if 5 <= now.hour < 12:
        return 'おはようございます'
    elif 12 <= now.hour < 18:
        return 'こんにちは'
    return 'こんばんは'
