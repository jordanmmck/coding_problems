#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (45.93%)
# Likes:    7387
# Dislikes: 341
# Total Accepted:    975.8K
# Total Submissions: 2.1M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
#
#

# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None

        max_sum = nums[0]
        curr_sum = nums[0]

        for num in nums[1:]:
            if max_sum <= 0 and num > max_sum:
                max_sum = num
                curr_sum = num
            else:
                curr_sum += num
                if curr_sum > max_sum:
                    max_sum = curr_sum

        return max_sum


# @lc code=end
