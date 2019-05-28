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
        if (len(self.lst) == 0):
            return
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
            
            
    def MinExtract(self):
        root = self.lst[0]
        last_member = len(self.lst)-1
        self.lst[0] , self.lst[last_member] = self.lst[last_member] , self.lst[0]
        self.lst.pop()
        self.Minheapify()
        return root
    
    
    def HeapSort(self):
        mini_lst = []
        leng = len(self.lst)
        for i in range(leng):
            mini_lst.append(heap.MinExtract())
        return mini_lst


def main():

    lst = [-9,8,-19,60,78,34,65,2,12,30]
    print(lst)
    heap = Heap(lst)
    print(heap.lst)
    mini = []
    print(mini)
    print(heap.lst)
    leng = len(heap.lst)
    for i in range(leng):
        mini.append(heap.MinExtract())
    print(mini)
    
    
        
    
if __name__ == "__main__":
    main() 
