class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        x = 0

        for num in nums:
            x ^= num
        
        for num in range(len(nums) + 1):
            x ^= num

        return x
    
print(Solution().missingNumber([3, 0, 1]))
        
        