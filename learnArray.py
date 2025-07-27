
# Python'da list dinamik array olarak kullanılır
arr = [1, 2, 3, 4, 5]

# Erişim (index ile O(1))
print(arr[2])  # 3

# Arama (O(n))
print(3 in arr)  # True

# Ekleme (sona, amortize O(1))
arr.append(6)
print(arr)

# Silme (O(n))
arr.remove(2)
print(arr)

print("------------------------------")
for i in arr:
    print(i)

print("------------------------------")
print(arr[0:4])  # [3, 4, 5] (örnek: 1. indexten 3. indexe kadar)

print("------------------------------")
arr.insert(2, 10)  # 2. indexe 10 ekle
print(arr)
