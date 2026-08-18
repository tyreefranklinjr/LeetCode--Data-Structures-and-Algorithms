# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        """
        An in order depth-first search traversal
        with optimal runtime and memory allocation
        using a returned arrow for the pointers
        """
        res = []

        def dfs(root):
            if not root: return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res

        # Time Complexity -> O(N + E) as n is the number of elements in root and E is the number of connections
        # Space Complexity -> O(1) as all auxillary space remains constant
