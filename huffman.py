#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:41:44 2019

@author: negin
"""
# class Node :
#     def __init__(self, key, value, left, right) :
#         self.value = value
#         self.left = left
#         self.right = right
        
        
class Heap:
    def __init__(self, lst):
        self.lst = lst
        self.Minheapify()
        
        
    def Minheapify(self):
        i = len(self.lst)-1
        while i != 0:
            if i%2 == 0:
                parrent_i = (i-1)//2
            else:
                parrent_i = i//2
            j = i
            while parrent_i >= 0 and self.lst[j] < self.lst[parrent_i]:
                self.lst[j] , self.lst[parrent_i] = self.lst[parrent_i] , self.lst[j]
                j = parrent_i 
                if parrent_i %2 == 0:
                    parrent_i = (parrent_i -1)//2
                else:
                    parrent_i = parrent_i //2
            i = i -1

def main():

    lst = [3,2,1,5,-9,40,17,-9,99,10]
    print(lst)
    heap = Heap(lst)
    print(heap.lst)
        
    
if __name__ == "__main__":
    main() 
