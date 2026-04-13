class Solution {

    int[] count;
    public String encode(List<String> strs) {
        int i = 0;
        count = new int[strs.size()];
        String ans = "";
        for (String str : strs)
        {
            count[i++] = str.length(); 
            ans += str;
        }
        return ans;
    }

    public List<String> decode(String str) {
        //iterate through count to get the length of each string
        int j = 0;
        ArrayList<String> ans = new ArrayList<>();
        for (int i = 0; i < count.length; i++)
        {
            int lim = count[i];
            String word = "";
            for (int k = 0; k < lim; k++)
            {
                word += str.charAt(j++); 
            }
            ans.add(word);
        }
        return ans;
    }
}
