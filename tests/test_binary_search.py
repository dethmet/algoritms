from examples.binary_search import binary_search_recursive, binary_search_iterative
# from ..binary_search

# @pytest.fixture
# from examples.binary_search import binary_search_recursive



def test_binary_search_recursive_exists(integer_search_fixture):
    numbers, existing_element, arr_search_numbers = integer_search_fixture
    assert binary_search_recursive(numbers, existing_element) in arr_search_numbers


def test_binary_search_recursive_not_exists(integer_search_fixture):
    numbers, _, _ = integer_search_fixture
    not_exists_element = 999999
    assert binary_search_recursive(numbers, not_exists_element) == -1


def test_binary_search_iterative_exists(integer_search_fixture):
    numbers, existing_element, arr_search_numbers = integer_search_fixture
    assert binary_search_iterative(numbers, existing_element) in arr_search_numbers


def test_binary_search_iterative_not_exists(integer_search_fixture):
    numbers, _, _ = integer_search_fixture
    not_exists_element = 999999
    assert binary_search_iterative(numbers, not_exists_element) == -1


def test_binary_search_recursive_exists_by_string(value_search_fixture):
    words, existing_element, orthodox_index = value_search_fixture
    assert binary_search_recursive(words, existing_element) == orthodox_index


def test_binary_search_recursive_not_exists_by_string(value_search_fixture):
    words, _, _ = value_search_fixture
    not_exists_element = '999999'
    assert binary_search_recursive(words, not_exists_element) == -1


def test_binary_search_iterative_exists_by_string(value_search_fixture):
    words, existing_element, orthodox_index = value_search_fixture
    assert binary_search_iterative(words, existing_element) == orthodox_index


def test_binary_search_iterative_not_exists_by_string(value_search_fixture):
    words, _, _ = value_search_fixture
    not_exists_element = '999999'
    assert binary_search_iterative(words, not_exists_element) == -1