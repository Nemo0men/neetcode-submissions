class Solution {
    public boolean hasDuplicate(int[] nums) {
        //if number is not in array, put it in array
        HashSet<Integer> storage = new HashSet<>();
        for (int num : nums) {
            if (storage.contains(num)) {
                return true;
            }
            else {storage.add(num);}
        }
        return false;
        //if number is in array, return true
        //return false
 
    }
}
