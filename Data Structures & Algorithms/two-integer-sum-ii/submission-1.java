class Solution {
    public int[] twoSum(int[] numbers, int target) {
        //returning indices in a list
        //1 < less than two. 
        //sorted list
        int start = 0;
        int end = numbers.length - 1;
        while (start != end)
        {
            if (numbers[start] + numbers[end] == target)
            {
                break;
            } else if (numbers[start] + numbers[end] > target)
            {
                end--;
            } else
            {
                start++;
            }
        }
        return new int[]{start + 1, end + 1};
            
    }
}
