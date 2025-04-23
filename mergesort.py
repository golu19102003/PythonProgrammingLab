def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        (result.append(left[i]), i := i+1) if left[i] <= right[j] else (result.append(right[j]), j := j+1)
    return result + left[i:] + right[j:]
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sorted array:", merge_sort(numbers))
