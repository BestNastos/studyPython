class Parent:

    def __init__(self):
        print("Parent __init__")

class A:
    def __init__(self):
        print("A __init__")

class Child1(Parent):

    def __init__(self):
        print("Child1 __init__")
        super().__init__()


class Child2(Parent):

    def __init__(self):
        print("Child2 __init__")
        super().__init__()


class IncestChild(Child1, Child2):

    def __init__(self):
        print("IncestChild __init__")
        super().__init__()


i_child = IncestChild()

# output:
# IncestChild __init__
# Child1 __init__
# Child2 __init__
# Parent __init__

# а если бы не было наследования от одного родителя то инициализация бы пошла только по линии Child1:
# IncestChild __init__
# Child1 __init__
# Parent __init__

IncestChild.mro() #Method Resolution Order - показывает порядок вызова методов

print(isinstance(i_child, Parent)) # true
print(type(i_child) is Parent) #False
print(type(i_child) is IncestChild) #true
print(issubclass(IncestChild, Parent)) #True