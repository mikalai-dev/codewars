#!/usr/bin/python3

"""
A game I played when I was young: Draw 4 cards from playing cards, use + - * / and () to make the final results equal to 24.

You will coding in function equalTo24. Function accept 4 parameters a b c d(4 cards), value range is 1-13.

The result is a string such as "2*2*2*3" ,(4+2)*(5-1); If it is not possible to calculate the 24, please return "It's not possible!"

All four cards are to be used, only use three or two cards are incorrect; Use a card twice or more is incorrect too.

You just need to return one correct solution, don't need to find out all the possibilities.

Examples
equalTo24(1,2,3,4) // can return "(1+3)*(2+4)" or "1*2*3*4"
equalTo24(2,3,4,5) // can return "(5+3-2)*4" or "(3+4+5)*2"
equalTo24(3,4,5,6) // can return "(3-4+5)*6"
equalTo24(1,1,1,1) // should return "It's not possible!"
equalTo24(13,13,13,13) // should return "It's not possible!"
"""

import itertools
import unittest


def operations_sequence(l):
   yield from itertools.product(*([l]*3))

def equal_to_24(a,b,c,d):
    operations = []
    for x in operations_sequence('+-*/'):
       operations.append(''.join(x))
    templates = []
    for oper in operations:
        templates.append("{0}" + oper[0] + "{1}" + oper[1] + "{2}" + oper[2] + "{3}")             # a b c d
        templates.append("({0}" + oper[0] + "{1})" + oper[1] + "{2}" + oper[2] + "{3}")           #(a b) c d
        templates.append("({0}" + oper[0] + "{1}" + oper[1] + "{2})" + oper[2] + "{3}")           #(a b c) d
        templates.append("{0}" + oper[0] + "({1}" + oper[1] + "{2})" + oper[2] + "{3}")           #a (b c) d
        templates.append("{0}" + oper[0] + "({1}" + oper[1] + "{2}" + oper[2] + "{3})")          #a (b c d)
        templates.append("{0}" + oper[0] + "{1}" + oper[1] + "({2}" + oper[2] + "{3})")           #a b (c d)
        templates.append("({0}" + oper[0] + "{1})" + oper[1] + "({2}" + oper[2] + "{3})")         #(a b) (c d)
    operands = list(itertools.permutations([a, b, c, d], 4))
    for template in templates:
        for operand_quartet in operands:
            a,b,c,d = operand_quartet
            try:
                if eval(template.format(a,b,c,d)) == 24:
                    return template.format(a,b,c,d)
            except ZeroDivisionError:
                #just prevent division by zero
                pass

    return """It's not possible!"""

class TestEqualsTo24(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(eval(equal_to_24(1,2,3,4)), 24)

    def test_with_brackets(self):
        self.assertEqual(eval(equal_to_24(2,3,4,5)) , 24)


    def test_for_imposibility(self):
        self.assertEqual((equal_to_24(1,1,1,1)) , "It's not possible!")


if __name__=="__main__":
    unittest.main()
