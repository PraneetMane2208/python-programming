def four_sum(nums,target):

    nums.sort()
    n, ans = len(nums), []
    for i in range(n):
        for j in range(i + 1, n):
            goal = target - nums[i] - nums[j]
            beg, end = j + 1, n - 1

            while beg < end:
                if nums[beg] + nums[end] < goal:
                        beg += 1
                elif nums[beg] + nums[end] > goal:
                            end -= 1
                else:

                    ans.append((nums[i], nums[j], nums[beg], nums[end]))
                    beg+= 1
                    end -= 1

    return set(ans)
    # arr.sort()
    # n=len(arr)
    # ans=[]
    # for i in range(n):
    #     for j in range(i+1,n):
    #         aim=target-arr[i]-arr[j]
    #         start=j+1
    #         end=n-1
    #         while(start<end):
    #             if(arr[i]+arr[j]<aim):
    #                 start+=1
    #             if(arr[i]+arr[j]>aim):
    #                 end-=1
    #             else:
    #                 ans.append((arr[i],arr[j],arr[start],arr[end]))
    #                 start+=1
    #                 end-=1
    # return set(ans)

arr=[4,-3,6,3,5,0]
b=four_sum(arr,12)
print(b)