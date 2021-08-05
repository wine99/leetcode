#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); ++i) {
            int a = nums[i];
            int b = target - nums[i];
            if (map.count(b)) return {map[b], i};
            map[b] = i;
        }
        return {};
    }
};
