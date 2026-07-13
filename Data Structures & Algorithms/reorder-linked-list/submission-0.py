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
    def reorderList(self, head: Optional[ListNode]) -> List():
        #brute force -> put into array then do the rearranging
        res = []
        curr = head
        
        while curr:
            res.append(curr) 
            curr = curr.next
        
        left = 0
        right = len(res) - 1

        while left < right:
            #connect the front node to the back node
            res[left].next = res[right]
            left += 1
            
            if left == right:
                break
            
            #connect the back node to the next front node 
            res[right].next = res[left]
            right -=1
        res[left].next = None
