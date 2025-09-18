from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l  =  0
        r = len(nums)
        mid = 0

        while l < r: 
            mid = int((l + r) / 2)  
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid


        return l
                   

print(Solution().searchInsert([1,3,5,6], 1)) 