'''
Created on 19 Mar 2013

@author: mgill
'''
import grass.script as grass

class CopyOp(object):
    '''
    classdocs
    '''


    def __init__(self, from_rast, to_rast, overwrite):
        '''
        Constructor
        '''
        self.overwrite = overwrite
        self.from_rast = from_rast
        self.to_rast = to_rast
        self.GRASS_COMMAND = 'g.copy'
        
    def process(self):
        grass.run_command(
           self.GRASS_COMMAND,
           overwrite = self.overwrite,
           rast = "%s,%s" % (self.from_rast, self.to_rast)
        )
        