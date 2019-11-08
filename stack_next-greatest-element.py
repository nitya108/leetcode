# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
    # For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    # For number 1 in the first array, the next greater number for it in the second array is 3.
    # For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
	
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        d={}
        ans=[]
        
        for x in nums2:
            while len(stack) and stack[-1]<x:
                d[stack.pop()]=x
            stack.append(x)
        
        for x in nums1:
            ans.append(d.get(x,-1))
            
        return ans