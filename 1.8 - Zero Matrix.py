import _matrices as matrices
from _utils import print_matrix

# Runtime: O(N * M)
# Memory: O(N + M)
def zero_matrix(matrix):
    rows_to_clear = [False for _ in range(len(matrix))]
    columns_to_clear = [False for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows_to_clear[i] = True
                columns_to_clear[j] = True

    for row, clear in enumerate(rows_to_clear):
        if clear:
            for column in range(len(matrix[0])):
                matrix[row][column] = 0
    for column, clear in enumerate(columns_to_clear):
        if clear:
            for row in range(len(matrix)):
                matrix[row][column] = 0

    return matrix

if __name__ == '__main__':
    print_matrix(zero_matrix(matrices.one_by_one_matrix))
    matrices.one_by_one_matrix[0][0] = 0
    print_matrix(matrices.one_by_one_matrix)

    matrices.unsquare_matrix[2][2] = 0
    matrices.unsquare_matrix[0][2] = 0
    print_matrix(zero_matrix(matrices.unsquare_matrix))
