from abc import abstractstaticmethod, ABCMeta


class Car(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_car_type():
        pass


class Sedan(Car):
    def get_car_type(self):
        return "Sedan car"


class Hatchback(Car):
    def get_car_type(self):
        return "Hatchback car"


class SUV(Car):
    def get_car_type(self):
        return "SUV car"


class CarFactory:
    def show_cart_type(self, type):
        try:
            print(eval(type)().get_car_type())
        except:
            print("This car type is not defined")


if __name__ == '__main__':
    fb = CarFactory()
    fb.show_cart_type('Sedan')
    fb.show_cart_type('Hatchback')
    fb.show_cart_type('SUV')
