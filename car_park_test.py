import unittest
# import car_park
from car_park import CarPark

class CarParkInitTest(unittest.TestCase):
  def test_car_park_class_can_be_instantiated(self):
    spaces = 0
    new_car_park = CarPark(spaces)
    self.assertIsInstance(new_car_park, CarPark)

  def test_when_CarPark_is_instantiated_there_are_available_spaces(self):
    spaces = 50
    new_car_park = CarPark(spaces)
    expected_spaces = spaces
    actual_spaces = new_car_park.spaces
    self.assertEqual(50, new_car_park.spaces)


if __name__ == '__main__':
  unittest.main(verbosity=2)
