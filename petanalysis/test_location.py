import unittest  # Jupyter notebook
import location
from location import * 

class test_location(unittest.TestCase): # test class
    def setUp(self):
        print('Set up')

    def tearDown(self):
        print('Tear Down')

    @classmethod
    def setUpClass(cls):
        print('SetupClass')

    @classmethod
    def tearDownClass(cls):
        print('TearDownClass')

    def test_getShelter(self):
        self.assertEqual(location.get_shelter("AA125"), 'The postcode should not include character!')
        self.assertEqual(location.get_shelter("1234"), 'The postcode should be 5 digit number!')
        self.assertEqual(location.get_shelter("12345"), 'This is not a postcode in the US!')
        self.assertIsInstance(location.get_shelter("30101"), pd.core.frame.DataFrame)

unittest.main(argv=[''], verbosity=2, exit=False)
