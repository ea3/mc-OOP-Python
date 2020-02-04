class Kettle(object):

    power_source = "electrocity"       # THIS IS A CLASS ATTRIBUTE. ALL INSTANCE  VARIABLES WILL SHARE THIS ATTRIBUTE.

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
hamilton.switch_on()
print(hamilton.on)

print(hamilton.make)
print(hamilton.price)

print("Models: {}, {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. ALl objects created using the same class will have the same characteristics
Object: an instance of a class. 
Instantiate: Create an instance of a class. 
Method: a function defined in a class
Attribute: a variable bound to an instance of a class. 
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

print("********")
kenwood.power = 1.5
print(kenwood.power)
hamilton.power = 5
print(hamilton.power)
Kettle.power_source = "Atomic power"
kenwood.power_source = "Un cacharro viejo"

# Subclasses are preferable for adding functionality to instances.

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)


