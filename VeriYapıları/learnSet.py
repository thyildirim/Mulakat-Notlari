# set_example.py

s = set([1, 2, 3, 2, 4])
print(s)  # {1, 2, 3, 4}

s.add(5)
print(s)

s.remove(3)
print(s)

print(2 in s)  # True
print(10 in s)  # False

# Küme işlemleri
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}
print(a.difference(b))   # {1, 2}
