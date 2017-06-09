'''
Created on Apr 14, 2013

@author: Majid Hameed
'''

def bubble_sort(L):
    """ (list)->NoneType
    Sorts the list using bubble sort algorithm
    
    >>> L=[7, 3, 5, 2]
    >>> bubble_sort(L)
    >>> L
    [2, 3, 5, 7]
    
    >>> L=[5, 4, 3, 2, 1]
    >>> bubble_sort(L)
    >>> L
    [1, 2, 3, 4, 5]
    
    >>> L=[2, 3, 5, 7]
    >>> bubble_sort(L)
    >>> L
    [2, 3, 5, 7]
    
    """
    
    start = 0
    end = len(L) - 1
    while end != 0:
        if L[start] > L[start + 1]:
            L[start], L[start+1] = L[start+1], L[start]
        
        start = start + 1
        
        if start == end:
            start = 0
            end = end - 1
            print(L)
    
if False and __name__ == '__main__':
    import doctest
    doctest.testmod()

bubble_sort([4, 2, 5, 6, 7, 3, 1])