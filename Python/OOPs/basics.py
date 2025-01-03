class Car:
    def __init__(self, brands, model):
        self.brands = brands
        self.model = model

    def full_name(self):
        return (f"Brand:{self.brands} Model: {self.model}")


obj = Car("ferrari","SF40")
print(obj.full_name())