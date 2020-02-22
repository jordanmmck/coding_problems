#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
#
# algorithms
# Medium (53.18%)
# Likes:    433
# Dislikes: 41
# Total Accepted:    41.5K
# Total Submissions: 78K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty integer array, find the minimum number of moves required to
# make all array elements equal, where a move is incrementing a selected
# element by 1 or decrementing a selected element by 1.
#
# You may assume the array's length is at most 10,000.
#
# Example:
#
# Input:
# [1,2,3]
#
# Output:
# 2
#
# Explanation:
# Only two moves are needed (remember each move increments or decrements one
# element):
#
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
#
#
#

# @lc code=start
import statistics


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = statistics.median(nums)
        total_steps = 0
        for num in nums:
            total_steps += abs(num - median)
        return int(total_steps)

    # @lc code=end

# it seems that you want to find the average...
# the mean is the value which is closest to all other values
# the mean is the center to which you must go
# once you know the center you can simply sum the differences?
# the median is the center, not avg
