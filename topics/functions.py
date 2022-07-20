print("1) map")
li = ["my", "name"]


def multiply(a):
    return a * 2


print(list(map(multiply, li)))  # ['mymy', 'namename']
print(list(map(lambda i, j : i + j, [1,2,3], [5,6,7]))) # [6, 8, 10]

print("2) reduce")
from functools import reduce

li = [1, 2, 3, 4]


def multiply(a, b):
    return a * b


print(reduce(multiply, li))  # returns int 24

print("3) filter")


def is_odd(a):
    if a % 2 == 0:
        return False
    else:
        return True


print(list(filter(is_odd, li)))
print(list(filter(lambda a: a % 2 != 0, li)))

print("4) all() and any()")
boo_li = "True", "False"
boo_li_1 = "True", "True"
print(any(boo_li))
print(all(boo_li))

print("5) bin() / abs()")
print(bin(3))  # 0b11
print(abs(-3))  # 3

print("6) recursion")


def fib(n):  # 0, 1, 1, 2, 3, 5, 8, 13, 21
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(8))  # 21

print("7) zip()")
print(list(zip({1, 2, 3}, {5, 6, 7})))  # works with any collections: [(1, 5), (2, 6), (3, 7)]
print(list(zip("ooo", "aaa")))  # without casting prints object address [('o', 'a'), ('o', 'a'), ('o', 'a')]

a = ['a', 'b', 'c', 'd']
b = [4, 1, 2, 3]
print(list(zip(a, b)))  # [('a', 1), ('b', 2), ('c', 3)]
print([(k, v + 1) for k, v in zip(a, b)])  # [('a', 2), ('b', 3), ('c', 4)]

print(sorted(b))

print("8) pyramid")
s = ""
for i in range(6):
    print(s + "*")
    s += "*"


# *
# **
# ***
# ****
# *****
# ******

def pyramid_upside_down(n):
    print("*" * n)
    n -= 1
    if n > 0:
        pyramid_upside_down(n)


pyramid_upside_down(5)


def pyramid(n):
    s = ""
    for i in range(n + 1):
        print(s + "*")
        s += "*"


pyramid(5)

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i: i * i for i in A1}
A6 = [[i, i * i] for i in A1]
print(A0, A1, A2, A3, A4, A5, A6)

print("9) I/O")
# count capitals:
with open("text.txt", "w") as file:
    print("Test Sentence", file=file)
count = 0
with open("text.txt", "r") as text:
    for i in text.read():
        if i.isupper():
            count += 1
print(count)
with open("text.txt", "r") as file:
    print(file.read())

print("10) lambda")
print((lambda a, b: a if a > b else b)(3, 3.5))  # 3.5

print("11) generator (yield)")


def generate(n):
    while n > 0:
        yield n * 2
        n -= 2


print([i for i in generate(5)])

print(type(3))  # <class 'int'>
print(type)  # <class 'type'>
isinstance((1), tuple)  # False

print("12) Boxing/unboxing?")


def handle_info(name, age, gender, friends):
    print(name, age, gender, friends)


person_info = ("Bob", 27)
person_additional_info = {"gender": "male", "friends": ("Kate",)}

handle_info(*person_info, **person_additional_info)  # Bob 27 male ('Kate',)
handle_info('Bob', 27, gender='male', friends=('Kate,')) #Bob 27 male Kate,

print("13) any() vs all()")
a = [8, "test"]
b = [False, 0, ""]
print(any(a))  # True
print(any(b))  # False
print(all(a))  # True
print(all(b))  # False


