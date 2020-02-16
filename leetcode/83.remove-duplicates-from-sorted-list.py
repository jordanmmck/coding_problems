#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (44.19%)
# Likes:    1127
# Dislikes: 94
# Total Accepted:    407.4K
# Total Submissions: 921.1K
# Testcase Example:  '[1,1,2]'
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
#
# Example 1:
#
#
# Input: 1->1->2
# Output: 1->2
#
#
# Example 2:
#
#
# Input: 1->1->2->3->3
# Output: 1->2->3
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        temp_node = head
        curr_node = head.next

        while curr_node.next is not None:
            if temp_node.val != curr_node.val:
                temp_node.next = curr_node
                temp_node = curr_node
            curr_node = curr_node.next
        if temp_node.val != curr_node.val:
            temp_node.next = curr_node
        else:
            temp_node.next = None

        return head

        # @lc code=end
