import math

def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    >>> num_buses(1)
    1
    >>> num_buses(50)
    1
    >>> num_buses(51)
    2
    >>> num_buses(0)
    0
    """
    return math.ceil(n/50)
    

def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    
    >>> stock_price_summary([1,2,3])
    (6.0, 0.0)
    
    >>> stock_price_summary([-1,-2,-3])
    (0.0, -6.0)
    
    >>> stock_price_summary([3, 6,-3, 2,-4])
    (11.0, -7.0)
    
    >>> stock_price_summary([-0.3,-0.4,-0.05])
    (0.0, -0.75)
    
    >>> stock_price_summary([0.5,0.4,0.005,0.095])
    (1.0, 0.0)
    
    >>> stock_price_summary([0])
    (0.0, 0.0)
    
    >>> stock_price_summary([])
    (0.0, 0.0)
    """
    gain=0;
    loss=0;
    for price in price_changes:
        if price < 0:
            loss = loss + price
        else:
            gain = gain + price
    return float(gain), float(loss)
             
def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """
    if k>0 and k <= len(L) // 2:
        l1 = L[:k]
        l2 = L[-k:]
        l3 = L[k:-k]
        
        L[:k]   = l2
        L[-k:]  = l1
        L[k:-k] = l3
     
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
