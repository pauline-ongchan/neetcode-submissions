# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode()
        tail = dummy
        while curr:
            if curr.val == val:
                tail.next = curr.next
            else:
                tail.next = curr
                tail = tail.next
            curr = curr.next
        return dummy.next

        