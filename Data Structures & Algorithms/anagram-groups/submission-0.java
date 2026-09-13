class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<String, List<String>>();
        for (String string:strs) {
            char[] charArray = string.toCharArray();
            Arrays.sort(charArray);
            String sortedStr = new String(charArray);
            if (!map.containsKey(sortedStr)) {
                map.put(sortedStr, new ArrayList<String>());
            }
            map.get(sortedStr).add(string);
        }

        return new ArrayList<>(map.values());
    }
}
