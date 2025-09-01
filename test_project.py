import pytest
from project import generate_pass, check_strength, check_compromise


def test_generate_pass_default():
    password = generate_pass()
    assert isinstance(password, str)
    assert "Generated password:" in password


def test_generate_pass_custom_length():
    length = 16
    password = generate_pass(str(length))
    assert isinstance(password, str)
    assert "Generated password:" in password
    # Extract the actual password from the return string
    actual_password = password.split(": ")[1].split(" ")[0]
    assert len(actual_password) == length


def test_generate_pass_too_short():
    response = generate_pass("3")
    assert "atleast 4" in response


def test_generate_pass_invalid():
    response = generate_pass("abc")
    assert "valid number" in response


def test_check_strength_levels():
    assert check_strength("") == 0
    assert check_strength("abc") == 1
    assert check_strength("abcABC") == 2
    assert check_strength("abcABC123") == 4
    assert check_strength("abcABC123$") >= 5


def test_check_compromise_empty():
    assert "cannot be empty" in check_compromise("")


def test_check_compromise_known_safe():
    # This is a randomly generated strong password, unlikely to be breached
    result = check_compromise("Th!sIs@Rand0mP@ssw0rd#123")
    assert "Password is not found" in result or "Password was found" in result