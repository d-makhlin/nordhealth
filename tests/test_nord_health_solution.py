from nord_health_solution import NordHealthSolution


def test_empty_list():
    # Check empty list
    assert NordHealthSolution.get_pairs_with_equal_sum_dict([]) == {}


def test_success():
    # Check that all existing pairs return in relation to a sum
    res_dict = NordHealthSolution.get_pairs_with_equal_sum_dict([1, 1, 2, 4, 3, 6, 1, 5])
    assert res_dict == {
        5: {(1, 4), (2, 3)},
        6: {(1, 5), (2, 4)},
        7: {(1, 6), (2, 5), (3, 4)},
        8: {(2, 6), (3, 5)},
        9: {(3, 6), (4, 5)}}


def test_equal_numbers():
    # Check no pairs for equal numbers
    assert NordHealthSolution.get_pairs_with_equal_sum_dict([2, 2, 2, 2, 2]) == {}


def test_equal_pairs():
    # Check equal pairs are filtered
    assert NordHealthSolution.get_pairs_with_equal_sum_dict([2, 3, 2, 3]) == {}


def test_one_element():
    # Check no pairs for one element
    assert NordHealthSolution.get_pairs_with_equal_sum_dict([2]) == {}
