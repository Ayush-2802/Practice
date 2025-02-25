class Car:
    def __init__(self, brands, model):
        self.brands = brands
        self.model = model

    def full_name(self):
        return (f"Brand:{self.brands} Model: {self.model}")

class EV(Car):
    def __init__(self, brands,model,battery_cap):
        super().__init__(brands,model)
        self.battery_cap = battery_cap

obj = EV("Tesla","ModelS","85KW")
print(obj.full_name(),"Battery:",obj.battery_cap)
