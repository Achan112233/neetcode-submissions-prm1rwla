class Solution {
    public boolean isPalindrome(String s) {
        s = s.trim().toLowerCase();
        int first = 0;
        int last = s.length() - 1;
        while (first < last){
            while(first < last && !Character.isLetterOrDigit(s.charAt(first))){
                first++;
            }
            while(first < last && !Character.isLetterOrDigit(s.charAt(last))){
                last--;
            }
             if (s.charAt(first) != s.charAt(last)){
                return false;
            }
            first++;
            last--;
        }

        return true;
    }
}
