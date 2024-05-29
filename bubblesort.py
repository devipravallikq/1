def performBubbleSort(nums):
    n = len(nums)
    while n-1 > 0 :
        for i in range(0,n-1):
            if nums[i] > nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
        print(nums)
        n -= 1
nums = [10,8,2,14,12,7]
print("before sorting:",nums)

performBubbleSort(nums)
print("after sorting:",nums)