'''
Given a string s, return the longest palindromic substring in s.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        res_len = 0
        
        for i in range(len(s)):
            # odd length
            left,right = i,i
            while left >= 0 and right < len(s) and s[left] == s[right]: # check if its a Palindromic 
                if ( right - left + 1 ) > res_len:
                    res_len = right-left+1 # update length
                    res = s[left:right+1]  # update Palindromic 

                left -=1
                right +=1
            
            # even length
            left,right = i,i+1
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                if ( right - left + 1 ) > res_len:
                    res_len = right-left+1 
                    res = s[left:right+1]  

                left -=1
                right +=1
                
        return res
