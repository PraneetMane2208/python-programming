


a=[2,3,3,4,4,7]
# def binary_search_front(a,target):
#     low=0
#     for i in range(len(a)):
#         if (a[i]==target):
#             return i
#             break

# def binary_search_back(a,target):
#     low=0
#     for i in range(len(a)):
#         if (a[len(a)-i-1]==target):
#             return len(a)-i
#             break
# b=binary_search_front(a,4)
# c=binary_search_back(a,4)
# print(b)
# print(c)


# now solving using Binary_search ----Facebook problem

    # def __init__(self,nums,target,find_st_index):
    #     self.nums=nums
    #     self.target=target
    #     self.find_st_index=find_st_index


def first(nums,target):
    
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
            
            
            end=mid-1
    return ans

def last(nums,target,):
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


print("first occurence = ",first(a,4))
print("last occurence = ",last(a,4))