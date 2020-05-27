#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (51.89%)
# Likes:    3894
# Dislikes: 570
# Total Accepted:    955.4K
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        l3_head = None
        l3 = None

        if l1.val < l2.val:
            l3_head = l1
            l1 = l1.next
        else:
            l3_head = l2
            l2 = l2.next

        l3 = l3_head

        while True:
            if l1 is None:
                l3.next = l2
                return l3_head
            if l2 is None:
                l3.next = l1
                return l3_head

            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next

            l3 = l3.next


# @lc code=end
