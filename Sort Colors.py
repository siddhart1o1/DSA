nums = [2, 0, 2, 1, 1, 0]



# o(2n)
# def solve2(nums):    
#     one = 0
#     two = 0
#     zero = 0
#     for i in range(len(nums)):
#         if(nums[i] == 0):
#             zero+=1
#         elif(nums[i] == 1):
#             one+=1
#         elif(nums[i] == 2):
#             two+=1


#     for i in range(len(nums)):
#         if(zero > 0):
#             zero-=1
#             nums[i] = 0 
#         elif(one > 0):
#             one-=1
#             nums[i] = 1
#         elif(two > 0):
#             two-=1
#             nums[i] = 2
            
            
            
# dutch national flag
def solve(nums):
    low = 0
    mid = 0
    high = len(nums)-1
    while(mid <= high):
        if(nums[mid] == 1):
            mid+=1

        elif(nums[mid] == 0):
            temp = nums[low]
            nums[low] = nums[mid]
            nums[mid] = temp
            low+=1
            mid+=1

        elif(nums[mid] == 2):
            temp = nums[high]
            nums[high] = nums[mid]
            nums[mid] = temp
            high-=1

        
            
            
    
solve(nums=nums)
print(nums)
