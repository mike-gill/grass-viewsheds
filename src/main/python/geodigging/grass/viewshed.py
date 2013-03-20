'''
Created on 19 Mar 2013

@author: mgill
'''
import grass.script as grass

class ViewshedOp(object):
    '''
    classdocs
    '''


    def __init__(self, overwrite, dem, output, coordinate, obs_elev, max_dist):
        '''
        Constructor
        '''
        self.overwrite = overwrite
        self.dem = dem
        self.output = output
        self.coordinate = coordinate
        self.obs_elev = obs_elev
        self.max_dist = max_dist
        self.GRASS_COMMAND = 'r.los'
        
    def process(self):
        grass.run_command(
           self.GRASS_COMMAND,
           overwrite = self.overwrite,
           input = self.dem,
           output = self.output,
           coordinate = self.coordinate,
           obs_elev = self.obs_elev,
           max_dist = self.max_dist
        )
        