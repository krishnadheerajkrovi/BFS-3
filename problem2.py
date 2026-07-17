"""
1. We create a node using the Node class, but to know we already have create it before ( from the other neighbor ) we use a dictionary to map the old node to the new node.
2. We use DFS to traverse the graph and create a copy of each node and its neighbors
3. We are done when we travel all the nodes and create a copy of each node and its neighbors

TC: O(N)
SC: O(N) 
"""

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {}

        def dfs(node):
            # if this node is already created then just return the new node
            
            if node in oldToNew:
                return oldToNew[node]

            # create copy of current node
            copy = Node(node.val)

            # map new node to old
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node) if node is not None else None
                