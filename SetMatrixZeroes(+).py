from ast import MatchSequence

matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# o(nm) space
def makeDigonalZeroes(matrix,i,j):
    orignali = i
    originalj = j
    for i in range(len(matrix)):
        matrix[i][originalj] = 0
    for j in range(len(matrix[orignali])):
        matrix[orignali][j] = 0

def solve(matrix):
    temp = [row[:] for row in matrix]
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if(temp[i][j] == 0):
                print(i,j)
                makeDigonalZeroes(matrix, i=i, j=j)
            else:
                continue

solve(matrix)
print(matrix)


# def makeDigonalZeroes(row, columns, i, j):
#     row[j] = 0
#     columns[i] = 0

# def makeZeroRows(matrix, j, i, l):
#     for j in range(l):
#         matrix[i][j] =0

# def makeZeroColumns(matrix, l,  i):
#     for i in range(l):
#         matrix[i][j] =0
        

# def solve(matrix):
#     row = []
#     columns = []

#     for i in range(len(matrix[0])):
#         row.append(1)

#     for j in range(len(matrix)):
#         columns.append(1)

#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if(matrix[i][j] == 0):
#                 print(i, j)
#                 makeDigonalZeroes(row, columns, i=i, j=j)
#             else:
#                 continue
    
#     for i in range(len(row)):
#         if(row[i] == 0):
#             makeZeroColumns(matrix, len(row),i)
        

#     print(row, columns)


# solve(matrix)
# print(matrix)
