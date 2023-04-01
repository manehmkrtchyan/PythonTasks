'''Write a program that simulates a ride-sharing service. 
The program should have classes for drivers, passengers, and rides.
Drivers should have attributes such as name and contact information, and a vehicle. 
Passengers should have attributes such as name and contact information.
Rides should have attributes such as the driver, the passenger, the ride destination, 
and the ride fare. The program should allow passengers to request rides, 
drivers to accept and complete rides, and both to rate each other. 
Use inheritance to implement classes for different types of vehicles 
(e.g., cars, motorcycles) and abstract classes for ride-sharing operations.'''
from  abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self) -> None:
        pass
    @abstractmethod
    def get_type(self):
        pass
class Car(Vehicle):
    def get_type(self):
        return 'Car'
class Motorcycle(Vehicle):
    def get_type(self):
        return 'Motorcycle'
class Driver:
    def __init__(self, name, contact, vehicle) -> None:
        self.name = name
        self.contact = contact
        self.vehicle = vehicle
        self.rating = []
        self.rides = []
    def rate_passenger(self, passenger, rate):
        passenger.rating.append(rate)
    def accept_ride(self, passenger):
        self.rides.append(passenger.current_ride)
        print('The ride is accepted')
class Passenger:
    def __init__(self, name, contact) -> None:
        self.name = name
        self.contact = contact
        self.rating = []
    def request(self, driver, destination):
        new_ride = Ride(driver, self, destination)
        self.current_ride = new_ride
    def rate_driver(self, driver, rate):
        driver.rating.append(rate)
class Ride:
    def __init__(self, driver, passenger, destination) -> None:
        self.driver = driver
        self.passenger = passenger
        self.destination = destination
car = Car()       
pas = Passenger('mane', 'scns')
dr = Driver('nsmxd', 'dcnk', car)
pas.request(dr, 'Yerevan')
dr.accept_ride(pas)