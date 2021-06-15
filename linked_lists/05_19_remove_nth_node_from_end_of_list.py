# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from idlelib.tree import TreeNode

from Cython.Compiler.ExprNodes import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = TreeNode(0)
        dummy.next = head
        left = right = dummy
        for i in range(n + 1):
            if right:
                right = right.next
        while right:
            left = left.next
            right = right.next
        if left and left.next:
            left.next = left.next.next
        return dummy.next
