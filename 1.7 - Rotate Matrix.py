
square_matrix =  [[ 1,  2,  3,  4],
                  [ 5,  6,  7,  8],
                  [ 9, 10, 11, 12],
                  [13, 14, 15, 16]]

square_uneven_matrix = [[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]

square_goal =  [[13,  9, 5, 1],
                [14, 10, 6, 2],
                [15, 11, 7, 3],
                [16, 12, 8, 4]]

general_matrix = [[1,  2,  3,  4],
                  [5,  6,  7,  8],
                  [9, 10, 11, 12]]

general_goal = [[9,  5, 1],
                [10, 6, 2],
                [11, 7, 3],
                [12, 8, 4]]

second_goal = [[12, 11, 10, 9],
               [ 8,  7,  5, 6],
               [ 4,  3,  2, 1]]


# Runtime: O(height * width)
# Memory: O(height * width)
def naive_rotate(matrix):
    ret = []
    height, width = len(matrix), len(matrix[0])
    for j in range(width):
        ret.append([matrix[i][j] for i in range(height - 1, -1, -1)])
    return ret

# Must be a square matrix
# Runtime: O(size^2)
# Memory: O(1)
def inplace_rotate(matrix):
    size = len(matrix)
    for i in range(int(size / 2)):
        border = size - i - 1
        for j in range(i, border):
            # Save top
            temp = matrix[i][j]
            # Left to top
            matrix[i][j] = matrix[border + i - j][i]
            # Bottom to left
            matrix[border + i - j][i] = matrix[border][border + i - j]
            # Right to bottom
            matrix[border][border + i - j] = matrix[j][border]
            # Top to right
            matrix[j][border] = temp

    return matrix



def print_matrix(matrix):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))


if __name__ == '__main__':
    print('NAIVE SQUARE MATRIX')
    print_matrix(naive_rotate(square_matrix))
    print('\nNAIVE GENERAL MATRIX')
    print_matrix(naive_rotate(general_matrix))
    print('\nNAIVE GENERAL TWO TIMES')
    print_matrix(naive_rotate(naive_rotate(general_matrix)))
    print('INPLACE SQUARE MATRIX')
    print('EMPTY')
    print_matrix(inplace_rotate([[]]))
    print('1X1')
    print_matrix(inplace_rotate([[1]]))
    print('3X3')
    print_matrix(inplace_rotate(square_uneven_matrix))
    print('4X4')
    print_matrix(inplace_rotate(square_matrix))
