matrix = [[2, 3],[1, 5]]

# [[1,4]]

def Mergable(first,second):
    first.sort()
    second.sort()
    temp = []
    if(first[0] >= second[0]):
        return second[0]
    elif(first[-1] >= second[0]):
        return first[0]
    else:
        return -1
    



def solve(intervals):
    i = 0
    temp = []
    while(i < len(intervals)-1):
        if(intervals[i] != -1):
            j = i+1
            while(j < len(intervals[i])):
                if(intervals[j] != -1):
                    res =  Mergable(intervals[i], intervals[j])
                    if(res != -1):
                        temp.append(intervals[i][res])
                        temp.append(intervals[j][len(intervals[j])-1])
                        intervals[i] = temp
                        intervals[j] = -1
                j += 1
        i += 1

    new = []
    for i in range(len(intervals)):
        if(intervals[i] != -1):
            new.append(intervals[i])

    return new


matrix = solve(matrix)
print(matrix)
