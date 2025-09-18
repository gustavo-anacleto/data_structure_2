class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
            {l, [0, 2]}
            {c, [1, 1]} - my goal
            {e, [2, 1]}
        """
        charMap = {}
        
        for idx, ch in enumerate(s):
            if not charMap.get(ch):
                charMap[ch] = [idx, 1]
            else:
                charMap[ch][1] += 1
             
        for _, vals in charMap.items():
            if vals[1] == 1:
                return vals[0]

        return -1

            
print(Solution().firstUniqChar("leetcode"))        

        