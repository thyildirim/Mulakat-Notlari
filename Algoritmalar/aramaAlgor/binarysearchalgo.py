def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1



def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)



arr = [1, 3, 5, 7, 9, 11, 13]
target = 9

# İteratif
print(binary_search_iterative(arr, target))  # Output: 4

# Rekürsif
print(binary_search_recursive(arr, target, 0, len(arr)-1))  # Output: 4



'''
Binary Search Notasyonları (Sıralı dizide çalışır):

    En İyi Durum (Best Case):
    O(1) → Aranan eleman tam ortadaysa, tek adımda bulunur.

    Ortalama Durum (Average Case):
    O(log n) → Dizi her seferinde ikiye bölünür, bu yüzden logaritmik.

    En Kötü Durum (Worst Case):
    O(log n) → Aranan eleman en sonda ya da yoksa, tüm log(n) bölmeler denenir.


🧠 Neden O(log n)?

    Her adımda arama alanı yarıya indirilir.

    Bu, 1 milyonluk bir dizide bile sadece ~20 adımda sonuca ulaşılmasını sağlar.

📝 Koşullar

    Dizi önceden sıralı olmalı.

    İkili bölme işlemi uygulanabilir olmalı.
'''
























'''
Özellik	                    İteratif	                    Rekürsif
Kullanım	                Döngülerle	                  Fonksiyonun kendini çağırması
Bellek Kullanımı	        Düşük (O(1))	                Yüksek (O(log n))
Performans	               Genellikle daha hızlı	        Daha yavaş olabilir
Kod Uzunluğu	            Daha uzun olabilir	            Daha kısa ve okunabilir
Örnek Kullanım	Binary Search, Bubble Sort	                    DFS, Merge Sort, Factorial



✅ Ne Zaman Hangisi?

    Basit ve büyük veri üzerinde çalışacaksan:
    → İteratif

    Ağaçlar, graf yapıları, böl ve fethet (divide and conquer) gibi yapılarla çalışıyorsan:
    → Rekürsif



'''