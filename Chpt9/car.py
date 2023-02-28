class Car:
    def __init__(self,  make, model, year):
        self.make= make
        self.model=model
        self.year= year
        self.odometer=0 #default value
    
    def description_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it.")

    def update_odometer(self, mileage):
        if mileage>= self.odometer:
            self.odometer= mileage
        else:
            print("you cannot roll back an odomoter.")
    
    def increment_odometer(self, miles):
        self.odometer += miles

    def fill_gas_tank(self):
        print("filling the gas tank")

class Electric(Car): #eletric car is a child class from super class car
    def __init__(self,make, model, year):
        super().__init__(make, model, year)
        self.battery=Battery() #default battery size of KWh
    
    # This method overrides method from car (parent class)
    def fill_gas_tank(self):
        print("Electric cars do not have a gas tank")

class Battery:
    def __init__(self,battery_size=75):
        self.battery_size=battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size} - kWh battery")

    def get_range(self):
        if self.battery_size == 75:
            range=260
        else:
            range = 315
        
        print(f"This car has a range of {range} miles on a full charge.")

    def upgrade_battery(self, battery_size):
        if battery_size <= 75:
            self.battery_size =100
            print(f"Upgrading the battery size to {self.battery_size}")
        elif battery_size ==100:
            print(f"No need to upgrade the battery. ")

my_tesla=Electric('Tesla', 'model s', '2018')
print(my_tesla.description_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery(battery_size=75)
print()
my_Mustang=Car('Ford', 'Mustang', '2017')
my_Mustang.fill_gas_tank()