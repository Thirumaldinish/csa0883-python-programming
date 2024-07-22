def matrix_multiplication(A, B):
    """Function to perform matrix multiplication."""
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Input matrices
A = [[2, 1], [3, 4]]
B = [[31, 1], [1, 2]]

# Perform matrix multiplication
result = matrix_multiplication(A, B)

# Print the result
print("Result of matrix multiplication:")
for row in result:
    print(row)
