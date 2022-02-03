import random
import string

from app.main import check_password

import pytest


def password_generator():
    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    numbers = string.digits
    special_symbols = "$@#&!-_"
    length = random.randint(8, 16)

    all_symbols = [letters_upper, letters_lower, numbers, special_symbols]
    random_password = ''

    random_password += random.choice(letters_upper)
    random_password += random.choice(letters_lower)
    random_password += random.choice(numbers)
    random_password += random.choice(special_symbols)

    while len(random_password) < length:
        random_password += random.choice(all_symbols[random.randint(0, 3)])

    return random_password


@pytest.mark.parametrize(
    "password, expected",
    [
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
        (password_generator(), True),
    ],
)
def test_random_password_generator(password, expected):
    assert check_password(password) is expected
