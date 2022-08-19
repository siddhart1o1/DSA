nums1 = [4, 5, 6, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3


i = 0
j = 0
while(i < m):
    if(nums1[i] < nums2[j]):
        i += 1
    elif(nums1[i] > nums2[j]):
        temp = nums1[i]
        nums1[i] = nums2[j]
        nums2[j] = temp
        nums2.sort()
    else:
        i += 1


for i in range(m, n+m):
    if(nums1[i] == 0):
        nums1[i] = nums2[j]
        j += 1


print(nums1)
 