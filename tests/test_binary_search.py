from examples.binary_search import binary_search_recursive, binary_search_iterative
# from ..binary_search

# @pytest.fixture
# from examples.binary_search import binary_search_recursive



def test_binary_search_recursive_exists(integer_search_fixture):
    numbers, existing_element, orthodox_index = integer_search_fixture
    assert binary_search_recursive(numbers, existing_element) == orthodox_index
    not_exists_element = 999
    assert binary_search_recursive(numbers, not_exists_element) == -1


def test_binary_search_recursive_not_exists(integer_search_fixture):
    numbers, _, _ = integer_search_fixture
    not_exists_element = 999
    assert binary_search_recursive(numbers, not_exists_element) == -1


def test_binary_search_iterative_exists(integer_search_fixture):
    numbers, existing_element, orthodox_index = integer_search_fixture
    assert binary_search_iterative(numbers, existing_element) == orthodox_index


def test_binary_search_iterative_not_exists(integer_search_fixture):
    numbers, _, _ = integer_search_fixture
    not_exists_element = 999
    assert binary_search_iterative(numbers, not_exists_element) == -1