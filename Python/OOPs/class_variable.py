class Car:
    total_cars = 0
    def __init__(self, brands, model):
        self.__brands = brands
        self.model = model
        Car.total_cars += 1

    def get_brands(self):
        return self.__brands

    def full_name(self):
        return (f"Brand:{self.brands} Model: {self.model}")

    def fuel_type(self):
        return "petrol or diesel"

class EV(Car):
    def __init__(self, brands,model,battery_cap):
        super().__init__(brands,model)
        self.battery_cap = battery_cap

    def fuel_type(self):
        return "electri charge"

EV("Tesla","ModelS","85KW")
Car("Tata","Safari")
Car("MarutiSuzuki","WagonR")
Car("Mahindara","bulero")

print(Car.total_cars)
