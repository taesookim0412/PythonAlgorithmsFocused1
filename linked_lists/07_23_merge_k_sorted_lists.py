# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        while (any(lists)):
            min_list = ListNode(sys.maxsize)
            min_i = -1
            for i, l_list in enumerate(lists):
                if l_list and l_list.val < min_list.val:
                    min_list = l_list
                    min_i = i
            lists[min_i] = lists[min_i].next
            curr.next = min_list
            curr = curr.next
        return dummy.next



