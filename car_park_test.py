import unittest
# import car_park
from car_park import CarPark

class CarParkInitTest(unittest.TestCase):
  def test_car_park_class_has_init_method(self):
    new_car_park = CarPark()
    self.assertIsInstance(new_car_park, CarPark)

if __name__ == '__main__':
  unittest.main(verbosity=2)
