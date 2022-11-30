from vehicles import Bicylce, Motorcycle, Car


if __name__ == '__main__':

    # Declare objects
    car = Car()
    bike = Bicylce()
    motorcycle = Motorcycle()

    # Print method call for each subclass.
    print(f"Power delivery for Bike: {bike.power_delivery()}")
    print(f"Number of passengers for Bicylce: {bike.number_passengers()}")
    print(f"Power delivery for Motorcycle: {motorcycle.power_delivery()}")
    print(f"Number of passengers for Motorcycle: {motorcycle.number_passengers()}")
    print(f"Power delivery for Car: {car.power_delivery()}")
    print(f"Number of passengers for Car: {car.number_passengers()}")