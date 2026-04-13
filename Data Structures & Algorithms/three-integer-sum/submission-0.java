class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        //returning all triplets where i j and k are distinct and equal zero
        //brute force iterate through array
        //list of pre, list of elmt, list of after
        //three ptrs
        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(nums);  // Sort to use two-pointer technique

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; // Skip duplicate `i`

            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {
                    ans.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;

                    // Skip duplicates
                    while (left < right && nums[left] == nums[left - 1]) left++;
                    while (left < right && nums[right] == nums[right + 1]) right--;
                }
                else if (sum < 0) left++;
                else right--;
            }
        }

        return ans;
    
    }
}
