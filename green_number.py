"""
This is a very simply formulated task. Let's call an integer number N 'green' if N² ends with all of the digits of N. Some examples:

5 is green, because 5² = 25 and 25 ends with 5.

11 is not green, because 11² = 121 and 121 does not end with 11.

376 is green, because 376² = 141376 and 141376 ends with 376.

Your task is to write a function green that returns the nth green number, starting with 1 - green (1) == 1

"""
import unittest

green_cache = [1]

def green(n):
    if len(green_cache) >= n:
        return green_cache[n-1]
    else:
        current = green_cache[-1]
        while len(green_cache) < n:
            current += 1
            squared = current ** 2
            if str(current**2).endswith(str(current)):
                green_cache.append(current)
        return green_cache[n-1]


class TestGreenNumbers(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(green(1), 1)
        self.assertEqual(green(2), 5)
        self.assertEqual(green(3), 6)
        self.assertEqual(green(4), 25)

    def test_bigger_numbers(self):
        self.assertEqual(green(12), 2890625)
        self.assertEqual(green(13), 7109376)

if __name__ == "__main__":
    unittest.main()
