package java;
import java.util.HashMap;
import java.util.Map;

public class MaximumLengthSubstring {
    public static void main(String[] args) {
        System.out.println(Solution.maximumLengthSubstring("aaaa"));
    }
}

class Solution {
    public static int maximumLengthSubstring(String s) {
        int pl = 0, pr = 0, max = 0;

        Map<Character, Integer> charMap = new HashMap<>();

        while (pr < s.length()) {
            charMap.merge(s.charAt(pr), 1, Integer::sum);
            
            while (charMap.get(s.charAt(pr)) > 2) {
                charMap.put(s.charAt(pl), charMap.get(s.charAt(pl)) - 1);
                pl++;
            }
            
            pr++;
            max = Math.max(max, pr - pl);
            
        }

        return max;
    }
}