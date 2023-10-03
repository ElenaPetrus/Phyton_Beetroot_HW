from datetime import datetime

from .vehicles import Vehicle, Car, Truck


class TestVehicle:

    initial_mileage = 100000
    vehicle = Vehicle("Chrysler 200", 5, initial_mileage,
                      "Chrysler", "petrol engine", 200)

    def test_vehicle_name(self):
        assert self.vehicle.name == "Chrysler 200"

    def test_vehicle_drive(self):
        self.vehicle.drive(50)
        assert self.vehicle.mileage == self.initial_mileage + 50

    def test_vehicle_tyres_change(self):
        self.vehicle.current_tyres = "summer tyres"
        assert not self.vehicle.tyre_change_time_has_come(5)


class TestTruck(TestVehicle):
    initial_mileage = 100000
    vehicle = Truck(1000, "Chrysler 200", 5, initial_mileage,
                    "Chrysler", "petrol engine", 200)

    # this method is specific to trucks, all the others are inherited from TestVehile
    def test_load_capacity(self):
        assert self.vehicle.load_capacity == 1000


class TestCar(TestVehicle):
    # all the tests are inherited from TestVehicle
    initial_mileage = 100000
    vehicle = Car(5, "Chrysler 200", 5, initial_mileage,
                  "Chrysler", "petrol engine", 200)
