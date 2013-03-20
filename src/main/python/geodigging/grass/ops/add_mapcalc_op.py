'''
Created on 19 Mar 2013

@author: mgill
'''
import grass.script as grass

class AddMapCalcOp(object):
    '''
    classdocs
    '''

    def __init__(self, original_map, map_to_add, out_map):
        '''
        Constructor
        '''
        self.original_map = original_map
        self.map_to_add = map_to_add
        self.out_map = out_map
        
        
    def process(self):
        if self.original_map == "":
            self._process_without_orig_map()
        else:
            self._process_with_orig_map()
            
        
    def _process_with_orig_map(self):
        #grass.mapcalc("$out_map = if($original_map, 0) + if($map_to_add, 0)",
        grass.mapcalc("$out_map = $original_map + !isnull($map_to_add)",
                      overwrite=True, 
                      original_map = self.original_map,
                      map_to_add = self.map_to_add, 
                      out_map = self.out_map)
        
    def _process_without_orig_map(self):
        #grass.mapcalc("$out_map = if($map_to_add)",
        grass.mapcalc("$out_map = !isnull($map_to_add)",
                      overwrite=True, 
                      map_to_add = self.map_to_add, 
                      out_map = self.out_map)
