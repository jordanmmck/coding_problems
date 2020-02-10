#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.63%)
# Likes:    2833
# Dislikes: 4437
# Total Accepted:    945K
# Total Submissions: 3.7M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
#
#

# @lc code=start


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x_str = str(x)
        if x_str[0] == '-':
            x_str = x_str[1:]

        rev_x_str = x_str[::-1]
        rev_num = int(rev_x_str)
        if rev_num > 2**31 - 1 or rev_num < -2**31:
            return 0
        return rev_num * sign

# @lc code=end
