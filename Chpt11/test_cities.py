import unittest
from city_function import get_city_country

class citiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formmated_info= get_city_country('santiago', 'chile')
        self.assertEqual(formmated_info, 'Santiago, Chile')

if __name__ =='__main__':
    unittest.main()

