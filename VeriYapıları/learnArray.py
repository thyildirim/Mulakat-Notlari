
# Python'da list dinamik array olarak kullanılır
arr = [1, 5,3,2,4,7,8,6,9,11,10,33,22]

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
print("0. indexten 3. indexe kadar" , arr[0:4])  # [3, 4, 5] (örnek: 1. indexten 3. indexe kadar)

print("------------------------------")
arr.insert(2, 10)  # 2. indexe 10 ekle
print("2. indexe 10 eklenmiş hali" , arr)

print("------------------------------")
arr.sort()  
print("Sıralı hali " , arr)

print("------------------------------")
# Eleman sayısı
print("Eleman sayısı", len(arr))  # 7