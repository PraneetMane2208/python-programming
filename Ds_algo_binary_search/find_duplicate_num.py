def findDuplicate(nums):
    


    low = 0
    high = len(nums) - 1
    mid = (high + low) / 2
    while high - low > 1:
        count = 0
        for k in nums:
            if mid < k <= high:
                count += 1
        if count > high - mid:
            low = mid
        else:
            high = mid
        mid = (high + low) / 2
    return high
nums=[3,1,3,4,2]
b=findDuplicate(nums)
print(b)