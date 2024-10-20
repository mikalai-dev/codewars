"""
The aim of this kata is to determine the number of sub-function calls made by an unknown function.You have to write a
function named count_calls which:
- takes as parameter a function and its arguments (args, kwargs)
- calls the function
- returns a tuple containing:
- the number of function calls made inside it and inside all the sub-called functions recursively
- the function return value.
NB: The call to the function itself is not counted.
HINT: The sys module may come in handy.

"""

import sys
import unittest

def count_calls(func, *args, **kwargs):
    call_count = -1 # Negative value for not counting the function call itself

    def profile_function(frame, event, arg):
        nonlocal call_count
        if event == 'call':  # Counting function call events
            call_count += 1
        return profile_function

    sys.setprofile(profile_function)
    result = func(*args, **kwargs)
    sys.setprofile(None)

    return (call_count, result)


def add(a, b):
    return a + b


def add_ten(a):
    return add(a, 10)


def misc_fun():
    return add(add_ten(3), add_ten(9))

class TestCountFunctionCalls(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(count_calls(add, 8, 12), (0, 20))
        self.assertEqual(count_calls(add_ten, 5), (1, 15))
        self.assertEqual(count_calls(misc_fun), (5, 32))

if __name__ == '__main__':
    unittest.main()