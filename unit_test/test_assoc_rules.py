import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../petanalysis/")
import assoc_rules as ar 

class TestAssocRules(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        print("Testing Module assoc rules")
        #lh.info("starting class: {} execution".format(cls.__name__))
        
    def setUp(self):
        print("Setting up Unit Test")
        self.filename = "petanalysis/Dog Data all.csv"
        self.df = ar.read_data_file(self.filename)
        self.pets_data_df = ar.file_data_wrangle(self.df)
        self.min_supp = 0.1
        self.min_conf = 0.8
        self.sortby = 'lift'
        self.rowcount = 25
        self.rules = ar.assoc_rules(self.pets_data_df, 0.1, 0.8, 'lift', 25)
        
    def tearDown(self):
        print("Execution ended for given Unit test")
    
    def test_read_data_file(self): 
        df1 = ar.read_data_file(self.filename)
        df2 = self.df
        self.assertEqual(True, df1.equals(df2))
        
    def test_Paint_file_data_wrangle(self): # test routine
        df1 = ar.file_data_wrangle(self.df)
        df2 = self.pets_data_df
        self.assertEqual(True, df1.equals(df2))
        
    def test_Paint_file_data_wrangle(self): # test routine
        df1 = ar.assoc_rules(self.pets_data_df,self.min_supp, self.min_conf, self.sortby, self.rowcount)
        df2 = self.rules
        self.assertEqual(True, df1.equals(df2))
        #self.assert_frame_equal(assoc_rules(self.pets_data_df,self.min_supp, self.min_conf, self.sortby, self.rowcount), self.rules)

        
    @classmethod 
    def teardown_class(cls):
        print("Ending Testing for Module Assoc rules for Pet Analysis")
        #lh.info("ending class: {} execution".format(cls.__name__))
        

if __name__ == "__main__":
    unittest.main()
