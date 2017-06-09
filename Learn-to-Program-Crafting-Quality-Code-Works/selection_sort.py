'''
Created on Apr 14, 2013

@author: Majid Hameed
'''

def selection_sort(L):
    """ (list)->NoneType
    Sorts the list using selection sort algorithm
    
    >>> L=[7, 3, 5, 2]
    >>> selection_sort(L)
    >>> L
    [2, 3, 5, 7]
    
    >>> L=[5, 4, 3, 2, 1]
    >>> selection_sort(L)
    >>> L
    [1, 2, 3, 4, 5]
    
    >>> L=[2, 3, 5, 7]
    >>> selection_sort(L)
    >>> L
    [2, 3, 5, 7]
    
    """
    
    start = 0
    end = len(L) - 1
    current_index = 0
    index_of_smallest = current_index
    
    while start != end:
        
        if L[index_of_smallest] > L[current_index]:
            index_of_smallest = current_index
        
        if current_index == end:
            L[start], L[index_of_smallest] = L[index_of_smallest], L[start]
            start = start + 1
            current_index = start
            index_of_smallest = current_index
            print(L)
            
        current_index = current_index + 1
        
if False and __name__ == '__main__':
    import doctest
    doctest.testmod()

selection_sort([1, 5, 8, 7, 6, 1, 7])