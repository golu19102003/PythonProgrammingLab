def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
numbers = list(map(int, input("Enter numbers separated by spaces for Selection Sort: ").split()))
print("Sorted array (Selection Sort):", selection_sort(numbers))
