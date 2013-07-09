'''
Created on 19 Mar 2013

@author: mgill
'''
from geodigging.grass.providers.point.list_point_provider import ListPointProvider
from geodigging.grass.viewshed_adder import ViewshedAdder
from geodigging.grass.viewshed_processor import ViewshedProcessor
from geodigging.grass.providers.point.grid_point_provider import GridPointProvider
from geodigging.grass.geom.point import Point
from geodigging.grass.providers.point.csv_point_provider import CsvPointProvider
 
def add_views_specific_pts():
    dem = 'avon_valley_dem_50m'
    output = 'test_vw_03_13'
    obs_elev = 2
    max_dist = 10000
    point_list = [
                    Point(408329, 120585),
                    Point(406380, 120600)
                 ]
    point_provider = ListPointProvider(point_list)
    viewshed_adder = ViewshedAdder(dem, output, point_provider, obs_elev, max_dist)
    viewshed_adder.process()
    
def add_views_grid_pts():
    dem = 'avon_valley_dem_50m'
    output = 'cumul_vw_rockbourne3'
    obs_elev = 2
    max_dist = 2000
    point_provider = GridPointProvider(Point(406000, 119000), 4, 4, 50, 50)
    viewshed_adder = ViewshedAdder(dem, output, point_provider, obs_elev, max_dist)
    viewshed_adder.process()
    
def add_views_csv_pts():
    dem = 'avon_valley_dem_50m'
    output = 'cumul_vw_long_barrows_rockbourne_2km'
    obs_elev = 2
    max_dist = 2000
    csvfile = open(r'C:\Users\mgill\archaeology\AVAS\gisdata\barrows\long_barrows_study_area.csv')
    point_provider = CsvPointProvider(csvfile, 11, 12, 1)
    viewshed_adder = ViewshedAdder(dem, output, point_provider, obs_elev, max_dist)
    viewshed_adder.process()
    
def process_specific_pts():
    dem = 'avon_valley_dem_50m'
    obs_elev = 2
    max_dist = 10000
    point_list = [
                    Point(408329, 120585, "test1"),
                    Point(406380, 120600, "test2")
                 ]
    point_provider = ListPointProvider(point_list)
    viewshed_processor = ViewshedProcessor(dem, point_provider, obs_elev, max_dist, "vw_")
    viewshed_processor.process()
    
if __name__ == '__main__':
    #add_views_specific_pts()
    #add_views_grid_pts()
    add_views_csv_pts()
    #process_specific_pts()