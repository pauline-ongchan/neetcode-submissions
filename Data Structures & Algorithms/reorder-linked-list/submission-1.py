 # rearrange to index 0, n-1, 1, n-2, 2, n-3, ...
        # example 1:
        # [2, 4, 6, 8]
        # [0, 1, 2, 3]
        # [2, 8, 4, 6]
        # [0, 3, 1, 2]
        
        #example 2:
        #[2, 4, 6, 8, 10]
        #[2. 10, 4, 8, 6]

        # first node -> last node -> second node -> second to the last node
        # maybe do middle
        # 2 -> 4 -> 6 -> 8 -> 10 
        # i 

        #temp -> tail 
        #temp -> 2
        # 2 -> 10 

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        l1 = head
        l2 = slow.next
        slow.next = None

        l2 = self.reverseLinkedList(l2)

        dummy = ListNode()
        tail = dummy

        while l2:
            next1 = l1.next
            next2 = l2.next
            
            l1.next = l2
            l2.next = next1
            l1 = next1
            l2 = next2
        

    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev