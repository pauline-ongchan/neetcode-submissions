# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        ll = []
        while curr:
            ll.append(curr.val)
            curr = curr.next
        l = 0
        r = len(ll) - 1
        while l <= r:
            if ll[l] != ll[r]:
                return False
            else:
                l += 1
                r -= 1
        return True


        