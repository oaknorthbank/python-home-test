import pytest

from assert_equals import assert_equals


def test_first_scenario():
    with pytest.raises(Exception) as excinfo:
        assert_equals(1, 0)

    assert "Expected 1 but found 0" in str(excinfo.value)
