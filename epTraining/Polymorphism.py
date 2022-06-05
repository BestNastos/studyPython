class A:

    def sum(self, a):
        print(a)

    def sum(self, a, b):
        print(a + b)


# not going to work because second sum method overrides the first one:
# A().sum(2)
# -> TypeError: A.sum() missing 1 required positional argument: 'b'

class Duck:

    def fly(self):
        print("Duck fly")


class Airplane:

    def fly(self):
        print("Airplane fly")

class Ship:

    def swim(self):
        print("Ship swim")

def go(entity):
    entity.fly()

list = [Duck(), Airplane(), Ship()]

# for i in list:
#     i.fly()

#output:
# Duck fly
# Airplane fly
# AttributeError: 'Ship' object has no attribute 'fly'

ship1 = Ship()
ship2 = Ship()
print(ship2.__eq__(ship1)) # вызываем метод отнаследованный у object но не имплементированный, вывод: NotImplemented

print(dir(object()))