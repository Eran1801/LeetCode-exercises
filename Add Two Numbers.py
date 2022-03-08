'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

It is guaranteed that the list represents a number that does not have leading zeros.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode() # create the ListNode we will return 
        curr = ans # pointer to the head
        
        res_l1 = ""
        res_l2 = ""
        
        while l1:
            res_l1 += str(l1.val)
            l1 = l1.next
            
        while l2:
            res_l2 += str(l2.val)
            l2 = l2.next
            
        res_l1 = int(res_l1[::-1])
        res_l2 = int(res_l2[::-1])
        
        # After this 2 while loop, res_l1/l2 stores the correct numbers in reverse order like it should
        
        res = res_l1 + res_l2
        res = str(res)[::-1] # return to str again to reverse the final result
        
        for i in range(len(res)): # the length of the res is the same as the list we need to return 
            curr.next = ListNode(int(res[i])) # adding the value to the spesfic node
            curr = curr.next # update pointer
        
        return ans.next
    
