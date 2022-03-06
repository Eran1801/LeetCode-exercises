'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_low = s.lower()

        s_check = str()

        # take down all the non-alphanumeric from the string
        for char in s_low:
            if char.isalnum(): # isalnum is a function that return true or false on if the string is Alphanumeric characters that include letters and numbers only.
                s_check += char


        # check if it's a palindrome word by itrate the string in reversed and check equal with the orginal 
        i = 0 
        for char in reversed(s_check):
            if char == s_check[i]:
                i +=1 
            else:
                return False

        return True
      
      
      '''
      Python String isalnum()  - https://www.programiz.com/python-programming/methods/string/isalnum
      Python reversed - https://stackoverflow.com/questions/7961499/best-way-to-loop-over-a-python-string-backwards
      
      '''
      
