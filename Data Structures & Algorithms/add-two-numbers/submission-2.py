# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode(val=0, next=None)
        curr = dummy

        while l1 is not None or l2 is not None:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            sum = l1Val + l2Val + carry
            newDigit = sum % 10
            carry = sum // 10

            curr.next = ListNode(val=newDigit, next=None)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry != 0:
            curr.next = ListNode(val=carry, next=None)

        return dummy.next