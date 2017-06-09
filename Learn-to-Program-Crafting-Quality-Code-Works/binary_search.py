'''
Created on Apr 14, 2013

@author: Majid Hameed
'''
def binary_search(L, v):
    """ (list, object) -> int

    Precondition: L is sorted from smallest to largest, and
    all the items in L can be compared to v.

    Return the index of the first occurrence of v in L, or
    return -1 if v is not in L.

    >>> binary_search([2, 3, 5, 7], 2)
    0
    >>> binary_search([2, 3, 5, 5], 5)
    2
    >>> binary_search([2, 3, 5, 7], 8)
    -1
    >>> binary_search([2, 3, 5, 8], 8)
    3
    """
    left = 0
    right = len(L) - 1
    
    while left <= right:
        middle = (left + right) // 2
        
        if L[middle] < v:
            left = middle + 1
        else:     
            right = middle - 1
    
    if left == len(L) or L[left] != v:
        return -1
    else:
        return left
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
