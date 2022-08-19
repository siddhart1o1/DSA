nums = [1, 3, 2, 3, 1]
def solve(nums):
    ans = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] > nums[j]*2):
                ans += 1

    return ans

ans = solve(nums)
print(ans)