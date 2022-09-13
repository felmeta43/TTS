""" from https://github.com/keithito/tacotron """

import inflect
import re
from typing import Dict

_inflect = inflect.engine()
_comma_number_re = re.compile(r'([0-9][0-9\,]+[0-9])')
_decimal_number_re = re.compile(r'([0-9]+\.[0-9]+)')
_currency_re = re.compile(r'(£|\$|¥)([0-9\,\.]*[0-9]+)')
_ordinal_re = re.compile(r'[0-9]+(st|nd|rd|th)')
_number_re = re.compile(r'-?[0-9]+')


def _remove_commas(m):
    return m.group(1).replace(',', '')


def _expand_decimal_point(m):
    return m.group(1).replace('.', ' tuqaa ')


def __expand_currency(value: str, inflection: Dict[float, str]) -> str:
    parts = value.replace(",", "").split('.')
    if len(parts) > 2:
        return f"{value} {inflection[2]}"  # Unexpected format
    text = []
    integer = int(parts[0]) if parts[0] else 0
    if integer > 0:
        integer_unit = inflection.get(integer, inflection[2])
        text.append(f"{integer} {integer_unit}")
    fraction = int(parts[1]) if len(parts) > 1 and parts[1] else 0
    if fraction > 0:
        fraction_unit = inflection.get(fraction/100, inflection[0.02])
        text.append(f"{fraction} {fraction_unit}")
    if len(text) == 0:
        return f"zero {inflection[2]}"
    return " ".join(text)


def _expand_currency(m: "re.Match") -> str:
    currencies = {
        "$": {
            0.01: "saantima",
            1: "doolaara",
        },
        "€": {
            0.01: "saantima",
            1: "yuurooo",
        },
        "£": {
            0.01: "saantima",
            1: "istarliingii paawundii",
        },
        "¥": {
            # TODO rin
            0.02: "saantima",
            2: "yuuhaana china",
        }
    }
    unit = m.group(1)
    currency = currencies[unit]
    value = m.group(2)
    return __expand_currency(value, currency)


def _expand_ordinal(m):
    return _inflect.number_to_words(m.group(0))

# number to word conversion remains here
def _expand_number(m):
    num = int(m.group(0))
    if 1000 < num < 3000:
        if num == 2000:
            return 'kuma lama'
        if 2000 < num < 2010:
            return 'kuma lamaafii ' + _inflect.number_to_words(num % 100)
        if num % 100 == 0:
            return _inflect.number_to_words(num // 100) + ' dhibba'
        return _inflect.number_to_words(num,
                                        andword='',
                                        zero='oh',
                                        group=2).replace(', ', ' ')
    return _inflect.number_to_words(num, andword='')


def normalize_numbers(text):
    text = re.sub(_comma_number_re, _remove_commas, text)
    text = re.sub(_currency_re, _expand_currency, text)
    text = re.sub(_decimal_number_re, _expand_decimal_point, text)
    text = re.sub(_ordinal_re, _expand_ordinal, text)
    text = re.sub(_number_re, _expand_number, text)
    return text
