# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        """
        Avoid brute force options and addresses the problem
        with a depth-first search solution, utilizing a range
        to determine if the node's position int he binary tree
        is valid
        """
         
        def dfs(node, left, right):
            if not node: return True

            if not (node.val < right and node.val > left): return False

            return (dfs(node.left, left, node.val) and dfs(node.right, node.val, right))

        return dfs(root, float("-inf"), float("inf"))

        # Time Complexity -> O(N) as N is the number of elements in root
        # Space Complexity -> O(1) as the number of auxillary space remains constant
