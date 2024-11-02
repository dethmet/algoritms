import pytest


@pytest.fixture
def integer_search_fixture():
    numbers = [-3, 1, 3, 5, 10, 11, 15, 17, 21, 23]
    orthodox_index = 4
    existing_element = numbers[orthodox_index]
    return numbers, existing_element, orthodox_index

@pytest.fixture
def value_search_fixture():
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    orthodox_index = 4
    existing_element = words[orthodox_index]
    return words, existing_element, orthodox_index
