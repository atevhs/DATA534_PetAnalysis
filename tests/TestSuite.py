from testcases.test_assoc_rules import TestAssocRules as tAR
from testcases.test_location import test_location as tL
from testcases.test_plot import test_plot as tP
import unittest

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(tAR))
    suite.addTest(unittest.makeSuite(tL))
    suite.addTest(unittest.makeSuite(tP))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
    
my_suite()