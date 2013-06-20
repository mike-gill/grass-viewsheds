'''
Created on 19 Jun 2013

@author: mgill
'''
import csv
from geodigging.grass.geom.point import Point

class CsvPointProvider(object):
    '''
    classdocs
    '''


    def __init__(self, file_obj, xfield_idx, yfield_idx, idfield_idx, 
                 skip_first_row=True, delimiter=",", quotechar='"'):
        '''
        Constructor
        '''
        self.file_ob = file_obj
        self.xfield_idx = xfield_idx
        self.yfield_idx = yfield_idx
        self.idfield_idx = idfield_idx
        self.skip_first_row = skip_first_row
        self.csv_reader = csv.reader(file_obj, delimiter=delimiter, 
                                     quotechar=quotechar)
        if skip_first_row: self.csv_reader.next()
    
    def next(self):
        row = self.csv_reader.next()
        if not row: return None
        return Point(float(row[self.xfield_idx]),
                     float(row[self.yfield_idx]),
                     row[self.idfield_idx])
        
        
        
        
        
        