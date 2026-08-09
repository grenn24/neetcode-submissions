# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        curr = prev

        # zig zag
        while curr:
            tmp1 = head.next
            tmp2 = curr.next

            head.next = curr
            curr.next = tmp1

            head = tmp1
            curr = tmp2


