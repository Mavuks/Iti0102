import calculator

def test_repeat_zero_length():
    # TODO: assert here something
    pass

def test_repeat_negative_length():
    # TODO: assert here something
    pass
def test_convert_name_savisaar():
    """Test converting name Savisaar."""
    assert calculator.convert_name('Savisaar') == 'SAV-8ar'


def test_convert_name_empty():
    """Test empty name."""
    assert calculator.convert_name('') == 'ERROR'


def test_convert_name_no_longer_in_end():
    """Test returned name to have a lower suffix in the end."""
    assert calculator.convert_name('TIIGER') == 'TII-6er'


def test_convert_name_two_digitas_str_len():
    """test a name with longer lenght then one digit."""
    assert calculator.convert_name('PYTHON') == 'PYT-6on'


def test_convert_name_error_with_len3():
    """test name with lenght of 3."""
    assert calculator.convert_name('ASD') == 'ASD-3sd'







