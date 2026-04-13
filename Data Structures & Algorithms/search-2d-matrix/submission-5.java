class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int startOut = 0;
        int startEnd = matrix.length - 1;
        while (startOut <= startEnd){
            int midOut = (startOut + startEnd) / 2;
            if (matrix[midOut][0] <= target && (midOut == startEnd||matrix[midOut + 1][0] > target)){
                int endOut = 0;
                int endEnd = matrix[midOut].length - 1;
                while (endOut <= endEnd){
                    int midMid = (endOut + endEnd) / 2;
                    if (matrix[midOut][midMid] == target){
                        return true;
                    } else if (matrix[midOut][midMid] < target){
                        endOut = midMid + 1;
                    } else {
                        endEnd = midMid - 1;
                    }
                }
                return false;
            } else if (matrix[midOut][0] < target){
                startOut = midOut + 1; 
            } else {
                startEnd = midOut - 1;
            }
        }
        return false;
    }
}
