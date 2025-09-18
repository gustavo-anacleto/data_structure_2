class Solution(object):
    def maximumLengthSubstring(self, s):
        l, r, _max = 0, 0, 0
        charMap = {}

        while r < len(s):
            charMap[s[r]] = charMap.get(s[r], 0) + 1

            while charMap[s[r]] > 2:
                charMap[s[l]] -= 1
                l += 1
            
            _max = max(_max, r - l + 1)
            r += 1
        
        return _max;  
        
print(Solution().maximumLengthSubstring("bcbbbcba"))    
        