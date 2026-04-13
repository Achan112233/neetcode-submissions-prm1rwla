class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> numb = new HashSet<>();
        for (int i = 0; i < nums.length; i++){
            if (numb.contains(nums[i])){
                return true;
            } else {
                numb.add(nums[i]);
            }
        }
        return false;
    }
}
