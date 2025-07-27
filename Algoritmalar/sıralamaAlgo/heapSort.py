def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    # Max heap oluştur
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Elemanları sırayla al ve heap'i tekrar düzenle
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]

    arr = test_arr.copy()
    heap_sort(arr)
    print("Heap Sort:", arr)

