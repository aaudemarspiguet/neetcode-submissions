class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
        }
        
        for (int j = 0; j < nums.length; j++){
            int candidate_val = target - nums[j]; 
            if (map.containsKey(candidate_val) && j != map.get(candidate_val)) {
                return new int[] {j, map.get(candidate_val)};
            }
        }
        return new int[] {};
    }
}
