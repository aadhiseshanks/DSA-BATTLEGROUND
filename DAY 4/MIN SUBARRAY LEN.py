def minSubArraylen(target, nums):
    left = 0
    sum = 0
    min_length = float("inf")
    
    for right in range(len(nums)):
        sum += nums[right]

        while sum >= target:
            min_length = min(min_length, right - left + 1)
            sum -= nums[left]
            left += 1

    return min_length or 0

print(minSubArraylen(7, [2, 3, 1, 2, 4, 3]))
print(minSubArraylen(4, [1, 4, 4]))
print(minSubArraylen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
