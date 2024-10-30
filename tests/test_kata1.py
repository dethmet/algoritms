from examples.kata1 import get_index


def test_linear_search_exists(integer_search_fixture):
    numbers, existing_element, orthodox_index = integer_search_fixture
    assert get_index(numbers, existing_element) == orthodox_index


def test_linear_search_not_exists(integer_search_fixture):
    numbers, _, _ = integer_search_fixture
    not_exists_element = 999
    assert get_index(numbers, not_exists_element) == -1