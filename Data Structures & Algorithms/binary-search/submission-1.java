class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        while (l <= r){
            int idx = (l + r) / 2;
            if (nums[idx] == target){
                return idx;
            } else if (nums[idx] < target){
                l = idx + 1;
            } else {
                r = idx - 1;
            }
        }
        return -1;
    }
}
