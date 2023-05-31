#!/usr/bin/python3

"""
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


NOTE: The idea is not sort the elements from the lowest value to the highest;
the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

"""

import unittest

E, S, W, N = (1, 0), (0, 1), (-1, 0), (0, -1)
turn_right = { E:S, S:W, W:N, N:E}

def snail(snail_map):
    result = []
    visited = []
    size = len(snail_map[0])
    x = 0
    y = 0
    direction = E

    if snail_map == [[]]:
        return []

    result.append(snail_map[0][0])
    visited.append((0,0))
    while True:
        if len(visited) == size**2:
            return result

        dx, dy = direction
        new_x, new_y = x + dx, y + dy
        if (0 <= new_x <= size-1 and 0 <= new_y <= size-1 and (new_y, new_x) not in visited):
            x, y = new_x, new_y
            visited.append((y, x))
            result.append(snail_map[y][x])

        else:
            direction = turn_right[direction]


class TestSnailList(unittest.TestCase):
    def test_list_equality(self):
        array = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
        expected = [1,2,3,6,9,8,7,4,5]
        self.assertListEqual(snail(array), expected)

    def test_list_equality2(self):
        array = [[1,2,3],
             [8,9,4],
             [7,6,5]]
        expected = [1,2,3,4,5,6,7,8,9]
        self.assertListEqual(snail(array), expected)


if __name__=="__main__":
    unittest.main()
