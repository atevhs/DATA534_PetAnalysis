import unittest
from pandas.testing import assert_frame_equal
import assoc_rules
from assoc_rules import * 

class TestAssocRules(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        print("Testing Module assoc rules")
        #lh.info("starting class: {} execution".format(cls.__name__))
        
    def setUp(self):
        print("Setting up Unit Test")
        self.filename = "Dog Data all.csv"
        self.df = read_data_file(self.filename)
        self.pets_data_df = file_data_wrangle(self.df)
        self.min_supp = 0.1
        self.min_conf = 0.8
        self.sortby = 'lift'
        self.rowcount = 25
        self.rules = assoc_rules(self.pets_data_df, 0.1, 0.8, 'lift', 25)
        
    def tearDown(self):
        print("Execution ended for given Unit test")
    
    def test_read_data_file(self): 
        df1 = read_data_file(self.filename)
        df2 = self.df
        self.assertEqual(True, df1.equals(df2))
        
    def test_Paint_file_data_wrangle(self): # test routine
        df1 = file_data_wrangle(self.df)
        df2 = self.pets_data_df
        self.assertEqual(True, df1.equals(df2))
        
    def test_Paint_file_data_wrangle(self): # test routine
        df1 = assoc_rules(self.pets_data_df,self.min_supp, self.min_conf, self.sortby, self.rowcount)
        df2 = self.rules
        self.assertEqual(True, df1.equals(df2))
        #self.assert_frame_equal(assoc_rules(self.pets_data_df,self.min_supp, self.min_conf, self.sortby, self.rowcount), self.rules)

        
    @classmethod 
    def teardown_class(cls):
        print("Ending Testing for Module Paint from Sudoku Show")
        #lh.info("ending class: {} execution".format(cls.__name__))
        

if __name__ == "__main__":
    unittest.main()
