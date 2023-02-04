import unittest
from pandas.testing import assert_frame_equal
import assoc_rules
from assoc_rules import * 

class TestPaint(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        print("Testing Module assoc rules")
        #lh.info("starting class: {} execution".format(cls.__name__))
        
    def setUp(self):
        print("Setting up Unit Test")
        self.filename = "Dog Data all.csv"
        self.df = read_data_file("Dog Data all.csv")
        self.pets_data_df = file_data_wrangle(df)
        self.min_supp = 0.1
        self.min_conf = 0.8
        self.sortby = 'lift'
        self.rowcount = 25
        self.rules = assoc_rules(pets_data_df, 0.1, 0.8, 'lift', 25)
        
    def tearDown(self):
        print("Execution ended for given Unit test")
    
    def test_read_data_file(self, filename): 
        self.assertIsNone(read_data_file(self,self.filename))
        
    def test_Paint_file_data_wrangle(self): # test routine
        self.assertIsNone(file_data_wrangle(self,self.df))
        
    def test_Paint_file_data_wrangle(self): # test routine
        self.assert_frame_equal(assoc_rules(self,self.pets_data_df,self.min_supp, self.min_conf, self.sortby, self.rowcount), self.rules)

        
    @classmethod 
    def teardown_class(cls):
        print("Ending Testing for Module Paint from Sudoku Show")
        #lh.info("ending class: {} execution".format(cls.__name__))
        

if __name__ == "__main__":
    unittest.main()