#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (33.12%)
# Likes:    1226
# Dislikes: 1828
# Total Accepted:    529.6K
# Total Submissions: 1.6M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
#
# Example 1:
#
#
# Input: 4
# Output: 2
#
#
# Example 2:
#
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
# the decimal part is truncated, 2 is returned.
#
#
#

# @lc code=start


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x <= 3:
            return 1

        start = 1
        end = x//2
        while start <= end:
            mid = (start + end) // 2
            if mid**2 <= x and x < (mid+1)**2:
                return mid

            if mid**2 < x:
                start = mid+1
            elif mid**2 > x:
                end = mid-1
            else:
                return mid

    # @lc code=end
