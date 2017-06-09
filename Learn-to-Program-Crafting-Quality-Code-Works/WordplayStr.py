'''
Created on Apr 7, 2013

@author: Majid Hameed
'''

class WordplayStr(str):
    
    def same_start_and_end_with(self):
        '''(WordplayStr) -> bool
        
        Precondition: len(self) != 0
        
        Return True if start and end letter is same False otherwise
        
        >>> s = WordplayStr('abca')
        >>> s.same_start_and_end_with()
        True
        >>> s = WordplayStr('abcd')
        >>> s.same_start_and_end_with()
        False
        '''
        return self[0] == self[-1]
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
