def maxProduct(nums):
    nums.sort()
    a = nums[-2]
    b = nums[-1]
    return (a-1)(b-1)
print(maxProduct([1, 2, 3]))
