import pytest

from data import heap as mod

CASES = [
    ('sift_up', [[3, 1, 2], 1], [1, 3, 2], False),
    ('sift_up', [[1, 2, 3], 2], [1, 2, 3], False),
    ('sift_down', [[3, 1, 2], 0], [1, 3, 2], False),
    ('push', [[1, 3], 2], [1, 3, 2], False),
    ('pop', [[1, 2, 3]], [1, [2, 3]], False),
    ('pop', [[]], [None, []], False),
    ('heapify', [[3, 1, 2]], [1, 3, 2], False),
    ('heapify', [[]], [], False),
    ('sift_up', [[1], 0], [1], False),
    ('sift_down', [[1], 0], [1], False),
    ('push', [[], 1], [1], False),
    ('pop', [[5]], [5, []], False),
    ('heapify', [[1]], [1], False),
    ('sift_down', [[5, 3, 4], 0], [3, 5, 4], False),
    ('push', [[1, 2], 0], [0, 2, 1], False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_heap_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
