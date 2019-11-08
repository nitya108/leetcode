# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number; 
# The second 1's next greater number needs to search circularly, which is also 2.

# Soln:Use the stack to record the reversed array nums. Loop the array from last integer to the first one. 
# If the last integer in stack is bigger than the current interger in array, we have found the answer. 
# Otherwise, we need to keep pop up the integer in stack. Besides, we need to push the current integer to the stack in each step.

class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        ret = [-1] * n
        stack = nums[::-1]
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                ret[i] = stack[-1]
            stack.append(nums[i])
        return ret