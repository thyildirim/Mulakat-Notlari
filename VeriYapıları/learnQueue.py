# queue_methods.py

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Queue boş mu?"""
        return len(self.items) == 0

    def enqueue(self, item):
        """Queue'nun sonuna eleman ekle (FIFO)"""
        self.items.append(item)

    def dequeue(self):
        """Queue'nun önünden eleman çıkar ve döndür. Boşsa None döner."""
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        """Öndeki elemanı döndür (çıkarmaz). Boşsa None döner."""
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        """Queue'daki eleman sayısı"""
        return len(self.items)

    def clear(self):
        """Queue'yu tamamen boşalt"""
        self.items.clear()

    def search(self, item):
        """Elemanın queue'da olup olmadığını kontrol et"""
        return item in self.items

    def __str__(self):
        """Queue'nun string gösterimi"""
        return str(self.items)

if __name__ == "__main__":
    q = Queue()

    print("Queue boş mu? ", q.is_empty())
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    print("Queue:", q)
    print("Öndeki eleman:", q.peek())
    print("Dequeue:", q.dequeue())
    print("Dequeue:", q.dequeue())
    print("Eleman sayısı:", q.size())
    print("'b' var mı?:", q.search('b'))
    q.clear()
    print("Queue temizlendi:", q)
    print("Queue boş mu? ", q.is_empty())


'''
enqueue(item) → ekleme (sona)

dequeue() → çıkarma (baştan)

peek() → baştaki elemana bakma

is_empty() → boş kontrolü

size() → eleman sayısı

clear() → temizleme

search(item) → arama

__str__() → yazdırma için kolay dönüşüm

'''