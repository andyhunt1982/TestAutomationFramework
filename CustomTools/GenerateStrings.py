import random
import string
import datetime


def upper_and_lower(length: int) -> str:
    letters = string.ascii_letters
    return ''.join(random.choice(letters).upper() for _ in range(length))


def lowercase(length: int) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def uppercase(length: int) -> str:
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for _ in range(length))


def numbers(length: int) -> str:
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(length))


def special_characters(length: int) -> str:
    punctuation = string.punctuation
    return ''.join(random.choice(punctuation) for _ in range(length))


def last_business_date_as_string() -> str:
    today = datetime.date.today()

    previous_business_day = today - datetime.timedelta(days=3 if today.weekday() == 0 else 1)
    previous_business_day = previous_business_day.strftime("%Y-%m-%d")
    return previous_business_day


def next_business_date_as_date() -> str:
    today = datetime.date.today()

    next_business_day = today + datetime.timedelta(days=3 if today.weekday() == 4 else 1)
    next_business_day = next_business_day.strftime("%Y-%m-%d")
    return next_business_day
