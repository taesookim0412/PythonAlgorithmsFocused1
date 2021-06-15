# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd, even = ListNode(0), ListNode(0)
        oddHead, evenHead = odd, even
        curr = head
        i = 0
        while curr:
            if (i + 1) % 2 == 1:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            tempNext = curr.next
            curr.next = None
            curr = tempNext
            i += 1
        odd.next = evenHead.next
        return oddHead.next