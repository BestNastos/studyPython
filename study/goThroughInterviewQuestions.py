from array import array
from functools import reduce

name = "Alice"

s = "My name is {}".format(name)
print(s)
s = "My name is %s" % name
print(s)
s = f"My name is {name}"
print(s)

# -----


def decorator(func):
    def wrap_logic():
        print("added logic")
        func()
    return wrap_logic


@decorator
def for_decorator():
    print("main logic for wrapping")


for_decorator()


# -----

class Car:

    class_value = "default_class_value"

    def __init__(self, color, speed, brand=None):
        self.color = color
        self.speed = speed
        self.brand = brand

    def instance_method_set_brand(self, brand):
        self.brand = brand

    @staticmethod
    def static_method(a, b):
        return a + b

    @classmethod
    def class_method_set_class_val(cls, class_val):
        cls.class_value = class_val

    def instance_method_set_class_val(self, class_val):
        self.class_value = class_val


car = Car("red", 60)
print(car.speed)
car.instance_method_set_class_val("instance_method_set_class_val")
print(car.class_value)
car.class_method_set_class_val("class_method_set_class_val")
print(car.class_value)
print(Car("green", 40).class_value)

class Audi(Car):

    def __init__(self, color, speed, brand=None):
        super().__init__(color, speed, brand)


    def instance_method_set_brand(self, brand):
        self.brand = brand + "_audi"

audi = Audi("color", 80)
audi.instance_method_set_brand("brand")
print(audi.brand)
# -----

li = [1, 5, 9]
print(list(map(lambda i: 1 + i, li)))

def add_one(i):
    return i + 1
print(list(map(add_one, li)))


def reduc(i , j):
    return i + j

print(reduce(reduc, li))
print(reduce(lambda i, j: i + j, li))

def filt(i):
    return i > 1

print(list(filter(filt, li)))
print(list(filter(lambda i : i > 1, li)))

s = "test string"
li = s.split()
li.reverse()
print(" ".join(li))

a = array("i", [4,5])
a.append(8)
print(a)

print(round(3.00456, 4))

li = [5,89,4,504,45,8,8,8,9]
print(li[:2])
print(li[::2])

li1 = ["", 0]
li2 = [4, "la"]
print(any(li1))
print(any(li2))
print(all(li1))
print(all(li2))

print(set(li))

s = " test again"
print("0" in s)

li.append([1,5])
print(li)
li.extend([4,5])
print(li)

map = {"d": 5, "a": 4, "c" : 9}
print(sorted(list(map))) #print(list(map.keys()))
print(sorted(map.items()))


# s = s.replace(" ", "")
# print(s)
s = s.split()
s  = "".join(s)
print(s)

for i, v in enumerate(s):
    print(i, v)

print([i + 1 for i in [5,6,8,9]])

n = -7
print("greater" if n > 0 else "smaller")

print("1234".isnumeric())
print("1234f".isalnum())
print("1234".isalpha())

print({k : k + 1 for k in [1,5,9]})

try:
    raise ZeroDivisionError
except ZeroDivisionError as err:
    print("the error was caught")
else:
    print("else statement")
finally:
    print("finally statement")

class Test:
    message = "message"

t = Test
print(t.message)

li = [0,1,2,3,4,5]
print(li[6:2])

li[0] = 10
print(li)
li.insert(2, 11)
print(li)

def method(a):
    while(a % 2 == 0):
        a /= 2
    return a == 1

print(method(32))

li = [ '1', 2, 'a', 'b', 'c', -1, True, 13.33, None, 41]

def method1(li):
    print(list(filter(lambda i: isinstance(i, int) and i > 0, li)))

method1(li)


def method2(s):
    for i in s:
        if i != "t":
            print(i, end="")
        else:
            break

method2("i love python")

def method3(s):
    # for i in s:
    #     if i == " ":
    #         continue
    #     else:
    #         print(i, end = "")

    print(s.replace(" ", ""))

method3("i love python")

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print(list1, list2)

class ConManager:

    def __enter__(self):
        print("string in __enter__")
        return [1]

    def __exit__(self, exception, value, trace):
        print("string in __exit__")
        # return [1]

with ConManager() as cm:
    print('print')