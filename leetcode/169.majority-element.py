#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (56.30%)
# Likes:    2981
# Dislikes: 215
# Total Accepted:    621.5K
# Total Submissions: 1.1M
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
#
#

# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # moore's voting alg
        candidate = None
        votes = 1
        for num in nums:
            if num == candidate:
                votes += 1
            else:
                votes -= 1
                if votes == 0:
                    candidate = num
                    votes = 1
        return candidate


# @lc code=end
