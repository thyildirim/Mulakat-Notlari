def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Her elemanın sayısını tut
    for num in arr:
        count[num - min_val] += 1

    # Kümülatif sayılar
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Çıktıyı oluştur
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]

    arr = test_arr.copy()
    counting_sort(arr)
    print("Counting Sort:", arr)
