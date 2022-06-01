class Car:

    brand = "default brand"

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def change_color(self, color):
        self.color = color

    def check_inheritance(self):
        return "Check inheritance - Car"

    def change_brand(self, brand):
        self.brand = brand

    def start(self, a, b=None, c=None):
            print(a , b , c)


    # @classmethod
    # def change_brand(cls, brand): #will overshadow non-static method with this name
    #     cls.brand = brand

    @staticmethod
    def get_brand():
        return 'get brand static'

    @classmethod
    def change_color_cls(cls, color):
        cls.color = color

class Audi(Car):

    def check_inheritance(self):
        return "Check inheritance - Audi"

if __name__ == "__main__":
    audi = Audi("red", "60")
    print(audi.check_inheritance())

    car = Car("red", "60")
    car_1 = Car("green", "70")
    print(Car("red", "60").color)
    print(car.speed)
    car.start("a", "b")

    car.change_brand('BMW')
    print(car.brand)
    print(car_1.brand)

    car.change_color_cls('color cls')
    print(car.color)
    print(car_1.color)
    print(Car.get_brand())

    car.change_color("purple")
    print(car.color)
    print(car_1.color)
    print(dir(car))

    vehicles = [car, audi]
    for i in vehicles:
        print(i.check_inheritance())

class A:
    p = 1234
    def getX (self):
        return self.x

    def setX (self, value):
        self.x = value


    x = property(getX, setX)












# red
# 60
# BMW
# Audi
# BMW
# honda
# get brand
# Check inheritance - Car
# Check inheritance - Audi