public class Solution {
    public boolean hasDuplicate(int[] nums) {
        if (nums.length == 0) {
            return false;
        }

        int point1 = 0;
        int point2 = 1;

        while (point1 < nums.length - 1) {
            if (point2 >= nums.length) {
                point1++;
                point2 = point1 + 1;
                continue;
            }

            if (nums[point1] == nums[point2]) {
                return true;
            }

            point2++;
        }

        return false;
    }
}