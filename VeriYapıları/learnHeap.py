# heap_example.py
import heapq

heap = []

# Eleman ekle
heapq.heappush(heap, 20)
heapq.heappush(heap, 15)
heapq.heappush(heap, 30)
heapq.heappush(heap, 10)

print("Heap:", heap)  # Min-heap olduğu için en küçük kökte

# En küçük elemanı çıkar
min_elem = heapq.heappop(heap)
print("En küçük eleman:", min_elem)
print("Heap şimdi:", heap)

# En küçük elemana bak (heap[0])
print("Heap'in kök elemanı:", heap[0])

# Heapify - Listeyi heap yap
arr = [5, 3, 8, 1, 2]
heapq.heapify(arr)
print("Heapify edilmiş liste:", arr)
