class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class Bike(Vehicle):
    def __init__(self, seat ,CC,brand , model):
        super().__init__(brand,model)
        self.seat =seat
        self.CC  = CC 
        print(f"The {self.brand} of {self.model} is {self.seat} seat and {self.CC} CC engine")

class Car(Vehicle):
    def __init__(self, seat ,CC, brand , model):
        super().__init__(brand,CC)
    
        self.seat =seat
        self.CC  = CC 
        print(f"The {self.brand} of {self.model} is {self.seat} seat and {self.CC} CC engine")

B = Bike(2,500,"Honda","XQWDF")




                

        