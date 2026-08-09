class Solution {
    public int singleNumber(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int k = 0;
            for (k = i + 1; k < nums.length; k++) {
                if (nums[i] == nums[k]) {
                    swap(nums, i + 1, k);
                    i++;
                    break;
                }
            }
            if (k == nums.length) {
                return nums[i];
            }
        }
        return 0;
    }

    public static void swap(int[] array, int index1, int index2) {
        int tmp = array[index1];
        array[index1] = array[index2];
        array[index2] = tmp;
    }
}
