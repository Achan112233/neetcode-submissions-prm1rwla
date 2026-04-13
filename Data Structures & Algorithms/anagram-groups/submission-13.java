class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //iterate through array strs
        //group all anagrams together, (same letters, same freq)
        //hashMap might be useful for freq.
        //actually, we can try to get the freq of each letter, and make that the key, then the val would be an array
        //return the list where they grouped...
        HashMap<HashMap<Character, Integer>, ArrayList<String>> mapss = new HashMap<>();
        List<List<String>> ans = new ArrayList<>();
        for (int i = 0; i < strs.length; i++)
        {
            HashMap<Character, Integer> freq = new HashMap<>();
            for (int j = 0; j < strs[i].length(); j++)
            {
                if (freq.containsKey(strs[i].charAt(j)))
                {
                    freq.put(strs[i].charAt(j), freq.get(strs[i].charAt(j)) + 1);
                } else {
                    freq.put(strs[i].charAt(j), 1);
                }
            }
            if (!mapss.containsKey(freq))
            {
                mapss.put(freq, new ArrayList<String>());
            }
            mapss.get(freq).add(strs[i]);
        }
        return new ArrayList<>(mapss.values());
    }
}
