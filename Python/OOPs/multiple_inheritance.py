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

class Battery:
    def __init__(self,battery_cap):
        self.battery_cap = battery_cap

class Engine:
    def __init__(self,Engine_info):
        self.Engine_info = Engine_info
    

class Ev(Car,Battery,Engine):
    def __init__(self,brands,model,battery_cap,Engine_info):
        Car.__init__(self,brands,model)
        Battery.__init__(self,battery_cap)
        Engine.__init__(self,Engine_info)

    def fuel_type(self):
        return "electri charge"



obj = Ev("Tesla","ModelS","85KW","v8")
print(obj.battery_cap)
print(obj.Engine_info)