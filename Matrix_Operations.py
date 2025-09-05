# Matrix Operations

def add_matrices(a, b):
    """Add two matrices."""
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def multiply_matrices(a, b):
    """Multiply two matrices."""
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

def transpose_matrix(a):
    """Transpose a matrix."""
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

def print_matrix(matrix):
    """Print a matrix."""
    for row in matrix:
        print(row)

def main():
    """Main function."""
    # Example matrices
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    print("Matrix A:")
    print_matrix(a)
    print("Matrix B:")
    print_matrix(b)

    print("A + B:")
    print_matrix(add_matrices(a, b))

    print("A * B:")
    print_matrix(multiply_matrices(a, b))

    print("Transpose of A:")
    print_matrix(transpose_matrix(a))

if __name__ == "__main__":
    main()