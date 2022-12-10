from grading import make_grade_dict, make_key_dict
import pytest

# Tests the make_grade_function dictionary as a dictionary
def test_grade_dict():
    test_gen_dict = make_grade_dict()
    assert isinstance(test_gen_dict, dict), \
    "make_gen_dict function must return a dictionary: " \
    f" expected a dictionary but found a {type(test_gen_dict)}"
 
# Tests the make_key_dict dictionary as a dictionary
def test_key_dict():
    test_keys_dict = make_key_dict()
    assert isinstance(test_keys_dict, dict), \
    "make_gen_dict function must return a dictionary: " \
    f" expected a dictionary but found a {type(test_keys_dict)}"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])


# Program by Daisy Mueller @ BYU-Idaho
## December 10, 2022