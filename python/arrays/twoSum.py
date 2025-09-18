class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        { (targe - nums[i]), i }
        """
        subs = {}

        for i, num in enumerate(nums):
            if subs.get(target - num) is None:
                subs[num] = i
            else:
                return [subs[target -  num], i]

    def twoSumNSquare(self, nums: list[int], target: int) -> list[int]:
        # Implementing with O(n²) solution

        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if num + num2 == target and i != j:
                    return [i, j]
                    


print(Solution().twoSumNSquare([2,7,11,15], 9))

        
        
        
    