from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(f"{make} (US Spec)", model)

    def create_motorcycle(self, make, model):
        return Motorcycle(f"{make} (US Spec)", model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make, model):
        return Motorcycle(f"{make} (EU Spec)", model)


class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")


vehicle1 = Car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = Motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()


# Create fabrics
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

# Create cars and motorcycles by fabrics
us_car = us_factory.create_car("Ford", "Mustang")
eu_motorcycle = eu_factory.create_motorcycle("BMW", "R1200")

# Use methodes
us_car.start_engine()
eu_motorcycle.start_engine()
