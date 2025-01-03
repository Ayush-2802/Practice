class Car:
    total_cars = 0
    def __init__(self, brands, model):
        self.__brands = brands
        self.model = model
        Car.total_cars += 1

    def get_brands(self):
        return self.__brands

    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod
    def general_disc():
        return "Cars are awsome"

class Ev(Car):
    def __init__(self, brands,model,battery_cap):
        super().__init__(brands,model)
        self.battery_cap = battery_cap

    def fuel_type(self):
        return "electri charge"

obj = Ev("Tesla","ModelS","85KW")

print(isinstance(obj,Car))
print(isinstance(obj,Ev))