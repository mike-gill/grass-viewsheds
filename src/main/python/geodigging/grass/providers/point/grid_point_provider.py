'''
Created on 19 Mar 2013

@author: mgill
'''

class GridPointProvider(object):
    '''
    classdocs
    '''


    def __init__(self, origin_point, rows, cols, cell_width, cell_height):
        '''
        Constructor
        '''
        self.origin_point = origin_point
        self.rows = rows
        self.cols = cols
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.row = 0
        self.col = 0
        
    def next(self):
        if self.col >= self.cols:
            self.col = 0
            self.row = self.row + 1
        if self.row < self.rows:
            pt = [self.origin_point.x + (self.col * self.cell_width),
                  self.origin_point.y + (self.row * self.cell_height)]
            self.col = self.col + 1
            return pt
        else:
            return None