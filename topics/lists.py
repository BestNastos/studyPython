li = [i + 1 for i in range(2, 8, 3) if i > 0]
print(li) # [3, 6]

li.reverse()
print(li) # [6, 3]

print(li*2) # [6, 3, 6, 3]

li_1 = [1, 1]
print(li + li_1) # [6, 3, 1, 1]

li.append(li_1) # добавляет в качестве элемента
print(li) # [6, 3, [1, 1]]

li.extend(li_1) # расширяет список
print(li) # [6, 3, [1, 1], 1, 1]

# import numpy as np
#
# a = np.array([1,2,3])
# b = np.array([4,5,6])
#
# np.concatenate((a,b))

li = [1, 2, 5, 7, 10]
print(li[:2]) # [1, 2]
print(li[1:]) # [2, 5, 7, 10]
print(li[3:4]) # [7]

li = [1, 1, 5, 7, 10]
print(list(set(li))) # [1, 10, 5, 7]

li_1 = [55, 55, 55, 55, 55]
print(list(zip(li, li_1))) # [(1, 55), (1, 55), (5, 55), (7, 55), (10, 55)]
print([(k + 1, v) for k, v in zip(li, li_1)]) # [(2, 55), (2, 55), (6, 55), (8, 55), (11, 55)]


for index, value in enumerate(li):
    print(index, " ", value)

print([(i+1, v) for i, v in enumerate(li)]) #[(1, 1), (2, 1), (3, 5), (4, 7), (5, 10)]

print(list([2,3]))#[2, 3]
print(list("name"))#['n', 'a', 'm', 'e']

print(li.index(10))#возвращает индекс элемента 4

li = [2, 1, 5, 7, 10]
li.insert(1, 45)#[2, 45, 1, 5, 7, 10]
print(li)

li.sort()
print(li)#[1, 2, 5, 7, 10, 45]

li = ["2", "4", "66"]
print([int(i) for i in li])

print("N".join(li)) #2N4N66
# print(li.split("6")) #not gonna work on list

x=['a', 'g']
print(list(map(list,x))) #[['a'], ['g']]

print([i for i in map(lambda i: i + 6, [1,2,3])]) #[7, 8, 9]

odds=iter([1,3,5,7,9])
print(next(odds))#1
print(next(odds))#3

# copy
print(li)
newli = li.copy()
newli[0] = 'a'
print(li, newli)

t = tuple(i for i in ("6", "2", "3"))
t1 = t[:2]
print(t1[0], t)

print(list(), dict(), set(), tuple()) #[] {} set() ()
a=["1", "2", "4"]
# a[0] = 5
print(str(a))


