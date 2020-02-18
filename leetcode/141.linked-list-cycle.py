#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (39.46%)
# Likes:    2277
# Dislikes: 340
# Total Accepted:    537.2K
# Total Submissions: 1.4M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which
# represents the position (0-indexed) in the linked list where tail connects
# to. If pos is -1, then there is no cycle in the linked list.
#
#
#
#
# Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
#
#
#
#
#
#
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
#
#
#
#
#
#
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
#
#
#
#
#
# Follow up:
#
# Can you solve it using O(1) (i.e. constant) memory?
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1 = head
        p2 = head
        while head and p1.next and p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True

        return False
        # @lc code=end
