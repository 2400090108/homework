import sys

def merge_sort(arr, temp, left, right):
    if left >= right:
        return 0
    mid = (left + right) // 2
    inv_count = merge_sort(arr, temp, left, mid) + merge_sort(arr, temp, mid + 1, right)

    i, j, k = left, mid +1, left
    while i <= mid and j <= right:
        if arr[i] > arr[j]:
            arr[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1 ):
        arr[i] = temp[i]

    return inv_count

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
    temp = [0] * n
    result = merge_sort(arr, temp, 0, n - 1)
    print(result)

