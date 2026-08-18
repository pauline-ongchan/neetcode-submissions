# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # create hashmap:
        # original node -> copied node
        copy = {}
        if not node:
            return None

        def dfs(node):
            # if node was already copied:
                # return its copy from hashmap
            if node in copy:
                return copy[node]

            # create a new copy of node
            copiedNode = Node()
            copiedNode.val = node.val
            
            # store: original node -> copy
            copy[node] = copiedNode

            # go through every neighbor of original node:
            for n in node.neighbors:
                # clone that neighbor
                # add the CLONED neighbor to copy.neighbors
                copiedNode.neighbors.append(dfs(n)) 
            return copiedNode

        return dfs(node)
        
        