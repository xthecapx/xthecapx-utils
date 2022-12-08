
from xthecapx_utils.utils import find_pair_of_numbers
from deepdiff import DeepDiff 

def test_example():
    integers = [1, 9, 5, 0, 20, -4, 12, 16, 7]
    sum = 12
    expected = [(12, 0), (16, -4), (7, 5)]
    result = find_pair_of_numbers(integers, sum)

    assert DeepDiff(expected, result) == {}

def test_case_1():
    integers = [12, 16, 7, 1, 9, 5, 0, 20, -4]
    sum = 12
    expected = [(5, 7), (0, 12), (-4, 16)]
    result = find_pair_of_numbers(integers, sum)

    assert DeepDiff(expected, result) == {}

def test_case_2():
    integers = [1, 2, 3, 4, 5, 6, 7, 8]
    sum = 12
    expected = [(7, 5), (8, 4)]
    result = find_pair_of_numbers(integers, sum)

    assert DeepDiff(expected, result) == {}

def test_case_3():
    """ list is empty """
    integers = []
    sum = 12
    expected = []
    result = find_pair_of_numbers(integers, sum)

    assert DeepDiff(expected, result) == {}

def test_case_4():
    """ list is nully """
    integers = None
    sum = 12
    expected = []
    result = find_pair_of_numbers(integers, sum)

    assert DeepDiff(expected, result) == {}

def test_case_5():
    """ sum is nully """
    integers = [1, 2, 3, 4, 5, 6, 7, 8]
    sum = None
    expected = []
    result = find_pair_of_numbers(integers, sum)

    assert DeepDiff(expected, result) == {}