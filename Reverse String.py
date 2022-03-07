'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

In computer science, an in-place algorithm is an algorithm which transforms input using no auxiliary data structure

'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        s[:] = s[::-1] # step = -1 means steps one each time but from the end to the start.
        
 # string spilt [from:to:step] - https://www.learnbyexample.org/python-string-slicing/
