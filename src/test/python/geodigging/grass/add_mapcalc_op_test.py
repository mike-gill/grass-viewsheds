'''
Created on 6 Aug 2013

@author: mgill
'''
import unittest
from geodigging.grass.ops.add_mapcalc_op import AddMapCalcOp
from mock import MagicMock, patch, call


class AddMapCalcOpTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_handle_original_map(self):
        add_mapcalc_op = AddMapCalcOp("orig_map", "test_map_to_add", "test_out")
        add_mapcalc_op._process_with_orig_map = MagicMock(name='_process_with_orig_map')
        add_mapcalc_op.process()
        
        add_mapcalc_op._process_with_orig_map.assert_called_once_with()
        

    def test_handle_without_original_map(self):
        add_mapcalc_op = AddMapCalcOp("", "test_map_to_add", "test_out")
        add_mapcalc_op._process_without_orig_map = MagicMock(name='_process_without_orig_map')
        add_mapcalc_op.process()
        
        add_mapcalc_op._process_without_orig_map.assert_called_once_with()  
        

    @patch('geodigging.grass.ops.add_mapcalc_op.grass')
    def test_process_with_orig_map(self, mock_grass):
        """Tests grass is correctly called when original map exists
        
        Tests grass mapcalc method is correctly called from within
        the AddMapCalcOp class.  Note that the patch decorator for this
        method patches grass.script (imported in module under test as grass).
        It is also possible to just patch a method on grass script as follows:
        
        @patch('grass.script.mapcalc')
        def test_process_with_orig_map(self, mock_mapcalc_method):
            add_mapcalc_op = AddMapCalcOp("orig_map", "test_map_to_add", "test_out")
            add_mapcalc_op.process()
            print mock_mapcalc_method.mock_calls
        
        """
        
        add_mapcalc_op = AddMapCalcOp("orig_map", "test_map_to_add", "test_out")
        add_mapcalc_op.process()
        expected = [call.mapcalc('$out_map = $original_map + !isnull($map_to_add)', 
                                 out_map='test_out', 
                                 map_to_add='test_map_to_add', 
                                 overwrite=True, 
                                 original_map='orig_map')]
        self.assertEqual(expected, mock_grass.mock_calls)
        
        
    @patch('geodigging.grass.ops.add_mapcalc_op.grass')
    def test_process_without_orig_map(self, mock_grass):
        
        add_mapcalc_op = AddMapCalcOp("", "test_map_to_add", "test_out")
        add_mapcalc_op.process()
        expected = [call.mapcalc('$out_map = !isnull($map_to_add)', 
                                 out_map='test_out', 
                                 map_to_add='test_map_to_add', 
                                 overwrite=True)]
        self.assertEqual(expected, mock_grass.mock_calls)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()