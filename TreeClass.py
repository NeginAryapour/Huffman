#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:34:22 2019

@author: negin Aryapour
"""
class Node :
    def __init__(self, key, value, left= None, right = None) :
        self.value = value
        self.left = left
        self.right = right
        self.key = key

class Tree:
    def __init__(self, root = None):
        self.root = root
        self.dic  = dict()
        
        
    def add(self, left_node, right_node):
        node = Node(left_node.key+right_node.key, left_node.value+right_node.value, left_node, right_node )
        self.root = node
        return self.root
    
    
    def isleaf(self, root):
        if root.left == None and root.right == None:
            return True
        return False
    
    
    def search(self , root, string, number):
        if root.left:
            self.search(root.left, string + "0", number+1,)
        if root.right:
            self.search(root.right, string +"1", number+1)
        if self.isleaf(root):
                self.dic[root.key] = (number, string)
        
            
    def write_huffmanfile(self, file):
        _file = open(file, "w")
        for i in self.dic:
            if i == '\0':
                _file.write("EOF"+ "\t"+ str(self.dic[i][0])+ "\t"+ self.dic[i][1]+'\n')
            elif i == '\n':
                _file.write("CR"+ "\t"+ str(self.dic[i][0])+ "\t"+ self.dic[i][1]+'\n')
            else:
                _file.write(i+ "\t"+ str(self.dic[i][0])+ "\t"+ self.dic[i][1]+'\n')
        _file.close()              