def dub(nums):
    slow = nums[0]
    fast = nums[0]
    while(True):
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    fast = nums[0]
    while(fast != slow):
        fast = nums[fast]
        slow = nums[slow]

    return fast


def solve(A):
    dublicate = dub(A)
    for i in 
    
solve()