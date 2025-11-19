class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        int p = 0;
        for (int i = 0; i < n; i++) {
            while (nums[i] != i + 1 && nums[i] >= 1 && nums[i] <= n && nums[i] != nums[nums[i] - 1]) {
                swap(nums[i], nums[nums[i] - 1]);
            }

        }
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) return i + 1;
        }
        return n + 1;
    }
};

// [3, 4, -1, 1]

// i = 0
// 3 != 1 && 3 >= 1 && 3 <= 4 && 3 != -1 -> swap -> nums = [-1, 4, 3, 1]
// i = 1
// swap -> nums = [-1, 1, 3, 4]
// 1 != 2 && 1 >= 1 && 1 <= 4 && 1 != -1 -> swap -> nums = [1, -1, 3, 4]