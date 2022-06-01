a = {"name": "Anastasia", "eyes": "brown"}
print(sorted(a))#['eyes', 'name']
print(sorted(a.items()))#[('eyes', 'brown'), ('name', 'Anastasia')]
print(list(a.keys())) #['name', 'eyes']
print(list(a))#['name', 'eyes']
print(set(a))#{'name', 'eyes'} порядок не гарантирован
print(a.keys())#dict_keys(['name', 'eyes'])
print(a.values())#dict_values(['Anastasia', 'brown'])
b = a.values() #b is object "dict_values"

print({num: num *2 for num in range(5)}) #{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

a["last name"] = "Ermushina"
print(a)

b = a.copy()
a["name"] = "Anna"
print(id(a), id(b))
print(a)
print(b)
c = b;
del c["name"]
print(a)
print(b)
print(c)



