from src.exception_const import ErrorObject

class ERROR_MESSAGES:
    unknown_error = ErrorObject(
        0, "Oops! Something went wrong!")
    parking_directions_not_valid = ErrorObject(
        1, "Parking direction is not valid")
    parking_occupied = ErrorObject(
        2, "Sorry, Parking space does not having any vaccant slots currently.")
    slot_not_found = ErrorObject(
        3, "No parked car matches the query")
    vaccant_slot = ErrorObject(
        4, "Parking slot is already vaccant")
    slot_out_of_bound = ErrorObject(
        5, "Parking slot is not available in parking space")
    non_registerable = ErrorObject(
        6, "Parking space cannot be provided to vehicle with invalid registration number")
    null_parking = ErrorObject(
        7, "Parking space cannot be initiated to non existing values")
    age_invalid = ErrorObject(
        8, "Driver does not have minimum driving age")
