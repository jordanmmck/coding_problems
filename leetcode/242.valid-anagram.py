#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (54.98%)
# Likes:    1131
# Dislikes: 129
# Total Accepted:    475.9K
# Total Submissions: 864K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
#
# Example 1:
#
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
#
#

# @lc code=start


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True
        if len(s) != len(t):
            return False

        d = {}
        for char in s:
            if d.get(char):
                d[char] += 1
            else:
                d[char] = 1

        for char in t:
            if d.get(char):
                d[char] -= 1
                if d[char] < 0:
                    return False
            else:
                return False

        return sum(list(d.values())) == 0

# iterate over first string, putting chars into dict with each char pointing to its occurrence count
# iterate over next string counting down in the same dict
# if a count dips below zero then False
# assert all entries in dict have been counted down to zero

# @lc code=end
