import os
import sys
import unittest as ut
from unittest.mock import patch
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../petanalysis/")
import plot as dogplt

class test_plot(ut.TestCase):
    @classmethod
    def setup_class(cls):
        print("Testing plot module:")
    
    def setUp(self):
        print("setup unit test.")
        self.dogs = pd.read_csv("petanalysis/Dog Data all.csv")
    
    def tearDown(self):
        print("Teardown unit test.")
    
    def test_age_historgram(self):
        with patch("plot.plt.show") as show_patch:
            dogplt.age_histogram(self.dogs)
            assert show_patch.called
            
    def test_size_heatmap(self):
        with patch("plot.plt.show") as show_patch:
            dogplt.size_heatmap(self.dogs)
            assert show_patch.called

    @classmethod
    def tearDownClass(cls):
        print('Plot testing completed.')

ut.main(argv=[''], verbosity=2, exit=False)