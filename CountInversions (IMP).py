arr = [2, 5 ,1, 3, 4]
# def solve(arr):
#     count = 0
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 count += 1
#     return count


def merge(arr, start, mid, end):
    count = 0
    temp = []
    i = start
    j = mid + 1
    while i < mid + 1 and j < end + 1:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            count = count + (mid - i + 1)

    while i < mid + 1:
        temp.append(arr[i])
        i += 1

    while j < end + 1:
        temp.append(arr[j])
        j += 1
        count = count + (mid - i + 1)

    arr[start:end+1] = temp
    return count


def solve(arr, start, end):
    count = 0
    if start < end:
        mid = (start + end) // 2
        count += solve(arr, start, mid)
        count += solve(arr, mid + 1, end)
        count += merge(arr, start, mid, end)

    return count


print(solve(arr, 0, len(arr)-1))
