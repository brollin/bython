# Classes defined in python2 as subclassing object
# are made as 'new style' classes. This means 
# objects are of type 'type' and not 'classobj'.
# It is best to always define classes in the 
# new style in python2. In python3, everything
# is automatically new style.
class Car(object):
    def __init__(self, make='NoMake', model='NoModel'):
        self.make = make
        self.model = model

    def beep(self):
        return 'Beep!'

    def __str__(self):
        return 'Make:  %s\nModel: %s' % (self.make, self.model)

class Truck(Car):
    def __init__(self, horsepower=None, *args, **kwargs):
        self.horsepower = horsepower
        
        # This line calls the super class's constructor
        super(Truck, self).__init__(*args, **kwargs)

    def beep(self):
        return 'Honk!'

    def __str__(self):
        return super(Truck, self).__str__() + \
            '\nHorespower: %s' % self.horsepower

car = Car('Ford','Taurus')
print(car)
print(car.beep())

# Instantiating an object with a super constructor
truck = Truck(300, 'Ford', 'Ranger')
print(truck)
print(truck.beep())


