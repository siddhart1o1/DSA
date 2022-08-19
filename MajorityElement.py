nums = [2, 2, 1, 1, 1, 2, 2]

# n/2
def solve(nums):
    dict = {}
    max =0
    res = 0
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
        if dict[i] > max:
            max = dict[i]
            res = i
    return res

     
# n/2
def optimized(nums):
    count = 0
    candidate = 0
    for i in nums:
        if(candidate == 0):
            candidate = i
        if(i == candidate):
            count += 1
        else:
            count -= 1
    
    return count



ans = solve(nums)
print(ans)