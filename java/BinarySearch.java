package java;
public class BinarySearch {
    public static void main(String[] args) {
        System.out.println(Solution.search(new int[] {1, 2, 3, 4, 5}, 3));
    }
}

class Solution {
    public static int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1, steps = 0;

        while (left <= right) {
            steps++;
            int mid = (left + right) / 2;
            
            if(nums[mid] == target){
                System.out.println("Steps: " + steps);
                return nums[mid];
            } else if(target < nums[mid]){
                right = mid - 1;
            } else {
                left = mid + 1; 
            }
        }

        return -1;
    }
}