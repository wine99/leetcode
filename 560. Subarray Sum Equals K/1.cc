#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count = 0;
        int sum = 0;
        unordered_map<int, int> sums = { {0, 1} };
        for (auto i : nums) {
            sum += i;
            if (sums.find(sum - k) != sums.end())
                count += sums[sum - k];
            sums[sum]++;
        }
        return count;
    }
};
