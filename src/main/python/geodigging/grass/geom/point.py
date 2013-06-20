'''
Created on 19 Mar 2013

@author: mgill
'''

class Point(object):
    '''
    classdocs
    '''


    def __init__(self, x, y, fid=None):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
        self.fid = fid
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
