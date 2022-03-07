'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = deque()
        
        open_close = { '}':'{' , ']':'[' , ')':'(' }
        
        for p in s:
            if p in open_close:
                # check if the stack is not empty and that the top value in the stack is equal to p
                if stack and stack[-1] == open_close[p]:
                    stack.pop() # delete this brackets from the stack  
                else: # if its a close brackets witout the open brackets 
                    return False
            else:
                stack.append(p)
                
        return True if not stack else False # means if the stack is empty return true false otherwise
            
            
   # deque python - https://www.geeksforgeeks.org/deque-in-python/
