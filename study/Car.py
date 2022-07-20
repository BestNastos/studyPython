class Car:

    # создаем атрибуты класса
    car_count = 0

    # создаем методы класса
    def start(self, name, make, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

    def __repr__(self):
        return "repr"
car_a = Car()
print(Car.car_count)
# print(car_a.name) #AttributeError: 'Car' object has no attribute 'name'
car_a.start("Corrola", "Toyota", 2015)
print(car_a.name)
print(car_a.car_count)
print(car_a)