# Input: [-10,9,20,null,null,15,7]

   # -10
   # / \
  # 9  20
    # /  \
   # 15   7

# Output: 42

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxutil(root):
            if root is None:
                return 0
            l = maxutil(root.left)
            r = maxutil(root.right)
            
            maxsingle=max(max(l,r)+root.val,root.val)
            
            maxtop=max(maxsingle,l+r+root.val)
            
            maxutil.res=max(maxutil.res,maxtop)
            
            return maxsingle
        maxutil.res=float('-inf')
        maxutil(root)
        return maxutil.res
        