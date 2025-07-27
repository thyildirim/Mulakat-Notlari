def linear_search(arr, target):
    """
    Bir dizide target elemanını doğrusal olarak arar.
    Bulursa index'ini döner, bulamazsa -1 döner.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # hedef bulundu
    return -1  # hedef bulunamadı


arr = [4, 2, 7, 9, 1, 5]
target = 1
target2 = 0
result = linear_search(arr, target)
result2 = linear_search(arr, target2)


print("Eğer dizide varsa Indexi döner !!, Yoksa -1 döner")
if result == -1 :
    print(f"Sonuç: {result}, BULUNAMADI")  
else:
    print(f"Sonuç: {result}. indexde target bulundu") # İNDEX DEĞERİ DÖNDÜ

if result2 == -1 :
    print(f"Sonuç: {result2}, BULUNAMADI")  
else:
    print(f"Sonuç: {result2}. indexde target bulundu") # İNDEX DEĞERİ DÖNDÜ




'''
En iyi durum (best case): O(1) → aranan ilk sıradaysa

Ortalama durum (average): O(n)

En kötü durum (worst case): O(n) → son elemanda ya da hiç yoksa'''