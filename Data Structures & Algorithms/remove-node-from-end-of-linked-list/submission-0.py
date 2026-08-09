# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        curr1 = head
        while curr1:
            length += 1
            curr1 = curr1.next

        if n == length:
            return head.next

        count = 0
        curr2 = head

        while count < length:
            if count == (length - n - 1):
                if curr2.next is not None:
                    curr2.next = curr2.next.next
                else:
                    curr2.next = None
                break
                

            curr2 = curr2.next
            count += 1

        return head