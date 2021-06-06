import re
import src.constant as const
from src.messages import ERROR_MESSAGES

PARKING_SPACE = {}
PARKER_DETAILS = {}
REG_NUM_AGE = {}
REG_SLOT_NUMBER = {}
AGE_SLOT_NUMBER = {}


def create_parking_lot(capacity):    
    """
    This method creates the parking in the parking space with the parking slots.
    Parking space have slots assigned based on the capacity of parking space.
    """
    if capacity < 1:
        print(ERROR_MESSAGES.null_parking.get_message())
        return


    for i in range(capacity):
        # parking spaces are created using incremental count
        PARKING_SPACE[i + 1] = False

    print(const.PARKING_CREATED % (capacity))


def is_valid_registration_number(registration_number):
        """
        This method validates for the correctness of the registration number of vehicle.
        It follows the rule of "2 caps letters followed by 2 integers followed by 2 caps letters and 4 integers" 
        all seperated by hyphens
        eg: AA-00-BB-111 is a valid registration number
        """

        if re.match(const.REGISTRATION_NO_FORMAT, registration_number):
            return True
        return False


def park(registration_number, driver_age):
    """
    This method creates is used to offer a parking slot from the parking space to the vehicle owner based on 
    registration number and age. The nearest empty parking slot is assignmed to the driver automatically.
    """
    
    if driver_age < const.DRIVING_AGE:
        print(ERROR_MESSAGES.age_invalid.get_message())
        return
    
    # check if the vehicle registarion number is in specified format
    # if not, do not register the vehicle
    if not is_valid_registration_number(registration_number):
        print(ERROR_MESSAGES.non_registerable.get_message())
        return

    slot = 0
    # each parking slot is checked and the nearest parking slot is made available
    # all occupied slots are marked boolean True
    for parking_slot in PARKING_SPACE.keys():
        if PARKING_SPACE[parking_slot] is False:
            PARKING_SPACE[parking_slot] = True
            slot = parking_slot
            break

    # if no parking slot is available currently
    if not slot:
        print(ERROR_MESSAGES.parking_occupied.get_message())
        return
    
    # storing all the details of the parker
    PARKER_DETAILS[slot] = {const.REGISTRATION_NUMBER: registration_number, const.DRIVER_AGE: driver_age}
    
    # storing the parkers vehicle registration number in age group based on the the parkers age
    if REG_NUM_AGE.get(driver_age):
        REG_NUM_AGE[driver_age].append(registration_number)
    else:
        REG_NUM_AGE[driver_age] = [registration_number]
    
    # mapping the parkers vehicle registration against the slot associated to the parker
    # assumption that the vehicles will have unique registration number is followed
    if registration_number not in REG_SLOT_NUMBER:
        REG_SLOT_NUMBER[registration_number] = slot

     # mapping the parkers age against the slot associated to the parker
    if AGE_SLOT_NUMBER.get(driver_age):
        AGE_SLOT_NUMBER[driver_age].append(slot)
    else:
        AGE_SLOT_NUMBER[driver_age] = [slot]

    print(const.CAR_PARKED % (registration_number, slot))


def leave(slot):
    """
    This method marks the slots in the parking space to be vaccant.
    It removes all the associated mappings of the parker.
    """

    if slot in PARKING_SPACE:
        if PARKING_SPACE[slot] is True:
            PARKING_SPACE[slot] = False
        else:
            # if slot is already vaccant it send the error message
            print(ERROR_MESSAGES.vaccant_slot.get_message())
            return

        registration_number = PARKER_DETAILS[slot][const.REGISTRATION_NUMBER]
        driver_age = PARKER_DETAILS[slot][const.DRIVER_AGE]

        del PARKER_DETAILS[slot]

        if driver_age in REG_NUM_AGE:
            REG_NUM_AGE[driver_age].remove(registration_number)

        if registration_number in REG_SLOT_NUMBER:
            REG_SLOT_NUMBER.pop(registration_number)

        if driver_age in AGE_SLOT_NUMBER:
            AGE_SLOT_NUMBER[driver_age].remove(slot)
            if len(AGE_SLOT_NUMBER[driver_age]) == 0:
                del AGE_SLOT_NUMBER[driver_age]

        print(const.SLOT_EMPTY % (slot, registration_number, driver_age))
    else:
        # if slot is not the part of the parking space it send the error message
        print(ERROR_MESSAGES.slot_out_of_bound.get_message())


def vehicle_registration_number_for_driver_of_age(driver_age):
    """
    It queries the registration number of the drivers belonging to a certain age group.
    If invalid or incorrect driver age is passed it raises appropriate errors
    """

    vehicle_registration_number = None
    try:
        driver_age = int(driver_age)
        if REG_NUM_AGE.get(driver_age):
            vehicle_registration_number = ','.join(REG_NUM_AGE[driver_age])
        else:
            vehicle_registration_number = ERROR_MESSAGES.slot_not_found.get_message()
    except ValueError:
        vehicle_registration_number = ERROR_MESSAGES.slot_not_found.get_message()

    print(vehicle_registration_number)


def slot_numbers_for_driver_of_age(driver_age):
    """
    It queries the slot numbers of the drivers belonging to a certain age group.
    If invalid or incorrect driver age is passed it raises appropriate errors
    """

    slot_number = None
    try:
        driver_age = int(driver_age)
        if AGE_SLOT_NUMBER.get(driver_age):
            slot_number = ','.join(map(str, AGE_SLOT_NUMBER[driver_age]))
        else:
            slot_number = ERROR_MESSAGES.slot_not_found.get_message()
    except ValueError:
        slot_number = ERROR_MESSAGES.slot_not_found.get_message()

    print(slot_number)


def slot_number_for_car_with_number(registration_number):
    """
    It fetches the slot number where the registered car is parked.
    """
    slot_number = None
    slot_number = str(REG_SLOT_NUMBER[registration_number]) if  REG_SLOT_NUMBER.get(registration_number) else ERROR_MESSAGES.slot_not_found.get_message()

    print(slot_number)
