a = {"name": "Anastasia"}
b = a
c = {"name": "Anastasia"}
print(a is b) #true
print(a is c) #false
print(a == b) #true
print(a == c) #true

set_1 = {"name", "Anastasia"}
print("name" in set_1) #true

print(False == 1)#true
print({1,1,3,4} == {4,3, 1})#true

a = 5
b = 9
print(a, b)
a, b = b, a
print(a, b)

a, b, c = 3, 4, 5
print(a, b, c)
a = b = c = 3
print(a, b, c)

# with open('newfile.txt', 'w', encoding='utf-8') as data: # with это как try с ресурсами, он закрывает ресурс
#     s = int(input())#e.g. 6
#     print('1 / {} = {}'.format(s, 1 / s), file=data) #создается файл, туда пишется 1 / 6 = 0.16666666666666666

print("hello" == "hello" )#true
print("hello" is "hello" )#true
a = "hello"
b = "hello"
print(a is b)#true
print({1,2} == {2,1} )#true
print((1,2) == (1,2) )#true
print([1,2] == [1,2] )#true