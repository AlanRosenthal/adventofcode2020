"""
Tests for report_repair.py
"""

from day1.report_repair import get_list_of_permutations
from day1.report_repair import find_tuple_sum
from day1.report_repair import prod
from day1.report_repair import process


def test_get_list_of_permutations_empty_list():
    """
    Test of get_list_of_permutations() with an empty list
    """
    result = get_list_of_permutations([], 2)
    assert not result


def test_get_list_of_permutations_basic_string():
    """
    Test of get_list_of_permutations() with strings
    """
    result = get_list_of_permutations(["a", "b", "c"], 2)
    assert result == [["a", "b"], ["a", "c"], ["b", "c"]]


def test_get_list_of_permutations_basic_numbers_group_2():
    """
    Test of get_list_of_permutations() with numbers, num_groups=2
    """
    result = get_list_of_permutations([1, 2, 3], 2)
    assert result == [[1, 2], [1, 3], [2, 3]]


def test_get_list_of_permutations_one_entry_group_2():
    """
    Test of get_list_of_permutations() with numbers, num_groups=2
    """
    result = get_list_of_permutations([1, 2], 2)
    assert result == [[1, 2]]


def test_get_list_of_permutations_one_entry_group_3():
    """
    Test of get_list_of_permutations() with numbers, num_groups=3
    """
    result = get_list_of_permutations([1, 2, 3], 3)
    assert result == [[1, 2, 3]]


def test_get_list_of_permutations_basic_numbers_group_3():
    """
    Test of get_list_of_permutations() with numbers, num_groups=3
    """
    result = get_list_of_permutations([1, 2, 3, 4], 3)
    assert result == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]


def test_find_tuple_sum_empty_list():
    """
    Test of find_tuple_sum() with an empty list
    """
    result = find_tuple_sum([], 1000)
    assert not result


def test_find_tuple_sum_empty_basic():
    """
    Test of find_tuple_sum() with an basic inputs
    """
    result = find_tuple_sum([[100, 300], [400, 500], [600, 400]], 1000)
    assert result == [600, 400]


def test_find_tuple_sum_empty_basic_triples():
    """
    Test of find_tuple_sum() with an basic inputs, with size of three
    """
    result = find_tuple_sum([[100, 300, 1], [400, 500, 1], [600, 400, 1]], 1001)
    assert result == [600, 400, 1]


def test_find_tuple_sum_empty_no_match():
    """
    Test of find_tuple_sum() with no match
    """
    result = find_tuple_sum([[100, 300], [400, 500], [600, 401]], 1000)
    assert result is None


def test_prod_empty_list():
    """
    Test of prod() with an empty list
    """
    result = prod(())
    assert not result


def test_prod_basic():
    """
    Test of prod() with an basic inputs, part 1
    """
    result = prod([1, 3])
    assert result == 3


def test_prod_basic2():
    """
    Test of prod() with an basic inputs, part 2
    """
    result = prod([2, 3])
    assert result == 6


def test_prod_basic_with_0():
    """
    Test of prod() with an basic inputs, that includes a 0
    """
    result = prod([1, 0])
    assert result == 0


def test_prod_triple():
    """
    Test of prod() with an basic inputs, part 1
    """
    result = prod([1, 2, 3])
    assert result == 6


def test_end_to_end_groups_2():
    """
    Test of process() with test input file, num_groups=2
    """
    result = process("test/test_input.txt", 2)
    assert result == 514579


def test_end_to_end_groups_3():
    """
    Test of process() with test input file, num_groups=3
    """
    result = process("test/test_input.txt", 3)
    assert result == 241861950
