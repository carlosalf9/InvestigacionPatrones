""" main method """ if name == "main":

"""list to store objects"""
objects = [] 

motorCycle = MotorCycle() 
objects.append(Adapter(motorCycle, wheels = motorCycle.TwoWheeler)) 

truck = Truck() 
objects.append(Adapter(truck, wheels = truck.EightWheeler)) 

car = Car() 
objects.append(Adapter(car, wheels = car.FourWheeler)) 

for obj in objects: 
   print("A {0} is a {1} vehicle".format(obj.name, obj.wheels())) 