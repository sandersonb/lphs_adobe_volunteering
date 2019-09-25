
import random

from lib.adobeanalytics import track

# TODO: Please fill out your student ID:
MY_STUDENT_ID = "bsanders"


def fizzbuzz(number: int) -> str:
    """
    TODO: Fill out your answer here
    Fizzbuzz: print each number on a new line.
    If the number if a multiple of 3, return "Fizz" instead of the number.
    If the number is a multiple of 5, return "Buzz" instead of the number.
    If the number is a multiple of both, return "FizzBuzz" instead of the number.
    :param number:
    :return: your answer
    """

    # TODO: Implement me
    return "Implement me"


if __name__ == '__main__':
    """
    You can change this function if you want, but you don't need to.
    """
    for i in range(10):
        function_input = random.randint(1, 100)
        function_output = fizzbuzz(function_input)
        track('fizzbuzz', MY_STUDENT_ID, str(function_input), function_output)
        print("fizzbuzz(%s) = %s" % (function_input, function_output))
