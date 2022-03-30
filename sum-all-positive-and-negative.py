# sum of all positive and negative numbers separately from 1 array


def _sum(arr):
    positive_num = 0
    negative_num = 0
    for num in arr:
        if num > 0:
            positive_num = positive_num + num
        if num < 0:
            negative_num = negative_num + num

    return positive_num, negative_num


if __name__ == '__main__':
    array = [1, 2, -4, -1]
    print(array)
    print("sum of positive_num and negative_sum", _sum(array))
