'''
Created on 19 Mar 2013

@author: mgill
'''
from geodigging.grass.providers.point.list_point_provider import ListPointProvider
from geodigging.grass.viewshed_adder import ViewshedAdder
from geodigging.grass.providers.point.grid_point_provider import GridPointProvider
from geodigging.grass.geom.point import Point


    
def process_specific_pts():
    dem = 'avon_valley_dem_50m'
    output = 'test_vw_03_13'
    obs_elev = 2
    max_dist = 10000
    point_list = [
                    [408329, 120585],
                    [406380, 120600]
                 ]
    point_provider = ListPointProvider(point_list)
    viewshed_adder = ViewshedAdder(dem, output, point_provider, obs_elev, max_dist)
    viewshed_adder.process()
    
def process_grid_pts():
    dem = 'avon_valley_dem_50m'
    output = 'cumul_vw_rockbourne3'
    obs_elev = 2
    max_dist = 2000
    point_provider = GridPointProvider(Point(406000, 119000), 4, 4, 50, 50)
    viewshed_adder = ViewshedAdder(dem, output, point_provider, obs_elev, max_dist)
    viewshed_adder.process()
    
if __name__ == '__main__':
    #process_specific_pts()
    process_grid_pts()