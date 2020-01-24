class Vechile:
    def __init__(self, price, color):
        self.color = color 
        self.price = price  
     
    def fillUPtank(self):
        self.gas = 100
    
    def emptyTank(self):
        self.gas = 0

class Truck(Vechile):
    def __init__(self, price, color, tires):
        super().__init__(price,color)
        self.tires = tires 

    def beep(self):
        print("Honk Honk")

class Car(Vechile):
    def __init__(self, price, color, speed):
        super().__init__(price,color)
        self.speed = speed 

    def beep(self):
        print("Beep Beep")
    
    