# You may serialize the following tree:

    # 1
   # / \
  # 2   3
     # / \
    # 4   5

# as "[1,2,3,null,null,4,5]"

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def recur(node):
            if node:
                res.append(str(node.val))
                recur(node.left)
                recur(node.right)
            else:
                res.append("$")
        res=[]
        recur(root)
        return ' '.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def recur():
            val=next(res)
            if val=='$':
                return None
            node= TreeNode(int(val))
            node.left=recur()
            node.right=recur()
            return node
        res=iter(data.split())
        return recur()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))