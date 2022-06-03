from topics.Car import Car


class Audi(Car):

    def change_brand(self, brand):
        print("Change brand in Audi to " + brand)


car = Audi("red", "60")
car.change_brand('BMW')