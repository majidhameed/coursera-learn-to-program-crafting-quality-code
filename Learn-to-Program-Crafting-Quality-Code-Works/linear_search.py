'''
Created on Apr 14, 2013

@author: Majid Hameed
'''

def linear_search(L, v):
    """ (list, object) -> int

    Return the index of the first occurrence of v in L, or
    return -1 if v is not in L.

    >>> linear_search([2, 3, 5, 3], 2)
    0
    >>> linear_search([2, 3, 5, 3], 5)
    2
    >>> linear_search([2, 3, 5, 3], 8)
    -1
    >>> linear_search([2, 3, 5, 8], 8)
    3
    """
    
    i = 0
    length = len(L) 
    while i != length and v != L[i]:
        i = i + 1
   
    print(i)
    
    if i == length:
        return -1
    else:
        return i

if False and __name__ == "__main__":
    import doctest
    doctest.testmod()
    

linear_search([7, 6, 5, 4, 3, 2], 7)