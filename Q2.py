def product(M, N):
    # row M x col N
    result_matrix = [[0]*len(M[0]) for _ in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            for k in range(len(M[0])):
                result_matrix[i][j] += M[i][k] * N[k][j]
    return result_matrix

def multiply_k(X, k):
    for i in range(len(X)):
        for j in range(len(X[0])):
            X[i][j] *= k
    return X

def sum_matrix(A, B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] += B[i][j]
    return A

def matrix_to_power_of_n(X, n):
    result = [[0]*len(X[0]) for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j]
    for i in range(2, n+1):
        result = product(result, X)
    return result


if __name__ == "__main__":
    # 1
    test_cases = [([[1,2], [3,4]], [[3,4], [5,6]]),
                  ([[123,212], [23,42]], [[23,34], [65,62]])]
    # result:
    #     test case 1: [[13, 16], [29, 36]]
    #     test case 2: [[16609, 17326], [3259, 3386]]
    for M, N in test_cases:
        print(product(M, N))

    #2
    n = int(input("Enter n: "))
    A = [[5, 3], [2, -1]]
    B = [[2, -3], [5, 4]]
    Xn = matrix_to_power_of_n(sum_matrix([[5, 3], [2, -1]], multiply_k([[2, -3], [5, 4]], -(11)**0.5)), n)
    # a + b sqrt(11) = x
    print("Xn matrix: ")
    for row in Xn:
        print(row)
    initial_X = [[(5,2) , (3, -3)], [(2, 5), (-1, 4)]]
    X = [[(5,2) , (3, -3)], [(2, 5), (-1, 4)]]
    for _ in range(2, n+1):
        new_X = [[(5,2) , (3, -3)], [(2, -1), (-1, 4)]]
        for i in range(len(A)):
            for j in range(len(A[0])):
                result_1 = 0
                result_2 = 0
                for k in range(len(A[0])):
                    a = X[i][k][0]
                    b = X[i][k][1]
                    c = initial_X[k][j][0]
                    d = initial_X[k][j][1]
                    result_1 += a * c + b * d * 11
                    result_2 += -a * d - b*c
                new_X[i][j] = (result_1, result_2)
        X = new_X
    An = []
    for i in range(2):
        row = []
        for j in range(2):
            row.append(X[i][j][0])
        An.append(row)
    Bn = []
    for i in range(2):
        row = []
        for j in range(2):
            row.append(X[i][j][1])
        Bn.append(row)
    print("Result: ")
    print("An : ")
    for row in An:
        print(row)
    print("Bn: ")
    for row in Bn:
        print(row)
