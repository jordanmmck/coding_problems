#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (38.01%)
# Likes:    4056
# Dislikes: 194
# Total Accepted:    841.2K
# Total Submissions: 2.2M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        if len(s) % 2 != 0:
            return False
        start_chars = ('(', '{', '[')
        stack = []
        for c in s:
            if c in start_chars:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c == ')' and stack.pop() != '(':
                    return False
                elif c == '}' and stack.pop() != '{':
                    return False
                elif c == ']' and stack.pop() != '[':
                    return False
        if len(stack) == 0:
            return True

        # @lc code=end
