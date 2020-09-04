#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (33.39%)
# Likes:    4045
# Dislikes: 320
# Total Accepted:    461.2K
# Total Submissions: 1.3M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Determine if you are able to reach the last index.
#
#
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# 0 <= nums[i][j] <= 10^5
#
#
#

# @lc code=start


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        if nums[0] >= n-1:
            return True

        jumpers = [False]*n
        jumpers[-1] = True
        for i in range(n-2, -1, -1):
            for j in range(min(i+nums[i], n-1), i, -1):
                if jumpers[j]:
                    jumpers[i] = True
                    break

        return jumpers[0]

# @lc code=end
