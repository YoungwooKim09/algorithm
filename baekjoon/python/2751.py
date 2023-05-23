import sys

sys.stdin = open('input.txt', 'r')

var = list(map(int, sys.stdin.read().splitlines()))

var.remove(var[0])

def merge_sort(arr) :
    if len(arr) < 2 :
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(left_arr) and h < len(right_arr) :
        if left_arr[l] < right_arr[h] :
            merged_arr.append(left_arr[l])
            l = l + 1
        else :
            merged_arr.append(right_arr[h])
            h = h + 1

    merged_arr = merged_arr + left_arr[l:]
    merged_arr = merged_arr + right_arr[h:]

    return merged_arr

print(*merge_sort(var), sep='\n')