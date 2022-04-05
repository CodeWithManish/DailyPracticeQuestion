"""
Given an array of integer, find the maximum sumo in a contiguous element, sub_array
"""


def maximum_sum_of_sub_array(arr):
    max_sum = arr[0]
    sub_arr_sum = 0
    for element in arr:
        sub_arr_sum += element
        if max_sum < sub_arr_sum:
            max_sum = sub_arr_sum
        if sub_arr_sum < 0:
            sub_arr_sum = 0
    return max_sum


if __name__ == '__main__':
    arr = [1, 2, -4, 1, 2, 3, -9]
    res = maximum_sum_of_sub_array(arr)
    print(res)
