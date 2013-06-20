'''
Created on 19 Mar 2013

@author: mgill
'''

from geodigging.grass.ops.viewshed_op import ViewshedOp

class ViewshedProcessor(object):
    '''
    classdocs
    '''


    def __init__(self, dem, point_provider, obs_elev, max_dist, prefix=""):
        '''
        Constructor
        '''
        self.dem = dem
        self.point_provider = point_provider
        self.obs_elev = obs_elev
        self.max_dist = max_dist
        self.prefix = prefix
        
    def process(self):
        p = self.point_provider.next()
        while p:
            # Create and run viewshed
            viewshed_op = ViewshedOp(True, self.dem, self.prefix + p.fid, 
                                     [p.x, p.y], self.obs_elev, self.max_dist, False)
            viewshed_op.process()
            p = self.point_provider.next()

            
            
            
            
        