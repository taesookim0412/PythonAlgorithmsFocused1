# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # single pass
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    # double pass
    # def reverseList(self, head: ListNode) -> ListNode:
    #     nodes = []
    #     curr = head
    #     while curr:
    #         nodes.append(curr)
    #         curr = curr.next
    #     res = resHead = ListNode(0)
    #     for node in reversed(nodes):
    #         node.next = None
    #         res.next = node
    #         res = res.next
    #     return resHead.next