def matrix_add(X,Y):
    result = [[X[i][j] + Y[i][j] for j in range
           (len(X[0]))] for i in range(len(X))]

    for r in result:
        print(r)
    
def matrix_transpose(m):
    print("Normal Matrix: \n")
    for row in m:
	    print(row)
    result = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    print("\n")
    print("Transposed Matrix: \n")
    for row in result:
        print(row)

def matrix_multiplication(X,Y):
    # result will be 3x4
    result = [[sum(a * b for a, b in zip(X_row, Y_col)) 
                            for Y_col in zip(*Y)]
                                    for X_row in X]

    for r in result:
        print(r)

X = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

Y = [[5, 8, 1],
    [6, 7, 3],
    [4, 5, 9]]

matrix_add(X,Y)
print("\n")
matrix_multiplication(X,Y)
print("\n")
matrix_transpose(Y)
print("\n")