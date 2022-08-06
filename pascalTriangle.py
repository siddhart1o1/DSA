numRows = 5

def solve(numRows):
    arr = [] 
    for i in range(numRows):
        temp = []
        if (i == 0):
            arr.append([1])
        elif (i == 1):
            arr.append([1,1])
        else:
            for j in range(0,i+1):
                if(j == 0 or j == i):
                    temp.append(1)
                else:
                    temp.append(arr[i-1][j-1]+arr[i-1][j])
            arr.append(temp)
    return arr
    
arr = solve(numRows)
print(arr)