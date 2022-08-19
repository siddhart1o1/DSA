
def solve(n,m,i,j,hash):
    if(i > n or j > m):
        return 0
    if(hash[i][j] != -1):
        return hash[i][j]
    if(n==i and m ==j):
        return 1
    hash[i][j] = solve(n,m,i+1,j,hash) + solve(n,m,i,j+1,hash)
    return hash[i][j]

n = 3
m = 7
n = n-1
m = m-1
i = 0
j = 0
hash = [[-1 for x in range(m+1)] for y in range(n+1)]
print(hash)
print(solve(n,m,i,j,hash))
print(hash)