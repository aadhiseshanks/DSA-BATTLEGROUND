from functools import cmp_to_key

def largestNumber(nums):
    num_str = list(map(str, nums))

    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0

    num_str.sort(key = cmp_to_key(compare))
    largest_num = ''.join(num_str)

    return largest_num if largest_num[0] != '0' else '0'

print(largestNumber([10, 2]))
print(largestNumber([3, 30, 34, 5, 9]))
