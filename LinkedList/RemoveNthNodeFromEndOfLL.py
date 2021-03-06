# Given a linked list, remove the nth node from the end of list and return its head.
# For example,
#    Given linked list: 1->2->3->4->5, and n = 2.
#    After removing the second node from the end, the linked list becomes 1->2->3->5.

  # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Key Step: 2 pointers fast and slow, iterate fast to n, then iterate both till end
# TC: O(n)
# SC: O(1)
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        for _ in xrange(n):
            fast = fast.next
            if not fast:
                return head.next
        while fast:
            fast = fast.next
            current = slow
            slow = slow.next
        current.next = slow.next
        return head