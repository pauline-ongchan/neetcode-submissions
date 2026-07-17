# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder=[]
        if root is None:
            return inorder
        inorder.extend(self.inorderTraversal(root.left))
        inorder.append(root.val)
        inorder.extend(self.inorderTraversal(root.right))

        return inorder

        