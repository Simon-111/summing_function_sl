# summer() is a function that finds consectutive runs in a list of numbers that total a certain amount
#     eg. summer([1, 2, 3, 4, 5, 6, 7, 8], 12 would return perhaps a tuple (2, 5) which means that the slice
#    [2:5] in that list that totals 12 or returns the slice of the list that totals twelve [3, 4, 5], returns
#    None if no run of 12 is found

import sys
import pytest
#from summer import summer
from ..src.summer import summer

def test_list_type_error():
    with pytest.raises(TypeError):
        summer(['a'], 10)


def test_secound_arg_not_int():
    with pytest.raises(TypeError):
        summer([1, 2, 3], 'this_no_work')


def test_first_arg_not_list():
    with pytest.raises(TypeError):
        summer(20.4, 5)


def test_second_arg_float():
    assert summer([1, 2, 3], 2.0)


def test_12_only():
    assert summer([12], 12) == [(0, 1)]


def test_empty_list():
    assert summer([], 5) == None


def test_list():
    assert summer([1, 2, 3, 4, 5, 6], 12) == [(2, 5)]


def test_4_num_sum():
    assert summer([1, 3, 4, 2, 4, 1], 11) == [(2, 6)]


def test_two_matches():
    assert summer([1, 5, 2, 3, 3], 6) == [(0, 2), (3, 5)]


def test_default_second_input():
    assert summer([5, 4, 10, 2, 2, 2, 2, 2]) == [(2, 3), (3, 8)]


def test_last_items_equals():
    assert summer([1, 3, 11, 3, 20], 20) == [(4, 5)]


def test_long_list_no_sum():
    assert summer([1, 10, 3, 5, 2, 1, 2, 7, 1, 1, 1, 5, 3], 4) == None
