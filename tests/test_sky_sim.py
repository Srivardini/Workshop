import pytest
from mymodule.sky_sim import get_radec

def test_module_import():
    try:
        import mymodule.sky_sim
    except Exception as e:
        raise AssertionError("Failed to import mymodule")
    return

def test_get_radec_values():
    """
    This  checks that get radec gives back the correct values 
    of Andromeda in decimal degrees
    """
    ra, dec = get_radec()
    assert ra == pytest.approx(14.215420962967535)
    assert dec == pytest.approx(41.269166666666667)
