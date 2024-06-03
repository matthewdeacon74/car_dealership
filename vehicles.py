class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def start_engine(self):
        print("Starting engine...")
        self.engine_on = True

    def make_noise(self):
        print("\tBeep Beep!")

    def get_info(self):
        return f"The {self.make} with {self.miles} miles costs ${self.price}"


class Truck(Vehicle):
    def __init__(self, make, miles, price):
        super().__init__(make, miles, price)
        self.cargo = False

    def load_cargo(self):
        print("Loading the truck bed...")
        self.cargo = True


class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        super().__init__(make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print("\tVroom vroom!")

    def get_info(self):
        return f"The {self.make} with {self.miles} miles and a top speed of {self.top_speed}MPH costs ${self.price}"
