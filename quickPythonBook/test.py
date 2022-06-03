import mymath
import study.study1
class Circle:
    def __init__(self):
        pass


my_circle = Circle()
my_circle.radius = 5 #you can define a field of an object on the fly
print(my_circle.radius)

circle = Circle()
# print(circle.radius) #produces an error because radius is defined on the fly for only one instance

print(mymath.pi)
print(study.study1.test)