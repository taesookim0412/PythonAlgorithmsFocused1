# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        vals = []
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next
        vals.sort()
        for val in vals:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next



