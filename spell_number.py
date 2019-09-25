
import random

from lib.adobeanalytics import track

# TODO: Please fill out your student ID:
MY_STUDENT_ID = "bsanders"


def spell_number(number: int) -> str:
    """
    TODO: Fill out your answer here
    Spell Number: spell out the english version of the number on a new line.
    For example, 42 should become "fourty-two" and 6 should become "six"
    :param number: the input integer value < 100 and >= 0
    :return: your answer
    """

    # TODO: Implement me
    return "Implement me"


if __name__ == '__main__':
    """
    You can change this function if you want, but you don't need to.
    """
    for i in range(10):
        function_input = random.randint(1, 99)
        function_output = spell_number(function_input)
        track('spell_number', MY_STUDENT_ID, str(function_input), function_output)
        print("spell_number(%s) = %s" % (function_input, function_output))
