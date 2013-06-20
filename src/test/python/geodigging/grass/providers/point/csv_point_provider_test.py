'''
Created on 20 Jun 2013

@author: mgill
'''
import unittest
from cStringIO import StringIO
from geodigging.grass.providers.point.csv_point_provider import CsvPointProvider
from geodigging.grass.geom.point import Point


class CsvPointProviderTest(unittest.TestCase):


    def setUp(self):
        self.csv_string = (
        'id,x,y\n' +
        '1,10,11\n' + 
        '2,20,21')
        
        self.csv_string_no_header = (
        '1,10,11\n' + 
        '2,20,21')

        self.pipe_string = (
        'id|x|y\n' +
        '1|10|11\n' + 
        '2|20|21')
        
        self.csv_string_dollar_quote_char = (
        'id,x,y\n' +
        '1,10,11\n' + 
        '$a,b$,20,21')


    def tearDown(self):
        pass


    def test_csv_with_header(self):
        file_obj = StringIO(self.csv_string)
        provider = CsvPointProvider(file_obj, 1, 2, 0)
        self.assertEqual(Point(10,11,"1"),provider.next(), "First point")
        self.assertEqual(Point(20,21,"2"),provider.next(), "Second point")
        
        
    def test_csv_without_header(self):
        file_obj = StringIO(self.csv_string_no_header)
        provider = CsvPointProvider(file_obj, 1, 2, 0, skip_first_row=False)
        self.assertEqual(Point(10,11,"1"),provider.next(), "First point")
        self.assertEqual(Point(20,21,"2"),provider.next(), "Second point")
        
        
    def test_csv_with_pipe_separator(self):
        file_obj = StringIO(self.pipe_string)
        provider = CsvPointProvider(file_obj, 1, 2, 0, delimiter='|')
        self.assertEqual(Point(10,11,"1"),provider.next(), "First point")
        self.assertEqual(Point(20,21,"2"),provider.next(), "Second point")
        
        
    def test_csv_with_dollar_quote_char(self):
        file_obj = StringIO(self.csv_string_dollar_quote_char)
        provider = CsvPointProvider(file_obj, 1, 2, 0, quotechar='$')
        self.assertEqual(Point(10,11,"1"),provider.next(), "First point")
        self.assertEqual(Point(20,21,"a,b"),provider.next(), "Second point")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_valid_csv']
    unittest.main()