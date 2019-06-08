#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:44:03 2019

@author: negin Aryapour
"""

class Heap:
    def __init__(self, lst = []):
        self.heap = [0]
        for i in lst:
            self.heap.append(i)
            self.__floatUp(len(self.heap)-1)
        
        
        
    def __floatUp(self, index):
        parrent = index//2
        if index <= 1:
            return 
        elif self.heap[index].value < self.heap[parrent].value:
            self.__swap(index, parrent)
            self.__floatUp(parrent)
        
        
    def __bubbleDown(self, index):
        left = 2* index
        right = 2* index +1
        smallest = index
        if len(self.heap) > left and self.heap[smallest].value > self.heap[left].value:
            smallest = left
        if len(self.heap) > right and self.heap[smallest].value > self.heap[right].value:
            smallest = right
        if smallest != index:
            self.__swap(index, smallest)
            self.__bubbleDown(smallest)
        
    
    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)
        
        
    def peak(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    
        
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            _min = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            _min = self.heap.pop()
        else:
            _min = False
        return _min
            
    
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]