import pytest

from assert_equals import assert_equals


def test_first_scenario():
    with pytest.raises(Exception, match="Expected 1 but found 0"):
        assert_equals(1, 0)
