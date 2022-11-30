from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def power_delivery(self):
        pass

    @abstractmethod
    def number_passengers(self):
        pass


class Bicylce(Vehicle):

    def __init__(self):
        self.power = "Calories"
        self.min = 1
        self.max = 2

    def power_delivery(self):
        return f"{self.power}, open"

    def number_passengers(self):
        return f"{self.min} or {self.max} max"


class Motorcycle(Vehicle):
    def __init__(self):
        self.power = "Engine powered"
        self.min = 1
        self.max = 2

    def power_delivery(self):
        return f"{self.power}, open"

    def number_passengers(self):
        return f"{self.min} or {self.max}"


class Car(Vehicle):
    def __init__(self):
        self.power = "Engine powered"
        self.min = 1
        self.max = 4

    def power_delivery(self):
        return f"{self.power}, enclosed"

    def number_passengers(self):
        return f"{self.min} to {self.max} people"