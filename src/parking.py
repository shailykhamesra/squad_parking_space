import re
import src.constant as const
import src.parking_helper as ph
from src.messages import ERROR_MESSAGES


class ParkingSpace():

    def __init__(self, input):
        self.parking_directions = input


    def initialize_parking(self):
        """
        This method initialize the parking space and creates a interface for the parking system.
        All exception catches have been handled here. It helps communicating to all the helper methods.
        """
        
        for directions in self.parking_directions:
            try:
                directions = directions.split()
                class_method = getattr(self, directions[0].lower())
                class_method(directions[1:])
            except (AttributeError, ValueError, IndexError):
                print(ERROR_MESSAGES.parking_directions_not_valid.get_message())
            except Exception as e:
                print(ERROR_MESSAGES.unknown_error.get_message())

    def create_parking_lot(self, parking_capacity):
        """
        This method is used as a interface for creating a parking space using parking helper
        """

        capacity = int(parking_capacity[0])
        ph.create_parking_lot(capacity)


    def park(self, parkers_data):
        """
        This method is used as a interface for parking vehicles using parking helper
        """
        registration_number = parkers_data[0]
        driver_age = int(parkers_data[2])
        ph.park(registration_number, driver_age)


    def leave(self, parking_slot):
        """
        This method is used as a interface for letting vehicles out of the parking space using parking helper
        """

        slot = int(parking_slot[0])
        ph.leave(slot)

    def slot_numbers_for_driver_of_age(self, driver_age):
        """
        This method is used as a interface for quering slot number based on age using parking helper
        """

        ph.slot_numbers_for_driver_of_age(driver_age[0])

    def slot_number_for_car_with_number(self, reg_no):
        """
        This method is used as a interface for quering slot number for vehicle based on vehicle registration number using parking helper
        """

        ph.slot_number_for_car_with_number(reg_no[0])

    def vehicle_registration_number_for_driver_of_age(self, driver_age):
        """
        This method is used as a interface for quering vehicles registration number based on parkers age using parking helper
        """

        ph.vehicle_registration_number_for_driver_of_age(driver_age[0])