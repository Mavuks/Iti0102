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


def test_convert_name_two_digits_str_len():
    """Test name with lenght of 2 digits."""
    assert calculator.convert_name('Maailmasoda') == 'MAA-11da'


def test_convert_name_addition_negative_numbers_fail():
    """Test addition negative numbers."""
    assert calculator.addition(-3, -4) == '-3 + -4 = -7'


def test_convert_name_addition_positive_numbers_fail():
    """Test addition poisitive numbers."""
    assert calculator.addition(4, 3) == '4 + 3 = 7'


def test_convert_name_addition_negative_a():
    """Test addition when a is negative."""
    assert calculator.addition(-4, 3) == '-4 + 3 = -1'


def test_convert_name_addition_negative_b():
    """test addition when b is negative."""
    assert calculator.addition(4, -3) == '4 + -3 = 1'


def test_subtraction_positive_numbers_fail():
    """Test subtraction positive numbers."""
    assert calculator.subtraction(4, 3) == '4 - 3 = 1'


def test_subtraction_negative_numbers_fail():
    """Test subtraction negative numbers."""
    assert calculator.subtraction(-3, -7) == '-3 - -7 = 4'


def test_subtraction_negative_a():
    """Test subtraction when a is negative."""
    assert calculator.subtraction(-5, 10) == '-5 - 10 = -15'


def test_subtraction_negative_b():
    """Test subtraction when b is negative."""
    assert calculator.subtraction(5, -10) == '5 - -10 = 15'


def test_repeat_negative():
    """Repeat negative."""
    assert calculator.repeat("s", -1) == ''


def test_repeat_zero():
    """Repeat zero."""
    assert calculator.repeat("s", 0) == ''


def test_repeat_empty_string():
    """Repeat empty string."""
    assert calculator.repeat("", 1) == ''


def test_line_empty_decorated():
    """Line empty"""
    assert calculator.line(1, decorated=False) == ''


def test_line_not_decorated():
    """Test not decorated"""
    assert calculator.line(3, decorated=False) == '---'


def test_line_decorated():
    """Test decorated."""
    assert calculator.line(6, decorated=True) == '>------<'





