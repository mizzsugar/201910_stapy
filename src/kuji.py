import random


def kuji() -> str:
    fortune_number = random.randrange(10)
    if fortune_number % 2 == 0:
        return 'あたり'
    return 'はずれ'
