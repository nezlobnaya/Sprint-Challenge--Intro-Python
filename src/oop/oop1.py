# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle: #base class
    pass

class FlightVehicle(Vehicle): #subclass of vehicle
    pass

class Starship(FlightVehicle): #subclass of Flightvehicle which is a subclass of Vehicle
    pass

class GroundVehicle(Vehicle): #subclass of Vehicle
    pass

class Airplane(FlightVehicle): #subclass of vehicle
    pass

class Car(GroundVehicle): #subclass of GroundVehicle which is a subclass of Vehicle
    pass

class Motorcycle(GroundVehicle): #subclass of Groundvehicle which is a subclass of Vehicle
    pass

