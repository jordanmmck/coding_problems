#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.65%)
# Likes:    1988
# Dislikes: 1654
# Total Accepted:    635.1K
# Total Submissions: 1.8M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#
#

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_pre = ''
        current_letter = ''

        shortest_len = 99999
        for word in strs:
            if len(word) < shortest_len:
                shortest_len = len(word)

        for i in range(shortest_len):
            for j, word in enumerate(strs):
                if j == 0:
                    current_letter = word[i]
                if word[i] != current_letter:
                    return common_pre
                if j == len(strs) - 1:
                    common_pre += current_letter

        return common_pre

        # @lc code=end
