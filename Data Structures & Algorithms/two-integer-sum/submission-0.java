class Solution {
    public int[] twoSum(int[] nums, int target) {
        int solution1;
        int solution2;
        HashMap<Integer, Integer> storage = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            solution2 = i;
            if (storage.containsKey(target - nums[i])) {
                solution1 = storage.get(target - nums[i]);
                return new int[] {solution1, solution2};
            }
            else {storage.put(nums[i], i);}
        }
        return new int[] {};
    }
}
