class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    cursor = ListNode(0)
    start = cursor
    while l1 and l2:
        if l1.val <= l2.val:
            cursor.next = l1
            l1 = l1.next
        else:
            cursor.next = l2
            l2 = l2.next
        cursor = cursor.next
    if l1 is None:
        cursor.next = l2
    elif l2 is None:
        cursor.next = l1
    return start.next