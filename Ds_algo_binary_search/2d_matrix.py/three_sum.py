def threeSum(self, nums):
        nums.sort()
        ans = []
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] > 0: break  # Since arr[i] <= arr[l] <= arr[r], if arr[i] > 0 then sum=arr[i]+arr[l]+arr[r] > 0
            l = i + 1
            r = n - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l+1 < n and nums[l+1] == nums[l]: l += 1  # Skip duplicates nums[l]
                    l += 1
                    r -= 1
                elif sum3 < 0: l += 1
                else: r -= 1
                
            while i+1 < n and nums[i+1] == nums[i]: i += 1  # Skip duplicates nums[i]
            i += 1
        return ans