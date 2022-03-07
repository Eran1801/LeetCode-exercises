'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

from collections import deque # deque is a Doubly Ended Queue

class Solution:
    def isValid(self, s: str) -> bool:
        
        queue = deque()
        
        open_close = { '}':'{' , ']':'[' , ')':'(' }
        
        for p in s:
            if p in open_close:
                # check if the stack is not empty and that the top value in the stack is equal to p
                if queue and queue[-1] == open_close[p]:
                    queue.pop() # delete this brackets from the stack  
                else: # if its a close brackets witout the open brackets 
                    return False
            else:
                queue.append(p)
                
        return True if not queue else False # means if the stack is empty return true false otherwise
            
            
   # deque python - https://www.geeksforgeeks.org/deque-in-python/
