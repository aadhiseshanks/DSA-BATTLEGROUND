def minimumdifference(nums, k):
    if k == 1:
        return 0

    nums.sort()
    min_value = float("inf")
    for i in range(len(nums) - k + 1):
        current_value = nums[i+k-1] - nums[i]
        min_value = min(min_value, current_value)

    return min_value

print(minimumdifference([90], 1))
print(minimumdifference([9, 4, 1, 7], 2))
