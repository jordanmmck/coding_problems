#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (41.94%)
# Likes:    408
# Dislikes: 1315
# Total Accepted:    228.5K
# Total Submissions: 545.2K
# Testcase Example:  '27'
#
# Given an integer, write a function to determine if it is a power of three.
#
# Example 1:
#
#
# Input: 27
# Output: true
#
#
# Example 2:
#
#
# Input: 0
# Output: false
#
# Example 3:
#
#
# Input: 9
# Output: true
#
# Example 4:
#
#
# Input: 45
# Output: false
#
# Follow up:
# Could you do it without using any loop / recursion?
#

# @lc code=start

import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        log = math.log(n, 3)
        if log.is_integer() or 3**round(log) == n:
            return True

        return False


# @lc code=end