'''
Created on Mar 31, 2013

@author: Majid Hameed
'''

def is_palindrome_v1(string):
    ''' (str) -> bool
    
    Returns True if and only if string is a palindrome.
    
    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('racecar')
    True
    >>> is_palindrome_v1('dented')
    False
    >>> is_palindrome_v1('tennis')
    False
    '''
    return string == reverse(string)


def reverse(string):
    ''' (str)->str
    
    Returns a reversed version of string
    >>> reverse('hello')
    olleh
    >>> reverse('ape')
    epa
    '''
    reverse_string = ''
    
    # For each character add that character at the beginning of reverse_string
    for ch in string:
        reverse_string = ch + reverse_string
    return reverse_string
     


def is_palindrome_v2(string):
    ''' (str) -> bool
    
    Returns True if and only if string is a palindrome.
    
    >>> is_palindrome_v2('noon')
    True
    >>> is_palindrome_v2('racecar')
    True
    >>> is_palindrome_v2('dented')
    False
    '''
    # no of chars in string
    n = len(string)
        
    # Compare the 1st half of s to the 2nd half of string
    # Omit the middle character of an odd-length string    
    return string[:n//2] == reverse(string[n-n//2:])
    
def is_palindrome_v3(string):
    ''' (str) -> bool
    
    Returns True if and only if string is a palindrome.
    
    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('dented')
    False
    '''
    
    i = 0
    j = len(string) -1
    while i < j and string[i] == string[j]:
        i = i + 1
        j = j - 1 
    return j <= i    
print (is_palindrome_v3('noon'))    
print (is_palindrome_v3('racecar'))
print (is_palindrome_v3('dented'))