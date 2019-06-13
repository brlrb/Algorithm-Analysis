# Definition for a binary tree node.

class TreeNode:
    x = [1,2,3,4,5,6]
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ValidateBSTRecursion:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False
            
            if not helper(node.right,val, upper):
                return False
            
            if not helper(node.left, lower, val):
                return False
            
            return True
        
        return helper(root)

# root = newNode(3) 
# root.left = newNode(2) 
# root.right = newNode(5) 
# root.right.left = newNode(1) 
# root.right.right = newNode(4)