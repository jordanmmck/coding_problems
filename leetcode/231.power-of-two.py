#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (42.75%)
# Likes:    603
# Dislikes: 156
# Total Accepted:    271.1K
# Total Submissions: 633.8K
# Testcase Example:  '1'
#
# Given an integer, write a function to determine if it is a power of two.
#
# Example 1:
#
#
# Input: 1
# Output: true
# Explanation: 2^0 = 1
#
#
# Example 2:
#
#
# Input: 16
# Output: true
# Explanation: 2^4 = 16
#
# Example 3:
#
#
# Input: 218
# Output: false
#
#

# @lc code=start


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 or n == 2:
            return True

        while n > 2:
            n /= 2
            if not n.is_integer():
                return False

        if n == 2:
            return True

# @lc code=end
