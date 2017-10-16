import newton

def test_give_it_a_better_name_pls_and_write_a_docstring_pls():
    """Test."""
    assert newton.square_root_with_newton_method(4, 1) == 2


def test_newton_form_zero():
    """newton zero."""
    assert newton.square_root_with_newton_method(0, 1) == None


def test_newton_iterations_zero():
    """iterations zero."""
    assert newton.square_root_with_newton_method(4, -1) == None


def test_newton_rounding_2():
    """rounding."""
    assert newton.square_root_with_newton_method(4.45, 2) == 2.11


def test_newton_rounding_1():
    """Rounding."""
    assert newton.square_root_with_newton_method(6.5, 2) == 2.551