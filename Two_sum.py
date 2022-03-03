def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # if we have a list with len of 2, and the both of them is equal the algo wont work so we check
        if len(nums) == 2:
            return [0,1]
        
        # first we want to save the list for the final result 
        list_copy = nums
        
        nums = sorted(nums) # sorting the list
        
        i = 0 # index that point to start
        j = len(nums) -1 # index that point to end
        
        for index in range(len(nums)):
            if nums[i] + nums[j] == target: # if the sum is target, save the indexs 
                break
            elif nums[i] + nums[j] > target: # if ths sum is to big, keep foward with i index
                j -= 1
            else:
                i += 1 # otherwise, keep foward with j
                
        
        # after we have the indexs now we need to return the orginal indexs of the orginal list 
        
        ans_index = []
        
        for index in range(len(nums)):
            if list_copy[index] == nums[i] or list_copy[index] == nums[j]:
                ans_index.append(index)
        
        return ans_index
        
