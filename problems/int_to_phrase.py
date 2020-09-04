import math


def int_to_phrase(num):
    if num == 0:
        return 'zero'

    d = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'fourty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand',
        10000: 'ten-thousand',
        100000: 'hundred-thousand',
    }

    ones = num % 10
    tens = num % 100
    hundreds = num % 1000
    thousands = num % 10000
    ten_thousands = num % 100000
    hundred_thousands = num % 1000000

    ones_str = d.get(ones)
    tens_str = d.get(math.floor(tens/10))
    hundreds_str = d.get(math.floor(hundreds/100))+'hundred'
    thousands_str = d.get(math.floor(thousands/1000))+'-thousand '
    ten_thousands_str = d.get(math.floor(ten_thousands/10000))+' ten-thousand'
    hundred_thousands_str = d.get(math.floor(
        hundred_thousands/100000))+' hundred-thousand'

    if 9 < tens < 20:
        ones_str = None

    print(hundred_thousands_str, ten_thousands_str,
          thousands_str, hundreds_str, tens_str, ones_str)


int_to_phrase(9256)
