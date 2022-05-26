var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    const current = nums[i];
    const complement = target - current;
    const complement_idx = nums.indexOf(complement, i + 1);
    if (complement_idx > 0) return [i, complement_idx];
  }
};
