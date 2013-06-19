'''
Created on 19 Mar 2013

@author: mgill
'''
import grass.script as grass
from geodigging.grass.ops.add_mapcalc_op import AddMapCalcOp

class ViewshedOp(object):
    '''
    classdocs
    '''


    def __init__(self, overwrite, dem, output, coordinate, obs_elev, 
                 max_dist, is_binary_output):
        '''
        Constructor
        '''
        self.overwrite = overwrite
        self.dem = dem
        self.output = output
        self.coordinate = coordinate
        self.obs_elev = obs_elev
        self.max_dist = max_dist
        self.is_binary_output = is_binary_output
        self.GRASS_COMMAND = 'r.los'
        
        
    def process(self):
        if self.is_binary_output:
            temp_raster_name = "temp_vw_viewshedop"
            self.run_command(temp_raster_name, True)
            add_mapcalc_op = AddMapCalcOp("", temp_raster_name, self.output)
            add_mapcalc_op.process()
        else:
            self.run_command(self.output, self.overwrite)
            
            
    def run_command(self, out_raster_name, overwrite_flag):
        grass.run_command(
           self.GRASS_COMMAND,
           overwrite = overwrite_flag,
           input = self.dem,
           output = out_raster_name,
           coordinate = self.coordinate,
           obs_elev = self.obs_elev,
           max_dist = self.max_dist
        )