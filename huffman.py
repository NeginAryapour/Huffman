#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:41:44 2019

@author: negin Aryapour
"""

        
        
from heap import Heap
from TreeClass import *
import re
  
            
def frequency(file):
    freq = dict()
    text_file = file.read()
    for i in text_file[:-1]:
        freq[i] = freq.get(i, 0) + 1
    freq['\0'] = 1
    return freq


def make_zip(dic, file):
#    print(dic)
    temp = ""
    zip_file = open("Zip.txt","w")
    base_file = open(file,"r")
    base_file_txt = base_file.read()
    for i in base_file_txt[:-1]:
        temp += dic[i][1]
    temp += dic['\0'][1]
    temp += (8 -(len(temp)%8))* "0"
    j = 0
    char = ""
    string = ""
    for i in range(len(temp)//8):
        string = temp[j:j+8]
        a = int(string, 2)
        c = chr(a)
        char += c
        j +=8
    zip_file.write(char) 
    zip_file.close()
    base_file.close()


def unZip(huffmanTxtFile, zipTxtFile):
    dic = dict()
    code = ""
    unzipedFile = open("Input.txt", "w")
    unzip_txt = ""
    hfile = open(huffmanTxtFile,"r")
    zfile = open(zipTxtFile,"r")
    zfile_txt = zfile.read()
    for line in hfile:
        ls = re.split(r'\t+', line)
        dic[ls[2][:-1]] = ls[0]
    for i in zfile_txt:
        code += '{0:08b}'.format(ord(i))
    c = ""
    for i in code:
        if c in dic:
            if dic[c] == 'CR':
                unzip_txt += '\n'
            elif dic[c] == 'EOF':
                unzip_txt += '\0'
                break
            else:
                unzip_txt += dic[c]
            c = i
        else:
            c+=i
    unzipedFile.write(unzip_txt)  
    
    
def main():
    lst = []
    tree = Tree(None)
    file = open("Input.txt", "r")
                                    #claculate the frequency of each diffrent character of input.txt file
    frequen = frequency(file)
    file.close()
                                    #make heap of each diffrent characters              
    for i in frequen:
        lst.append(Node(i, frequen[i], None, None))
    h = Heap(lst)
    while len(h.heap) > 2:
        left_node = h.pop()
        right_node = h.pop()
        root_node = tree.add(left_node, right_node)
        h.push(root_node)
    tree.search(tree.root,"",0)
    tree.write_huffmanfile("Huffman.txt")
    make_zip(tree.dic, "Input.txt")
    unZip("Huffman.txt", "Zip.txt")
    

if __name__ == "__main__":
    main() 