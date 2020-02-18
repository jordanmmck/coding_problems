#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (62.76%)
# Likes:    3442
# Dislikes: 135
# Total Accepted:    624.3K
# Total Submissions: 993.2K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,1]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,1,2,1,2]
# Output: 4
#
#
#

# @lc code=start


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor

    # @lc code=end

# I think you want to use the length of the array and the sum
# length of array is always odd
# if sum is odd then answer is odd
# len-1 / 2 is the number of unique numbers being used
# if sum is even then the num is even of course, so ignore all odds
# using XOR
