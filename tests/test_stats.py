import pytest
from stats import mean, median, mode


# ─── mean() ───────────────────────────────────────────

def test_mean_normal():
    assert mean([1, 2, 3, 4, 5]) == 3.0

def test_mean_single_element():
    assert mean([7]) == 7.0

def test_mean_negative_numbers():
    assert mean([-2, -4, -6]) == -4.0

def test_mean_floats():
    assert mean([1.5, 2.5]) == 2.0

def test_mean_empty_list():
    with pytest.raises(ValueError):
        mean([])

def test_mean_non_list():
    with pytest.raises(TypeError):
        mean("hello")

def test_mean_non_numbers():
    with pytest.raises(TypeError):
        mean([1, "a", 3])


# ─── median() ─────────────────────────────────────────

def test_median_odd_length():
    assert median([1, 3, 5]) == 3.0

def test_median_even_length():
    assert median([1, 2, 3, 4]) == 2.5

def test_median_single_element():
    assert median([9]) == 9.0

def test_median_unsorted_input():
    assert median([5, 1, 3]) == 3.0

def test_median_empty_list():
    with pytest.raises(ValueError):
        median([])

def test_median_duplicates():
    assert median([2, 2, 2]) == 2.0


# ─── mode() ───────────────────────────────────────────

def test_mode_normal():
    assert mode([1, 2, 2, 3]) == 2

def test_mode_single_element():
    assert mode([5]) == 5

def test_mode_multiple_duplicates():
    assert mode([1, 1, 2, 2, 2, 3]) == 2

def test_mode_all_same():
    assert mode([4, 4, 4]) == 4

def test_mode_empty_list():
    with pytest.raises(ValueError):
        mode([])

def test_mode_non_list():
    with pytest.raises(TypeError):
        mode(42)