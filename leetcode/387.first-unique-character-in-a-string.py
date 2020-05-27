#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (51.72%)
# Likes:    1793
# Dislikes: 113
# Total Accepted:    509K
# Total Submissions: 959K
# Testcase Example:  '"leetcode"'
#
#
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
# Note: You may assume the string contain only lowercase letters.
#
#

# @lc code=start


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            if d.get(c) is not None:
                d[c] = -1
            else:
                d[c] = i
        print(d)
        for k, v in d.items():
            if v != -1:
                return v
        return -1


# @lc code=end
