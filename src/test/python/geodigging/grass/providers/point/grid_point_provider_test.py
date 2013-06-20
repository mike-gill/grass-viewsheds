'''
Created on 19 Mar 2013

@author: mgill
'''
import unittest
from geodigging.grass.providers.point.grid_point_provider import GridPointProvider
from geodigging.grass.geom.point import Point


class GridPointProviderTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_correct_points(self):
        origin_pt = Point(100, 100)
        rows = 3
        cols = 3
        cell_width = 5
        cell_height = 5
        expected_pt_list = [[100, 100], [105, 100], [110, 100],
                            [100, 105], [105, 105], [110, 105],
                            [100, 110], [105, 110], [110, 110]]
        
        provider = GridPointProvider(origin_pt, rows, cols, cell_width, cell_height)
        
        pt_list = []
        p = provider.next()
        while p:
            pt_list.append(p)
            p = provider.next()
            
        self.compare_pt_lists(expected_pt_list, pt_list)
        
        
    def compare_pt_lists(self, arr1, arr2):
        self.assertEquals(len(arr1), len(arr2), "List length")
        for i in range (len(arr1)):
            self.assertEquals(arr1[i][0], arr2[i][0])
            self.assertEquals(arr1[i][1], arr2[i][1])
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()