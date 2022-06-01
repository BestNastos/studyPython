name = 'Anastasia'
print(f'my name is {name}')
print('my name is %s' % name)
print("my name is {}".format(name))
print("me "*5)

print(name[0])#A
print(name[:2])#An
print(name[-1])#a
print(name[::2])#Aatsa

print(name.count("a"))#3
print(name.find("n"))#1
print(name.startswith("Ana"))#true
print(name.endswith("Ana"))#false

print(name.replace("A", "a"))#anastasia
print(name)#Anastasia

test = " test "
print(test.strip())#test
print(name.strip("a"))#Anastasi

sent = "I am, Anastasia"
print(sent.split())#['I', 'am,', 'Anastasia']
print(sent.split(","))#['I am', ' Anastasia']
print("T".join(sent)) #IT TaTmT,T TATnTaTsTtTaTsTiTa

s = ('test' 'test')
print(s)#testtest

pyt = "I love Python" #task: print I love Py
print(pyt[:-4]) #I love Py

i = 0
while pyt[i] != "t":
    print(pyt[i], end="") #I love Py
    i += 1

print(pyt.replace(" ", ""))#task: print I love Python without white spaces
for i in pyt:
    if i != " ":
        print(i, end="")#IlovePython

longstr = """
    test
test
    test
test"""



