# Input: [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation: 
# Without loss of generality, we can assume the root node is at position (0, 0):
# Then, the node with value 9 occurs at position (-1, -1);
# The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
# The node with value 20 occurs at position (1, -1);
# The node with value 7 occurs at position (2, -2).

# Solution:
# ->Root node is considered as 0 horizontal distance.
# ->As we move left hd is decreased by 1 and is increased by 1 as we move right.
# ->vd is used to get the top to bottom series.
# ->comparison in each dic is done based on vd value
# -> if vd comes out to be same then node value is compared.

	def verticalTraversal(self,root):
		dic=collections.defaultdict(list)
		queue=[(root,0,0)]
		ans=[]
		while queue:
			for _ in range(len(queue)):
				node,hd,vd=queue.pop(0)
				dic[hd].append((vd,node.val))
				if node.left:
					queue.append((node.left,hd-1,vd-1))
				if node.right:
					queue.append((node.right,hd+1,vd-1))
		for i in sorted(dic.keys()):
			level=[x[1] for x in sorted(dic[i],key=lambda x:(-x[0],x[1]))]   
			ans.append(level)
		return ans