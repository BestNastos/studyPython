from datetime import date

from study.CoffeeShop import CoffeeShop

print("1. String formatting")
name = 'Chris'

# 1. f strings
print(f'Hello {name}')

# 2. % operator
print('Hey %s %s' % (name, name))

# 3. format
print(
    "My name is {}".format((name))
)

print("2. Is vs ==")
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == c) #true
print(a is c) #false
print(id(a)) #1649342035584
print(id(b)) #1649342035584
print(id(c)) #1649342035328

print("3. Decorator")

def logging(func):
 def log_function_called():
   print(f'{func} called.')
   func()
 return log_function_called

@logging
def my_name():
 print('chris')

@logging
def friends_name():
 print('anna')

my_name()
friends_name()

print("5. Self, static, class methods")
CoffeeShop.check_weather()
coffee_shop = CoffeeShop('1')
coffee_shop_1 = CoffeeShop('2')

coffee_shop_1.change_coffee()
coffee_shop_1.change_specialty('drip coffee')
coffee_shop_2 = CoffeeShop('3')

print(coffee_shop.make_coffee())
print(coffee_shop_1.make_coffee())
print(coffee_shop_2.make_coffee())

print("6. Map function")
# возвращает объект (итератор), который перебирает значения, применяя функцию к каждому элементу.
def add_three(x):
    return x + 3
li = [1,2,3]
print(list(map(add_three, li)))
print(list(map(lambda i, j : i + j, [1,2,3], [5,6,7]))) #[6, 8, 10]

print("7. Reduce function")
# На каждой итерации в функцию передаются как текущий элемент, так и вЫходные данные предыдущего элемента
from functools import reduce
def add_three(x,y):
    return x + y
li = [0,1,2,3]
print(reduce(add_three, li))#6
print(reduce(lambda i,j : i+j, range(7))) # 0 1 2 3 4 5 6 -> 21

print("8. Filter function")
def add_three(x):
    if x % 2 == 0:
        return True
    else:
        return False

li = [1,2,3,4,5,6,7,8]
print([i for i in filter(add_three, li)]) #[2, 4, 6, 8]
print([i for i in filter(lambda j : j > 5, li)]) #[6, 7, 8]

print("9. Reverse list")

li = ['a','b','c']
print(li)
li.reverse()
print(li)
#=> ['a', 'b', 'c']
#=> ['c', 'b', 'a']

print("10. Deep copy")
import copy

li5 = [['a'],['b'],['c']]
li6 = copy.deepcopy(li5)

li5.append([4])
li5[0][0] = 'X'
print(li6 , li5)
#=> [['a'], ['b'], ['c']]

print("11. Round function")
a = 5.12345
print(round(a,3))
#=> 5.123

print("12. Split the list")
a = [0,1,2,3,4,5,6,7,8,9]
print(a[:2])
#=> [0, 1]

print(a[8:])
#=> [8, 9]

print(a[2:8])
#=> [2, 3, 4, 5, 6, 7]

print(a[2:8:2])
#=> [2, 4, 6]

print("13. Two lists in one tuple")

a = ['a','b','c']
b = [1,2,3,4]

print([(k,v) for k,v in zip(a,b)])
#=> [('a', 1), ('b', 2), ('c', 3)]
print(list(zip(a,b)))

print("14. Combine lists")
print(a+b)
print([i for i in list(a+b)])

print("15. Sort dict")
dicti = {"name" : "London", "population" : "8000000", "country": "uk"}

print(sorted(dicti)) # sorts keys and returns list of sorted keys
print(sorted(dicti.items())) # sorts entries and returns them as tuples
print(list(dicti)) # returns list of keys

print("16. Inheritance")
class Car():
    def drive(self):
        print('vroom')
class Audi(Car):
    pass
audi = Audi()
audi.drive()

print("17. String split / replace / join")
s = 'A string with white space'
print(s.replace(' ', ''))
print(s.split())
print('.'.join(s.split()))  #A.string.with.white.space

print("18. Function enumerate()")
# lets you write Pythonic for loops when you need a count and the value from an iterable.
# The big advantage of enumerate() is that it returns a tuple with the counter and value,
# so you don't have to increment the counter yourself.
li = ['a','b','c','d','e']
for idx,val in enumerate(li):
    print(idx, val)
#=> 0 a
#=> 1 b
#=> 2 c
#=> 3 d
#=> 4 e

print("19. Comprehensions")
a = []
a1 = [i + 3 for i in range(5)]
print(a1) #=> [3, 4, 5, 6, 7]
for index, value in enumerate(a1):
    a.append(value)
    a.append(index)
print(a) #[3, 0, 4, 1, 5, 2, 6, 3, 7, 4]

print('turning code block into list comprehension:')
a = [1, 2, 3, 4, 5]
a2 = []
for i in a:
    a2.append(i + 1)
print(a2) # => [2, 3, 4, 5, 6]

print('result:')
print([i + 1 for i in a])

d = {num: num**2 for num in range(1, 11)}
print(d) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

vlans = [10, '30', 30, 10, '56']
unique_vlans = {int(vlan) for vlan in vlans}
print(unique_vlans) #{56, 10, 30}

print("20. If / else")
x = 5
print('greater' if x > 6 else 'less')

print("21. Function isnumeric() and isalnum()")
'123a'.isnumeric() #=> False
'123abc'.isalnum() #=> True

print("22. Remove/ del / pop")
li = ['a','b','c','d']
li.remove('b') #удаляет первое совпадающее значение
del li[0] #удаляет элемент по его индексу
li.pop(1) #удаляет элемент по индексу и возвращает этот элемент
print(li)

print("23. Exceptions")
# try:
#     a = input("Введите первое число: ")
#     b = input("Введите второе число: ")
#     print("Результат: ", int(a)/int(b))
# except ValueError:
#     print("Пожалуйста, вводите только числа")
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
#
# try:
#     a = input("Введите первое число: ")
#     b = input("Введите второе число: ")
#     result = int(a)/int(b)
# except (ValueError, ZeroDivisionError):
#     print("Что-то пошло не так...")
# else:
#     print("Результат в квадрате: ", result**2) #в отличие от finally выполнится только если не было ошибки

print("24. Any() and All(), bools")
a = [False, False, False]
b = [True, False, False]
c = [True, True, True]
d = "true"
print(bool(d)) # converts to bool
print(bool(0)) # converts to bool - false
print(bool([])) # converts to bool - false - empty list
print( any(a) )
print( all(b) )
print( any(c) )

if "a":
    print("if")
else:
    print("else")

print("25. Exception ValueError")
try:
    print(int("try"))
except ValueError:
    print("except")
finally:
    print("finally")

print("26. Loops For and While")
a = 5
while a > 0:
    a -= 1
    print(a)
else:
    print("test else")

for x in 'Hello':
    if x == 'l':
        print('YES')    # печатаем YES и выходим из цикла
        break
else:
    print('NO') # если дошли до break то else не печатается, else принадлежит циклу for а не if-y


print("27. Test pass by link or value")
name = 5
def add_chars(str1):
    print(id(str1))  # => 4353702856
    print(id(name))  # => 4353702856
    # новое имя, тот же объект
    str2 = str1
    # создаем новое имя (не отличается от предыдущего) и новый объект
    str1 += 1
    print(id(str1))  # => 4387143328
    # объект не изменился
    print(id(str2))  # => 4353702856

add_chars(name)
print(name)  # =>5

print("28. Cast in to str")
str(5)

print("29. O(n) iterator")
li = [11,22,15,47,563,0] # 	O(n)
if 11 in li:
    print("yes")

print("30. Arrays")
import array as arr
numbers= arr.array('i', [10, 20, 30]) # сюда можно класть только указанный тип: в данном случае - i - int
print(numbers)

print("31. Kwargs")
def func_name(a,b,c=True,**d):
    print(a)
    print(b)
    print(c)
    print(d)

func_name(1,1, c=False, k=100, n="f")

print("32. Parametric polymorphism")
print(int(22).__add__(5)) #  same as 22 + 5

print("33. Duck typing")

class Duck:
    def fly(self):
        print("duck is flying")

class Swan:
    def fly(self):
        print("swan is flying")

birds = [Duck(), Swan()]
for bird in birds:
    bird.fly()

# output:
# duck is flying
# swan is flying

print("34. __getitem__")

class CustomContainer:
    def __init__(self, list):
        self._list = list

    def __getitem__(self, item):
        element = self._list[item]
        return str(element)

my_container = CustomContainer([1,'2', 3, 4, 5])
print(my_container[2]) # 3

print("35. classmethod")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, bYear) :
        return cls(name, date.today().year - bYear)
        #same as return Person(name, date.today().year - bYear) in non classmethod
        #better to use classmethod because this way you don't need an instance to call this method

    def __str__(self):
        return self.name + " " + str(self.age)

person = Person("Adam", 19)
print(person)
person1 = Person.fromBirthYear("Anna", 1985)
print(person1)

print("35. Problem solving (Hackerrank")
def func(n):
    if n % 2 == 1:
        print("Weird")
    else:
        if 2 <=  n <= 5: print("Not Weird")
        if 6 <=  n <= 20: print("Weird")
        if n > 20: print("Not Weird")

func(20)


# set_len = input("set len - ")
# print(set_len)
# values = input("values - ")
# print(values)
# com_num = int(input("com_num - "))
# print(com_num)
#
# set_val = {int(i) for i in values.split()}
#
# while(com_num > 0):
#     command = input("command " + str(com_num) + " - ")
#     if "pop" in command:
#         set_val.pop()
#     elif "discard" in command:
#         val = int(command.split()[1])
#         set_val.discard(val)
#     elif "remove" in command:
#         val = int(command.split()[1])
#         if val in set_val: set_val.remove(val)
#     com_num = com_num - 1
#     print(set_val)
#
# summa = 0
# for i in set_val:
#     summa = summa + int(i)
#
# print(summa)


# n = int(input("n - "))
# s = set(map(int, input("s - ").split()))
# m = int(input("m - "))
# for i in range(m):
#     attr, *kw = input(" command " + str(i) + " - ").split() + [""]
#     if kw[0]:
#         getattr(s, attr)(int(kw[0]))
#     else:
#         getattr(s, attr)()
# print(sum(s))

n = int(input("g"))
s = set(map(int, input("g").split()))
for i in range(int(input("g"))):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))