# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self,root):
        mini=[0]
        maxi=[0]
        res=[]
        k=[]
        self.findminmax(root,mini,maxi,0)
        for line in range(mini[0],maxi[0]+1):
            self.printvline(root,line,0,k)
            res.append(k)
            k=[]
        return res
            
    def findminmax(self,node,mini,maxi,hd):
        if node is None:
            return
        if hd<mini[0]:
            mini[0]=hd
        if hd>maxi[0]:
            maxi[0]=hd
        self.findminmax(node.left,mini,maxi,hd-1)
        self.findminmax(node.right,mini,maxi,hd+1)
    
    def printvline(self,node,line,hd,res):
        if node is None:
            return
        if hd==line:
            res.append(node.val)
        self.printvline(node.left,line,hd-1,res)
        self.printvline(node.right,line,hd+1,res)