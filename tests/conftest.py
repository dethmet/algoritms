import random
from string import ascii_lowercase, digits

import pytest


@pytest.fixture
def integer_search_fixture():
    numbers = sorted([random.randint(-100000,100000) for i in range(100000)])
    orthodox_index = random.randint(0, len(numbers))
    existing_element = numbers[orthodox_index]
    return numbers, existing_element, numbers.index(existing_element)

@pytest.fixture
def value_search_fixture():
    words = sorted([''.join(random.choices(ascii_lowercase + digits, k=6)) for i in range(100000)])
    orthodox_index = random.randint(0, len(words))
    existing_element = words[orthodox_index]
    return words, existing_element, words.index(existing_element)
