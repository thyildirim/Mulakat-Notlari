# stack_methods.py

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Stack boş mu?"""
        return len(self.items) == 0

    def push(self, item):
        """Eleman ekle (LIFO)"""
        self.items.append(item)

    def pop(self):
        """En üstteki elemanı çıkar ve döndür. Eğer boşsa None döner."""
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """En üstteki elemanı döndür (çıkarmaz). Eğer boşsa None döner."""
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        """Stack'teki eleman sayısı"""
        return len(self.items)

    def clear(self):
        """Stack'i tamamen boşalt"""
        self.items.clear()

    def search(self, item):
        """Elemanın stack'te olup olmadığını kontrol et"""
        return item in self.items

    def __str__(self):
        """Stack'in string gösterimi"""
        return str(self.items)

if __name__ == "__main__":
    s = Stack()

    print("Stack boş mu? ", s.is_empty())
    s.push(10)
    s.push(20)
    s.push(30)
    print("Stack:", s)
    print("En üstteki:", s.peek())
    print("En üstte pop edilen sayı :", s.pop())
    print("En üstte pop edilen sayı ::", s.pop())
    print("Eleman sayısı:", s.size())
    print("20 var mı?:", s.search(20))
    s.clear()
    print("Stack temizlendi:", s)
    print("Stack boş mu? ", s.is_empty())



'''
push(item) → ekleme

pop() → çıkarma

peek() → bakma

is_empty() → boş kontrolü

size() → boyut

clear() → tümünü temizleme

search(item) → arama

__str__() → yazdırma kolaylığı için string dönüşümü

'''