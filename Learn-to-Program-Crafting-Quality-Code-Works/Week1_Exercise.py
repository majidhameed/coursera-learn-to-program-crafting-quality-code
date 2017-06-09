'''
Created on Apr 1, 2013

@author: Majid Hameed
'''

def is_palindrome_v3(s):     
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('dented')
    False
    """
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i]:
            return False

    return True
print (is_palindrome_v3('noon'),is_palindrome_v3('racecar'),is_palindrome_v3('a'), is_palindrome_v3('aba'), is_palindrome_v3('aa'))
print (is_palindrome_v3('dented'),is_palindrome_v3('ap'),is_palindrome_v3('cap'))    