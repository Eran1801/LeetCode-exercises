'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_check = str()

        # take down all the non-alphanumeric from the string AND convert the leeter to lower if it is.
        for char in s:
            if char.isalnum():
                s_check += char.lower()
        return s_check == s_check[::-1] #  check if it's a palindrome
      
        
        
   '''
   Python String isalnum()  - https://www.programiz.com/python-programming/methods/string/isalnum
   
   s_check[::-1] - means that same string but in reverse, if s_check was = "Hey" so print(s_check[::-1]) will be "yeH"
   
   '''
      
