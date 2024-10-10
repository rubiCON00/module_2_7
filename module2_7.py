def get_matrix(n, m,  value):
    matrix =[]
    for i  in range(n):
        matrix.append([])
        for k in range(m):
            matrix[i].append(value)
    print(matrix)
    return (matrix)
n = (5)
m = (6)
value = (7)
matrix = get_matrix(n,m,value)




