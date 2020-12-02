from day1.report_repair import get_list_of_permutations
from day1.report_repair import find_tuple_sum
from day1.report_repair import prod


def test_get_list_of_permutations_empty_list():
    result = get_list_of_permutations([])
    assert not list(result)


def test_get_list_of_permutations_basic_string():
    result = get_list_of_permutations(["a", "b", "c"])
    assert list(result) == [("a", "b"), ("a", "c"), ("b", "c")]


def test_get_list_of_permutations_basic_numbers():
    result = get_list_of_permutations([1, 2, 3])
    assert list(result) == [(1, 2), (1, 3), (2, 3)]


def test_find_tuple_sum_empty_list():
    result = find_tuple_sum([], 1000)
    assert not result


def test_find_tuple_sum_empty_basic():
    result = find_tuple_sum([(100, 300), (400, 500), (600, 400)], 1000)
    assert result == (600, 400)


def test_find_tuple_sum_empty_no_match():
    result = find_tuple_sum([(100, 300), (400, 500), (600, 401)], 1000)
    assert result == None

def test_prod_empty_list():
    result = prod(())
    assert not result

def test_prod_basic():
    result = prod((1, 3))
    assert result == 3

def test_prod_basic2():
    result = prod((2, 3))
    assert result == 6

def test_prod_basic0():
    result = prod((1, 0))
    assert result == 0
