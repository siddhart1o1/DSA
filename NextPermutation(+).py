from re import L


arr = [1, 2, 3]


def isSorted(test_list):
    flag = False
    i = 1
    while i < len(test_list):
        if(test_list[i] < test_list[i - 1]):
            flag = True
        i += 1



def solve(arr):
    if(isSorted(arr)) == False:
        
        

solve(arr)