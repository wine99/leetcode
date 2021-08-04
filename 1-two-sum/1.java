class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        int[][] sorted = new int[n][2];

        for (int i = 0; i < n; ++i) {
            sorted[i][0] = nums[i];
            sorted[i][1] = i;
        }
        Arrays.sort(sorted, Comparator.comparingInt(o -> o[0]));

        int left = 0;
        int right = n - 1;
        while (left < right) {
            int sum = sorted[left][0] + sorted[right][0];
            if (sum < target) {
                ++left;
            } else if (sum > target) {
                --right;
            } else {
                return new int[] {sorted[left][1], sorted[right][1]};
            }
        }
        return new int[] {};
    }
}
