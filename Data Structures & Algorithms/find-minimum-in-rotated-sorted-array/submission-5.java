class Solution {
    public int findMin(int[] nums) {
        int high = nums.length - 1;
        int low = 0;

        while (low < high) {
            int mid = (high+low)/2;
            //mid is in left portion
            if (nums[mid] > nums[high]) {
                low = mid + 1;
            //mid is in right portion
            } else if (nums[mid] <= nums[high]) {
                high = mid;
            }
        }

        return nums[low];
    }
}
