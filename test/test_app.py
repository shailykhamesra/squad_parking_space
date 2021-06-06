import pytest
import sys
from unittest import TestCase
from io import StringIO
from unittest.mock import patch
import src.constant as const
from src.parking import ParkingSpace
import src.parking_helper as ph
from src.messages import ERROR_MESSAGES


@pytest.mark.parking_space
class TestApp(TestCase):
    
    # @pytest.fixture()
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        pass
    

    def build_parking_space(self, parking_direction):
        return ParkingSpace(parking_direction)

    # test parking space creation with invalid capacity
    def test_create_parking_lot_value_error(self):
        parking_direction = ['Create_parking_lot', '6']
        ps = self.build_parking_space(parking_direction)
        with pytest.raises(ValueError):
            ps.create_parking_lot(parking_direction[0])


    # creating a successfult parking space
    def test_create_parking_lot(self):
        parking_direction = ['Create_parking_lot', '6']
        expected_output = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False}
        ps = self.build_parking_space(parking_direction)
        ps.create_parking_lot(parking_direction[1])
        self.assertEqual(ph.PARKING_SPACE, expected_output)


    # calling park using invalid command
    def test_park_with_invalid_direction(self):
        parking_direction = ['Create_parking_lot', '6']
        ps = self.build_parking_space(parking_direction)
        parking_direction = ['Park']
        with pytest.raises(IndexError):
            ps.park(parking_direction)


    # calling park using improper driver age
    def test_park_inproper_driver_age(self):
        parking_direction = ['Create_parking_lot', '6']
        ps = self.build_parking_space(parking_direction)
        parking_direction = ['Park', 'AA-02-BB-1111', 'driver_age', 'aa']
        with pytest.raises(ValueError):
            ps.park(parking_direction)

    
    # successful parking
    def test_park_inproper_driver_age(self):
        parking_direction = ['Create_parking_lot', '6']
        ps = self.build_parking_space(parking_direction)
        parking_direction = ['AA-02-BB-1111', 'driver_age', '25']
        ps.park(parking_direction)
        ps.leave('1')

    # leave invalid slot
    def test_leave(self):
        parking_direction = ['Create_parking_lot', '6']
        ps = self.build_parking_space(parking_direction)
        with pytest.raises(ValueError):
            ps.leave('aa')

    #test leave a slot
    def test_leave_slot(self):
        parking_direction = ['Create_parking_lot', '6']
        ps = self.build_parking_space(parking_direction)
        parking_direction = ['AA-02-BB-1111', 'driver_age', '25']
        ps.park(parking_direction)
        ps.leave('1')
        self.assertEqual(ph.PARKER_DETAILS, {})

    #invalid driver age
    def test_slot_numbers_for_driver_of_age(self):
        parking_direction = ['Create_parking_lot', '6']
        ps = self.build_parking_space(parking_direction)
        ps.slot_numbers_for_driver_of_age('27')
        with pytest.raises(KeyError):
            self.assertEqual(ph.AGE_SLOT_NUMBER['27'], {})

    
    #invalid car number slot
    def test_slot_number_for_car_with_number(self):
        parking_direction = ['Create_parking_lot', '6']
        ps = self.build_parking_space(parking_direction)
        ps.slot_number_for_car_with_number('27')
        with pytest.raises(KeyError):
            self.assertEqual(ph.REG_SLOT_NUMBER['27'], {})



    # if driver with age is not present car number slot
    def test_vehicle_registration_number_for_driver_of_age(self):
        parking_direction = ['Create_parking_lot', '6']
        ps = self.build_parking_space(parking_direction)
        ps.vehicle_registration_number_for_driver_of_age('27')
        with pytest.raises(KeyError):
            self.assertEqual(ph.REG_NUM_AGE['27'], {})
