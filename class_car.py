class Car:
    """Simple attempt to represent a car"""
    def __init__(self, type, model, year):
        """Initializing attributes of the car"""
        self.type = type
        self.model = model
        self.year = year
        self.odometer_reading = 25

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.type} {self.model}"
        return long_name.title()

    def read_odometer(self):
        '''Prints a statement showing the cars mileage'''
        print(f"This car has {self.odometer_reading} miles on it.\n")

    def update_odometer(self, mileage):
        '''Set the odometer reading to a given value.
            Reject any attempt at rolling back the odometer'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        '''Add the given amount to the odometer reading.'''
        self.odometer_reading += miles

'''Calling functions'''
my_used_car = Car('toyota', 'corolla', 2012)
print(my_used_car.get_descriptive_name())

'''Print current mileage'''
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
'''Update the mileage and print'''
my_used_car.update_odometer(24000)
my_used_car.read_odometer()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(25)
my_new_car.read_odometer()

'''Creating a child class of existing car'''
class ElectricCar(Car):
    '''Represents aspects of a car, spesific to a electric car'''

    def __init__(self, type, model, year):
        '''Initialize attributes of the parent class.
            Then initialize attributes of an electric car'''
        super().__init__(type, model, year)
        self.battery = Battery()
    
    
    
    def fill_gas_tank(self):
        '''Electric cars don't have gas tanks'''
        print("This car doesn't need to fill the gas tank")

class Battery:
    
    def __init__(self, battery_size=100):
        '''Initialize the attributes of the battery'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size'''
        print(f"This car has a {self.battery_size}-kwh battery")
    
    def get_range(self):
        '''Prints a statement about the range this battery provides.'''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")


'''Calling functions'''
my_tesla = ElectricCar('tesla', 'model x', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()