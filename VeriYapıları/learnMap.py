# map_dict.py

my_map = {"name": "Alice", "age": 25, "city": "Istanbul"}

print(my_map["name"])  # Alice

my_map["age"] = 26     # Güncelleme
my_map["job"] = "Engineer"  # Ekleme
print(my_map)

del my_map["city"]  # Silme
print(my_map)


'''

Dictionary (Python dict kullanımı aynı Map)


d = {}
d["apple"] = 5
d["banana"] = 3

print(d.get("apple"))  # 5
print("banana" in d)   # True

d.pop("apple")
print(d)



'''