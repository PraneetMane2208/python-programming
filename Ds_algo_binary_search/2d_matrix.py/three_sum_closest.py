class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                s = sum((nums[i], nums[l], nums[r]))
                # if abs(s-target) < abs(res-target):
                #     res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                if abs(s-target) < abs(res-target):
                    res = s
                # else: # break early 
                #     return res
        return res
arr=[-1,2,1,-4]
a=Solution()
print(a.threeSumClosest(arr,1))