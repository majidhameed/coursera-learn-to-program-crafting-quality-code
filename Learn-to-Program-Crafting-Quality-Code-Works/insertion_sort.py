'''
Created on Apr 15, 2013

@author: Majid Hameed
'''

def insertion_sort(L):
    """ (list)->NoneType
    Sorts the list using insertion sort algorithm
    
    >>> L=[7, 3, 5, 2]
    >>> insertion_sort(L)
    >>> L
    [2, 3, 5, 7]
    
    >>> L=[5, 4, 3, 2, 1]
    >>> insertion_sort(L)
    >>> L
    [1, 2, 3, 4, 5]
    
    >>> L=[2, 3, 5, 7]
    >>> insertion_sort(L)
    >>> L
    [2, 3, 5, 7]
    
    """
    for i in range(len(L)):
        insert(L, i)
        
def insert(L, index):
    start = index
    while start != 0:
        if L[start] < L[start - 1]:
            L[start], L[start - 1] = L[start - 1], L[start]
            
        start = start - 1
        
if False and __name__ == '__main__':
    import doctest
    doctest.testmod()