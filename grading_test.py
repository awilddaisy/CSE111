from grading import make_grade_dict, \
    make_key_dict
from pytest import approx
import pytest

# grades_dict = make_grade_dict()
# keys_dict = make_key_dict()

def test_grade_dict():
    assert make_grade_dict('5.6-') == [0]
    assert make_grade_dict('5.10') == [13]
    assert make_grade_dict('5.10-') == [12]

def test_key_dict():
    assert make_key_dict('0') == '5.6-'
    assert make_key_dict('4') == '5.7'
    assert make_key_dict('20') == '5.12+'





# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
