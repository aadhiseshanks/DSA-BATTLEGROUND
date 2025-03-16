def find_first_and_last(nums, target):
    result = [-1, -1]
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2  
        if nums[mid] == target:
            result[0] = mid
            result[1] = mid

            while result[0] > 0 and nums[result[0] - 1] == target:
                result[0] -= 1

            while result[1] < len(nums) - 1 and nums[result[1] + 1] == target:
                result[1] += 1

            return result
            
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

print(find_first_and_last([5, 7, 7, 8, 8, 10], 8))
print(find_first_and_last([5, 7, 7, 8, 8, 10], 6))
