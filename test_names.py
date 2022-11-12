from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("John", "Doe") == "Doe; John"
    assert make_full_name("Michael", "Jackson") == "Jackson; Michael"
    assert make_full_name("Daisy", "Mueller-McQuivey") == "Mueller-McQuivey; Daisy"
    assert make_full_name("", "") == "; "

def test_extract_family_name():
    assert extract_family_name("Doe; John") == "Doe"
    assert extract_family_name("Jackson; Michael") == "Jackson"
    assert extract_family_name("Mueller-McQuivey; Daisy") == "Mueller-McQuivey"
    assert extract_family_name("; ") == ""

def test_extract_given_name():
    assert extract_given_name("Doe; John") == "John"
    assert extract_given_name("Jackson; Michael") == "Michael"
    assert extract_given_name("Mueller-McQuivey; Daisy") == "Daisy"
    assert extract_given_name("; ") == ""


pytest.main(["-v", "--tb=line", "-rN", __file__])
