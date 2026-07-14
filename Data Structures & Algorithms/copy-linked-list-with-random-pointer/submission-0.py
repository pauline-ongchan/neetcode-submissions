
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        curr = head
        dummy = Node(0)
        tail = dummy
        mapping = {}

        #val and nexts
        while curr:
            next_node = Node(curr.val)
            tail.next = next_node
            if curr not in mapping:
                mapping[curr] = tail.next
            tail = tail.next
            curr = curr.next
        
        curr2 = dummy.next
        temp = dummy.next
        # doing random
        curr = head
        while curr:
            if curr.random == None:
                curr2.random = None
            else:
                curr2.random = mapping[curr.random]
            curr = curr.next
            curr2 = curr2.next
        return dummy.next
        