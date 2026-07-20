# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0 
        answer = None 
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            # in its current node
            nonlocal count 
            count += 1
            if count == k:
                nonlocal answer 
                answer = node.val
                return 
            inorder(node.right)

        inorder(root)
        return answer
        