#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (48.36%)
# Likes:    1423
# Dislikes: 324
# Total Accepted:    325.7K
# Total Submissions: 671.7K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
#
# Example: 
#
#
# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#

# @lc code=start


class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        previous_sums = []
        while True:
            square_sum = 0
            for char in s:
                square_sum += int(char)**2
            if square_sum == 1:
                return True
            if square_sum in previous_sums:
                return False
            previous_sums.append(square_sum)
            s = str(square_sum)


# @lc code=end
