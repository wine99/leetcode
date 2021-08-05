/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map()
    for (let [i, a] of nums.entries()) {
        const b = target - a
        if (map.has(b)) return [map.get(b), i]
        map.set(a, i)
    }
    return []
};
