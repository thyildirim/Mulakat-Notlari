def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    
    arr = test_arr.copy()
    bubble_sort(arr)
    print("Bubble Sort:", arr)