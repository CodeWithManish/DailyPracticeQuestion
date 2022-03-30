# sum of matrix

matrix1 = [[1, 2, 3], [4, 3, 2], [2, 4, 1]]
matrix2 = [[2, 4, 1], [2, 1, 3], [4, 3, 2]]

sum = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def sum_of_matrix():
    '''
    :return: sum of matrix
    '''
    for test in range(0, len(matrix1)):
        # print(test)
        for value in range(len(matrix1[0])):
            # print(value)
            sum[test][value] = matrix1[test][value] + matrix2[test][value]

    return sum


if __name__ == '__main__':
    sum_of_matrix()
    print(sum)
