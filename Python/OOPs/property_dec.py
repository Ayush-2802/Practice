class Car:
    total_cars = 0
    def __init__(self, brands, model):
        self.__brands = brands
        self.__model = model
        Car.total_cars += 1
    
    @property
    def model(self):
        return self.__model

obj1 = Car("Tata","Safari")
# obj1.model = "city"
print(obj1.model)