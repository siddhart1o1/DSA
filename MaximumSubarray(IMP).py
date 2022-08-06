from array import array


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def solve(nums):    
    max =  -2147483648
    sum = 0 
    for i in range(len(nums)):
        sum = sum + nums[i]
        if(max < sum):
            max = sum
        if(sum < 0):
            sum = 0        
    return max


    
sol = solve(nums)
print(sol)