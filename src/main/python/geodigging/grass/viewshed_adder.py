'''
Created on 19 Mar 2013

@author: mgill
'''

from geodigging.grass.ops.viewshed_op import ViewshedOp
from geodigging.grass.ops.add_mapcalc_op import AddMapCalcOp
from geodigging.grass.ops.copy_op import CopyOp

class ViewshedAdder(object):
    '''
    classdocs
    '''


    def __init__(self, dem, output, point_provider, obs_elev, max_dist):
        '''
        Constructor
        '''
        self.dem = dem
        self.output = output
        self.point_provider = point_provider
        self.obs_elev = obs_elev
        self.max_dist = max_dist
        
    def process(self):
        #temp_output = "tmp" + self.output
        temp_mapcalc = "tmpmc" + self.output
        vw_output = "tmp" + self.output
        n = 0
        sum_map = ""
        p = self.point_provider.next()
        while p:
            # Create and run viewshed
            viewshed_op = ViewshedOp(True, self.dem, vw_output, p, self.obs_elev, self.max_dist)
            viewshed_op.process()
            
            # Add result to main output
            add_mapcalc_op = AddMapCalcOp(sum_map, vw_output, temp_mapcalc)
            add_mapcalc_op.process()
            copy_op = CopyOp(temp_mapcalc, self.output, True)
            copy_op.process()
            sum_map = self.output
            
            
#            if n == 0:
#                target = temp_output
#            else:
#                # Add result to main output
#                add_mapcalc_op = AddMapCalcOp(self.output, temp_output, temp_mapcalc)
#                add_mapcalc_op.process()
#                copy_op = CopyOp(temp_mapcalc, self.output, True)
#                copy_op.process()
            p = self.point_provider.next()
            n = n + 1
            
            
            
            
        