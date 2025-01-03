class Car:
    def __init__(self, brands, model):
        self.__brands = brands
        self.model = model

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

obj = EV("Tesla","ModelS","85KW")
print(obj.fuel_type())

obj2 = Car("Tata","Safari")
print(obj2.fuel_type())
