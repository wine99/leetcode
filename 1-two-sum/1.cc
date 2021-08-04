#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<pair<int, int>> sorted;

        for (int i = 0; i < n; ++i) {
            sorted.push_back(make_pair(nums[i], i));
        }
        sort(sorted.begin(), sorted.end(), less<>());

        int left = 0;
        int right = n - 1;
        while (left < right) {
            int sum = sorted[left].first + sorted[right].first;
            if (sum < target) {
                ++left;
            } else if (sum > target) {
                --right;
            } else {
                return {sorted[left].second, sorted[right].second};
            }
        }
        return {};
    }
};
