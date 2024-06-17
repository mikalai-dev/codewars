"""
Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses

Examples
balanced_parens(0) => [""]
balanced_parens(1) => ["()"]
balanced_parens(2) => ["()()","(())"]
balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]

"""

import unittest
def balanced_parens(n):
    if n == 0:
        return [""]
    elif n == 1:
        return ["()"]

    parens = []
    for item in balanced_parens(n - 1):
        parens += [item[:i] + "()" + item[i:] for i in range(0, len(item))]
    return list(set(parens))


class TestBalancedParens(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(sorted(balanced_parens(0)), sorted([""]))
        self.assertEqual(sorted(balanced_parens(1)), sorted(["()"]))
        self.assertEqual(sorted(balanced_parens(2)), sorted(["()()","(())"]))
        self.assertEqual(sorted(balanced_parens(3)), sorted(["()()()","(())()","()(())","(()())","((()))"]))


if __name__ == "__main__":
    unittest.main()
