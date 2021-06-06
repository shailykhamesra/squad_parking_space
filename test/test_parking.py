import pytest
import sys
from unittest import TestCase
from io import StringIO
from unittest.mock import patch
import src.constant as const
import src.parking_helper as ph
from src.messages import ERROR_MESSAGES

@pytest.mark.parking_space
class ParkingSpaceTest(TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        pass
        


    # to test the parking slot allotment with negative values
    @patch.dict(ph.PARKING_SPACE, {}, clear=True)
    def test_create_invalid_parking_lot(self):
        capacity = -1
        expected_message = ERROR_MESSAGES.null_parking.get_message()
        ph.create_parking_lot(capacity)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)


    # to test the parking slot allotment and the message after allotment
    @patch.dict(ph.PARKING_SPACE, {}, clear=True)
    def test_create_parking_lot(self):
        capacity = 3
        expected_output = {1: False, 2: False, 3: False}
        expected_message = const.PARKING_CREATED % (capacity)
        ph.create_parking_lot(capacity)
        self.assertDictEqual(ph.PARKING_SPACE, expected_output)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)


    # test when parking slot is occupied
    @patch.dict(ph.PARKING_SPACE, {1: True, 2: True, 3: True}, clear=True)
    @patch.dict(ph.PARKER_DETAILS, {}, clear=True)
    def test_park_fully_occupied(self):
        registration_number = "AA-01-BB-1111"
        driver_age = 21
        expected_message = ERROR_MESSAGES.parking_occupied.get_message()
        ph.park(registration_number, driver_age)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)


    # test when parking space is not available
    @patch.dict(ph.PARKING_SPACE, {}, clear=True)
    @patch.dict(ph.PARKER_DETAILS, {}, clear=True)
    def test_park_not_created(self):
        registration_number = "AA-01-BB-1111"
        driver_age = 21
        expected_message = ERROR_MESSAGES.parking_occupied.get_message()
        ph.park(registration_number, driver_age)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)


    # test when parkers registartion number is not valid
    @patch.dict(ph.PARKING_SPACE, {1: True, 2: False, 3: True}, clear=True)
    @patch.dict(ph.PARKER_DETAILS, {}, clear=True)
    def test_park_invalid_registration_number(self):
        registration_number = "AA-01-B-111"
        driver_age = 21
        expected_message = ERROR_MESSAGES.non_registerable.get_message()
        ph.park(registration_number, driver_age)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)

    
    # test for parkers age
    @patch.dict(ph.PARKING_SPACE, {1: True, 2: False, 3: False}, clear=True)
    @patch.dict(ph.PARKER_DETAILS, {}, clear=True)
    def test_park_invalid_age(self):
        registration_number = "AA-01-BB-1111"
        driver_age = 12
        expected_message = ERROR_MESSAGES.age_invalid.get_message()
        ph.park(registration_number, driver_age)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)

    # test for nearest parking slot allotment
    @patch.dict(ph.PARKING_SPACE, {1: True, 2: False, 3: False}, clear=True)
    @patch.dict(ph.PARKER_DETAILS, {}, clear=True)
    def test_park_nearest_slot(self):
        registration_number = "AA-01-BB-1111"
        driver_age = 21
        expected_message = const.CAR_PARKED % (registration_number, 2)
        ph.park(registration_number, driver_age)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)


    # test for parking details mapping
    @patch.dict(ph.PARKING_SPACE, {1: True, 2: True, 3: False}, clear=True)
    @patch.dict(ph.PARKER_DETAILS, {}, clear=True)
    def test_park_details(self):
        registration_number = "AA-01-BB-1111"
        driver_age = 21
        expected_message = const.CAR_PARKED % (registration_number, 3)
        ph.park(registration_number, driver_age)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)
        self.assertDictEqual(ph.AGE_SLOT_NUMBER, {driver_age: [3]})
        self.assertDictEqual(ph.REG_SLOT_NUMBER, {registration_number: 3})
        self.assertDictEqual(ph.PARKER_DETAILS, {3: {const.REGISTRATION_NUMBER: registration_number, const.DRIVER_AGE: driver_age}})
        

    # test for slot not present in parking space
    @patch.dict(ph.PARKING_SPACE, {1: False, 2: True, 3: True}, clear=True)
    @patch.dict(ph.PARKER_DETAILS, {2: {const.REGISTRATION_NUMBER: "AA-01-BB-1111", const.DRIVER_AGE: 21}}, clear=True)
    @patch.dict(ph.REG_NUM_AGE, {21: ["AA-01-BB-1111"]}, clear=True)
    @patch.dict(ph.REG_SLOT_NUMBER, {"AA-01-BB-1111": 2}, clear=True)
    @patch.dict(ph.AGE_SLOT_NUMBER, {21: [2]}, clear=True)
    def test_leave_slot_not_present(self):
        slot = 4
        registration_number = "AA-01-BB-1111"
        driver_age = 21
        expected_message = ERROR_MESSAGES.slot_out_of_bound.get_message()
        ph.leave(slot)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)


    @patch.dict(ph.PARKING_SPACE, {1: False, 2: True, 3: True}, clear=True)
    @patch.dict(ph.PARKER_DETAILS, {2: {const.REGISTRATION_NUMBER: "AA-01-BB-1111", const.DRIVER_AGE: 21}}, clear=True)
    @patch.dict(ph.REG_NUM_AGE, {21: ["AA-01-BB-1111"]}, clear=True)
    @patch.dict(ph.REG_SLOT_NUMBER, {"AA-01-BB-1111": 2}, clear=True)
    @patch.dict(ph.AGE_SLOT_NUMBER, {21: [2]}, clear=True)
    def test_leave(self):
        slot = 2
        registration_number = "AA-01-BB-1111"
        driver_age = 21
        expected_message = const.SLOT_EMPTY % (slot, registration_number, driver_age)
        ph.leave(slot)
        self.assertDictEqual(ph.REG_NUM_AGE, {driver_age: []})
        self.assertDictEqual(ph.REG_SLOT_NUMBER, {})
        self.assertDictEqual(ph.AGE_SLOT_NUMBER, {})
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)


    @patch.dict(ph.REG_SLOT_NUMBER, {"AA-01-BA-1111": 1, "AA-01-BC-1111": 2}, clear=True)
    def test_slot_number_for_car_with_number(self):
        registration_number = "AA-01-BA-1111"
        expected_message = "1"
        ph.slot_number_for_car_with_number(registration_number)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)

    @patch.dict(ph.REG_SLOT_NUMBER, {"AA-01-BA-1111": 1, "AA-01-BB-1111": 2}, clear=True)
    def test_slot_number_for_car_with_number_does_not_exist(self):
        registration_number = "AA-01-BA-1112"
        expected_message = ERROR_MESSAGES.slot_not_found.get_message()
        ph.slot_number_for_car_with_number(registration_number)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)


    # test for the slot number based on driver age
    @patch.dict(ph.AGE_SLOT_NUMBER, {21: [1, 6, 3]}, clear=True)
    def test_slot_numbers_for_driver_of_age(self):
        driver_age = 21
        expected_message = "1,6,3"
        ph.slot_numbers_for_driver_of_age(driver_age)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)

    # test for the slot number based on invalid driver age
    @patch.dict(ph.AGE_SLOT_NUMBER, {21: [2, 4]}, clear=True)
    def test_slot_numbers_for_driver_of_age(self):
        driver_age = "aa"
        expected_message = ERROR_MESSAGES.slot_not_found.get_message()
        ph.slot_numbers_for_driver_of_age(driver_age)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)

   
   # test invalid driver age
    @patch.dict(ph.REG_NUM_AGE, {"21": ["AA-01-BC-1111", "AA-01-BD-1111", "AA-01-BA-1111"]}, clear=True)
    def test_vehicle_registration_number_for_driver_of_age(self):
        driver_age = 'aa'
        expected_message = ERROR_MESSAGES.slot_not_found.get_message()
        ph.vehicle_registration_number_for_driver_of_age(driver_age)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)

    # test for all reg no form drivers age
    @patch.dict(ph.REG_NUM_AGE, {21: ["AA-01-BC-1111", "AA-01-BD-1111", "AA-01-BA-1111"]}, clear=True)
    def test_vehicle_registration_number_for_driver_of_age(self):
        driver_age = 21
        expected_message = "AA-01-BC-1111,AA-01-BD-1111,AA-01-BA-1111"
        ph.vehicle_registration_number_for_driver_of_age(driver_age)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_message)
