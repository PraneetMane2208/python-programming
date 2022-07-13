def mountain_array(arr):
    start=0
    end=len(arr)-1
    while(start<end):

        mid=int(start+(end-start)/2)
        if(arr[mid]>arr[mid+1]):
            end=mid
        else:
            start=mid+1
    return start

# def binary_search(arr,target):
#      ans=-1
#      start=0
#      end=mountain_array(arr)-1
#      while(start<=end):
#         mid=int(start+(end-start)/2)
#         if (target<arr[mid]):
#             end=mid-1
#         elif(target>arr[mid]):
#             start=mid+1
#         else:
#             ans=mid

#      if(ans==-1):
#          start=mountain_array(arr)+1
#          end=len(arr)-1
#          while(start<=end):
#             mid=int(start+(end-start)/2)
#             if (target<arr[mid]):
#                 end=mid-1
#             elif(target>arr[mid]):
#                 start=mid+1
#             else:
#                 ans=mid
#      return ans
def orderagnostic(nums,target,flag,start,end):
    if(flag==1):
        ans=-1
        
        # start=0
        # end=len(nums)-1
        while(start<=end):
            mid=int(start+(end-start)/2)
            if (target<nums[mid]):
                end=mid-1
            elif(target>nums[mid]):
                start=mid+1
            else:
                ans=mid
                end=mid-1
    else:
        ans=-1
        
        start=0
        end=len(nums)-1
        while(start<=end):
            mid=int(start+(end-start)/2)
            if (target<nums[mid]):
                end=mid-1
            elif(target>nums[mid]):
                start=mid+1
            else:
                ans=mid
                start=mid+1

            
                
    return ans

def search(arr,target):
    peak=mountain_array(arr)
    firsttry=orderagnostic(arr,target,1,0,peak)
    if (firsttry!=-1):
        return firsttry
    else:
        return orderagnostic(arr,target,0,peak+1,len(arr)-1)

arr=[1,2,3,4,5,3,1]
b=search(arr,3)
print(b)