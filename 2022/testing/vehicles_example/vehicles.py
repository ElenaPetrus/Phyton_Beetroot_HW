from datetime import datetime


class Vehicle:

    def __init__(
        self, name, seats, mileage, manufacturer, engine_type, engine_power,
        current_tyres="winter tyres",
    ):
        self.name = name
        self.seats = seats
        self.mileage = mileage
        self.speed = 0
        self.manufacturer = manufacturer
        self.engine_type = engine_type
        self.engine_power = engine_power
        self.current_tyres = current_tyres

    tyres_change_time_map = {
        "winter tyres": (1, 2, 3, 11, 12),
        "summer tyres": (4, 5, 6, 7, 8, 9, 10),
    }

    def drive(self, miles_driven):
        self.mileage += miles_driven

    def press_acceleration_pedal(self, speed):
        self.speed += speed

    def tyre_change_time_has_come(self, month_to_check=None):
        if not month_to_check:
            current_month = datetime.now().month
        else:
            current_month = month_to_check
        return current_month not in self.tyres_change_time_map[self.current_tyres]


class Car(Vehicle):
    # please create some attributes/methods that are specific for cars only
    def __init__(self, trunk_size, *args):
        Vehicle.__init__(self, *args)
        self.trunk_size = trunk_size


class Truck(Vehicle):
    # please create some attributes/methods that are specific for trucks only
    def __init__(self, load_capacity, *args):
        Vehicle.__init__(self, *args)
        self.load_capacity = load_capacity


vehicle = Vehicle("Chrysler 200", 5, 100000, "Chrysler", "petrol engine", 200)
print(vehicle.tyre_change_time_has_come())
