# For example:
# Given binary tree [3,9,20,null,null,15,7],
    # 3
   # / \
  # 9  20
    # /  \
   # 15   7
# return its zigzag level order traversal as:
# [
  # [3],
  # [20,9],
  # [15,7]
# ]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return 
        currentlevel=[]
        nextlevel=[]
        ltr=True
        currentlevel.append(root)
        result=[]
        x=[]
        
        while len(currentlevel)>0:
            temp=currentlevel.pop(-1)
            x.append(temp.val)
            
            if ltr:
                if temp.left:
                    nextlevel.append(temp.left)
                if temp.right:
                    nextlevel.append(temp.right)
            else:
                if temp.right:
                    nextlevel.append(temp.right)
                if temp.left:
                    nextlevel.append(temp.left)
            
            if len(currentlevel)==0:
                result.append(x)
                x=[]
                currentlevel,nextlevel=nextlevel,currentlevel
                ltr= not ltr
        
        return result