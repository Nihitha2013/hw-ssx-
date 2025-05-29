class vehicle:
    def maxspeed(self):
        pass

class BMW(vehicle):
    def maxspeed(self):
        return "BMW max speed is 155 mph"
    def fueltype(self):
        return "BMW fuel type is petrol"

class Ferrari(vehicle):
    def maxspeed(self):
        return "Audi maxspeed is 250 mph"
    def fueltype(self):
        return "Audi fuel type is petrol"
    

obj=[BMW(),Ferrari()]

for i in (obj):
    print(i.maxspeed())
    print(i.fueltype())


