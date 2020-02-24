#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (32.46%)
# Likes:    430
# Dislikes: 281
# Total Accepted:    58.9K
# Total Submissions: 181.3K
# Testcase Example:  '5'
#
# Given a non-negative integer c, your task is to decide whether there're two
# integers a and b such that a^2 + b^2 = c.
#
# Example 1:
#
#
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
#
#
#
#
# Example 2:
#
#
# Input: 3
# Output: False
#
#
#
#
#

# @lc code=start
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 2:
            return True
        squares = [i**2 for i in range(1, int(math.sqrt(c)) + 1)]
        lower = 0
        upper = len(squares) - 1
        while lower <= upper:
            num_sum = squares[lower] + squares[upper]
            if num_sum == c or squares[lower] == c or squares[upper] == c:
                return True
            if num_sum < c:
                lower += 1
            if num_sum > c:
                upper -= 1
        return False

# @lc code=end
