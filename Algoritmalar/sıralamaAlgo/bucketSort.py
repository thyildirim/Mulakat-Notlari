def bucket_sort(arr):
    if len(arr) == 0:
        return

    bucket_count = 10
    buckets = [[] for _ in range(bucket_count)]

    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val

    for num in arr:
        index = int(((num - min_val) / range_val) * (bucket_count - 1))
        buckets[index].append(num)

    # Her bucket'ı insertion sort ile sırala
    def insertion_sort_bucket(bucket):
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            while j >= 0 and bucket[j] > key:
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = key

    arr.clear()
    for bucket in buckets:
        insertion_sort_bucket(bucket)
        arr.extend(bucket)



if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]

    arr = test_arr.copy()
    bucket_sort(arr)
    print("Bucket Sort:", arr)

