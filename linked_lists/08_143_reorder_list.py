class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
            nodes[-1].next = None
        dummy = curr = ListNode(0)
        l, r = 0, len(nodes) - 1
        while l <= r:
            curr.next = nodes[l]
            curr = curr.next
            if l != r:
                curr.next = nodes[r]
                curr = curr.next
            l += 1
            r -= 1
        return dummy.next