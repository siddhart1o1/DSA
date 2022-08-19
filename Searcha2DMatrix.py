
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]


def binary_search(arr, target):
    mid = arr[len(arr)//2]
    if mid == target:
        return True
    if len(arr) == 1 and mid != target:
        return False
    if mid < target:
        return binary_search(arr[len(arr)//2: len(arr)], target)
    else:
        return binary_search(arr[0:len(arr)//2], target)

def solve(matrix,target):
    m = len(matrix)
    n = len(matrix[0])
    i = 0
    while(i < m):
        if(matrix[i][0] == target or matrix[i][n-1] == target):
            return True
        else:
            if(matrix[i][0] < target and matrix[i][n-1] > target):
                return binary_search(matrix[i], target)
        i += 1
    return False


ans =  solve(matrix,3312)
print(ans)



