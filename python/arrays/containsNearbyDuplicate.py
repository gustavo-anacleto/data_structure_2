class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d = {}
        for i, num in enumerate(nums):
            if num in d and abs(i - d[num]) <= k:
                return True
            d[num] = i
        return False
    
print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 1))
                

                
                