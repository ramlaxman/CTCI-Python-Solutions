import _matrices as matrices
from _utils import print_matrix


def zero_row(row, matrix):
    for column in range(len(matrix[0])):
        matrix[row][column] = 0

def zero_column(column, matrix):
    for row in range(len(matrix)):
        matrix[row][column] = 0

# Runtime: O(N * M)
# Memory: O(1)
def zero_matrix(matrix):

    first_column_has_zero = False
    first_row_has_zero = False
    for row in range(len(matrix)):
        if matrix[row][0] == 0:
            first_column_has_zero = True
    for column in range(len(matrix[0])):
        if matrix[0][column] == 0:
            first_row_has_zero = True

    # Leave the first row/column for the end
    # so it can be used to store the columns/rows to zero
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Empty the rows
    for row in range(1, len(matrix)):
        if matrix[row][0] == 0:
            zero_row(row, matrix)

    # Empty the columns
    for column in range(1, len(matrix[0])):
        if matrix[0][column] == 0:
            zero_column(column, matrix)

    if first_column_has_zero:
        zero_column(0, matrix)
    if first_row_has_zero:
        zero_row(0, matrix)

    return matrix

if __name__ == '__main__':
    print_matrix(zero_matrix(matrices.one_by_one_matrix))
    matrices.one_by_one_matrix[0][0] = 0
    print_matrix(matrices.one_by_one_matrix)

    matrices.unsquare_matrix[2][2] = 0
    matrices.unsquare_matrix[0][2] = 0
    matrices.unsquare_matrix[0][0] = 0
    print_matrix(zero_matrix(matrices.unsquare_matrix))
