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


def test_newton_fails_with_high_iterations():
    """Fails with high iterations"""
    assert newton.square_root_with_newton_method(3, 123456) == 1.732


def test_newton_fail_with_low_iterations():
    """Fails with low iterations"""
    assert newton.square_root_with_newton_method(3, 0.0000009) == 1.5


def test_newton_iterations_related_2():
    """Iterations related 2."""
    assert newton.square_root_with_newton_method(3, 0) == 1.5


def  test_newton_fails_with_high_numbers():
    """Test fails with high numbers."""
    assert newton.square_root_with_newton_method(123456, 4) == 3868.619


def test_newton_with_small_numbers():
    """With small numbers."""
    assert newton.square_root_with_newton_method(0.0005, 2) == 0.5


def test_newton_number_and_iterations_related_1():
    """Number and iterations related 1."""
    assert newton.square_root_with_newton_method(1.00, 1.9) == 1.25


def test_newton_number_related_2():
    """Number related 2."""
    assert newton.square_root_with_newton_method(2.1, 2.4) == 1.451


def test_newton_number_related_1():
    """Nr1."""
    assert newton.square_root_with_newton_method(-1, 0.1) == None


def test_newton_limit_iterations():
    """Limit Iterations."""
    assert newton.square_root_with_newton_method(15, 900000) == 3.873



