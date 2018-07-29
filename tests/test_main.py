"""
to run tests: 
C:\ProgramData\Anaconda3\python.exe -m unittest discover -s tests -p 'test*.py'
"""

import pathlib
import unittest
import sys
import pandas as pd
from pandas.util.testing import assert_frame_equal

from main import test_function

path = str(pathlib.Path(__file__).parents[1]) # generate path to parent dir
if path not in sys.path:
    sys.path.append(path)

class Test_main(unittest.TestCase):

    def test_test_function(self):
        # import end result to test against
        path = str(pathlib.Path(__file__).parents[1]) # generates path to proj_etd
        test_filepath = ''
        test = pd.read_csv(test_filepath)
        
        # generate file using imported function
        check_raw_filepath = ''
        check_raw = pd.read_csv(check_raw_filepath)
        check = test_function(check_raw)
        
        # test
        assert_frame_equal(test, check)
        
if __name__ == '__main__':
    unittest.main()
