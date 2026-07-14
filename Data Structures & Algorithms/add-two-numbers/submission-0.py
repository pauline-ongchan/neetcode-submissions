# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        ans = 0
        while l1 and l2:
            ans = l1.val + l2.val + carry
            ansNode = ListNode((ans % 10))
            tail.next = ansNode
            carry = int(ans/10)
            l1 = l1.next
            l2 = l2.next
            tail = tail.next

        while l1:
            ans = l1.val + carry
            ansNode = ListNode((ans % 10))
            tail.next = ansNode
            carry = int(ans/10)
            l1 = l1.next
            tail = tail.next
        
        while l2:
            ans = l2.val + carry
            ansNode = ListNode((ans % 10))
            tail.next = ansNode
            carry = int(ans/10)
            l2 = l2.next
            tail = tail.next
        
        if carry != 0:
            ansNode = ListNode(carry)
            tail.next = ansNode
            tail = tail.next
        
        return dummy.next
