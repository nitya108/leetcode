# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:43:31 2019

@author: Hi
"""
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def leftview(root,level,maxlevel):
    if root is None:
        return
    
    if (maxlevel[0]<level):
        print(root.data)
        maxlevel[0]=level
        
    leftview(root.left,level+1,maxlevel)
    leftview(root.right,level+1,maxlevel)


#for right view change .right to left and left to right:
#    leftview(root.right,level+1,maxlevel)
#    leftview(root.left,level+1,maxlevel)
root = Node(12) 
root.left = Node(10) 
root.right = Node(20) 
root.right.left = Node(25) 
root.right.right = Node(40) 

maxlevel=[0]
leftview(root,1,maxlevel)