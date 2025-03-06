class Car:
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec}): Двигун запущено")


class Motorcycle:
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec}): Мотор заведено")


class VehicleFactory:
    def create_car(self, make, model):
        raise NotImplementedError

    def create_motorcycle(self, make, model):
        raise NotImplementedError


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU Spec")


us_factory = USVehicleFactory()
vehicle1 = us_factory.create_car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sport")
vehicle2.start_engine()

eu_factory = EUVehicleFactory()
vehicle3 = eu_factory.create_car("BMW", "M3")
vehicle3.start_engine()

vehicle4 = eu_factory.create_motorcycle("Ducati", "Sport")
vehicle4.start_engine()
