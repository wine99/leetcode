/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let sorted = Array.from(nums.entries())
                      .sort((a, b) => a[1] - b[1])
    let left = 0
    let right = nums.length - 1
    while (left < right) {
        let sum = sorted[left][1] + sorted[right][1]
        if (sum < target) ++left
        else if (sum > target) --right
        else return [sorted[left][0], sorted[right][0]]
    }
    return []
};
