from sentences import get_determiner, get_noun, get_verb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    single_noun = ["boy", "girl", "cat", "dog", "bird", "house"]
    for _ in range(7):
        word = get_noun(1)
        assert word in single_noun
    plural_noun = ["birds", "boys", "cars","cats", "children"]
    for _ in range(6):
        word = get_noun(2)
    assert word in plural_noun

def test_get_verb():
    past_tense = ["drank","ate", "grew","laughed","thought","ran"] 
    for _ in range(7):
        word = get_verb("past")
        assert word in past_tense
    present_plural = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps"]
    for _ in range(8):
        word = get_verb("present")
        assert word in present_plural
    else_present = ["drink", "eat", "grow", "laugh", "think","run", "sleep"]
    for _ in range(8):
        word = get_verb("present")
        assert word in else_present 
    future_tense = ["will drink","will eat","will grow","will laugh","will think","will run"]
    for _ in range(7):
        word = get_verb("future")

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])