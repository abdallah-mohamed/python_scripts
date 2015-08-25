"""
3) [35 points] Write a class Car that keeps track of the name of the car, the
fuel efficiency in miles per gallon (mpg), the number of miles driven, and the
number of gallons left in the gas tank. The constructor should take the car name
and the fuel efficiency as input. Write the class declaration first and then
define the member functions for the class. You'll have to figure out what
functions to add based on the sample usage below:
my_car = Car( "Ferrari Testarossa", 20 ); // 20 miles per gallon.
my_car.add_gas(10); // Add 10 gallons of gas to the tank.
my_car.drive(100); // Drive 100 miles.
print(my_car.get_name() + " has driven " + my_car.get_miles()
+ " miles and has " + my_car.get_gas( ) + " gallons left in the tank.");
Output: Ferrari Testarossa has driven 100 miles and has 5 gallons left in the
tank.
"""


class Car(object):

    def __init__(self, name, mpg):
        self._name = name
        self._mpg = mpg
        self._num_miles_driven = 0
        self._num_gallons_left = 0

    def add_gas(self, num_gallons):
        self._num_gallons_left += num_gallons

    def drive(self, num_miles):
        self._num_miles_driven += num_miles
        self._num_gallons_left -= num_miles / self._mpg

    def get_name(self):
        return self._name

    def get_miles(self):
        return self._num_miles_driven

    def get_gas(self):
        return self._num_gallons_left


def create_car():
    my_car = Car("Ferrari Testarossa", 20)
    my_car.add_gas(10)
    my_car.drive(100)
    print(my_car.get_name() + " has driven " + str(my_car.get_miles()) + " miles and has "
          + str(my_car.get_gas()) + " gallons left in the tank.")

if __name__ == "__main__":
    create_car()
