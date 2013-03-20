'''
Created on 19 Mar 2013

@author: mgill
'''

class ListPointProvider(object):
    '''
    classdocs
    '''


    def __init__(self, point_list):
        '''
        Constructor
        '''
        self.index = 0
        self.point_list = point_list
        
    def next(self):
        if self.index == len(self.point_list):
            return None
        else:
            p = self.point_list[self.index]
            self.index = self.index + 1
            return p
        
    def reset(self):
        self.index = 0