class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = res = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            l1Val = l2Val = 0
            if l1 and l1.val:
                l1Val = l1.val
            if l2 and l2.val:
                l2Val = l2.val
            val = l1Val + l2Val + carry
            carry = val // 10
            while val >= 10:
                val -= 10
            res.next = ListNode(val)
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next