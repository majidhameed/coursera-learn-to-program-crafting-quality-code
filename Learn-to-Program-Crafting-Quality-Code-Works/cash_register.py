'''
Created on Apr 16, 2013

@author: Majid Hameed
'''


class CashRegister:
    '''A cash register'''
    
    def __init__(self, loonies, toonies, fives, tens, twenties):
        """ (CashRegister, int, int, int, int, int) -> NoneType

        A CashRegister with loonies, toonies, fives, tens, and twenties.
        
        >>> register = CashRegister(5, 5, 5, 5, 5)
        >>> register.loonies
        5
        >>> register.toonies
        5
        >>> register.fives
        5
        >>> register.tens
        5
        >>> register.twenties
        5
        """
        self.loonies = loonies
        self.toonies = toonies
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
        
        
    def __str__(self):
        """ (CashRegister) -> str
        Return a string representation of this CashRegister.
        >>> reg1 = CashRegister(1, 2, 3, 4, 5)
        CashRegister: $160 ($1x1, $2x2, $5x3, $10x4, $20x5)
        """    
        
        '''
        return 'CashRegister: $' + str(self.get_total()) + ' ($1x' + str(self.loonies) + \
            ', $2x' + str(self.toonies) + ', $5x' + str(self.fives) + ', $10x' + \
            str(self.tens) + ', $20x' + str(self.twenties) + ')'
        OR    
        '''
        
        return "CashRegister: " + \
            "${0} ($1x{1}, $2x{2}, $5x{3}, $10x{4}, $20x{5})".format(self.get_total(), self.loonies, self.toonies, self.fives, self.tens, self.twenties)   
        
    def __eq__(self, other):
        """ (CashRegister, CashRegister) -> bool

        Return True iff this CashRegister has the same amount of money as other.
        
        >>> reg1 = CashRegister(2, 0, 0, 0, 0)
        >>> reg2 = CashRegister(0, 1, 0, 0, 0)
        >>> reg1 == reg2
        True
        """
        return self.get_total() == other.get_total()
    
    
    def get_total(self):
        """ (CashRegister) -> int

        Return the total amount of cash in the register.
        
        >>> register = CashRegister(5, 5, 5, 5, 5)
        >>> register.get_total()
        190
        """
        return self.loonies + 2 * self.toonies + 5 * self.fives \
            + 10 * self.tens + 20 * self.twenties
    
    def add(self, count, denomination):
        """ (CashRegister, int, str) -> NoneType

        Add count items of denomination to the register.
        denomination is one of 'loonies', 'toonies',
        'fives', 'tens', and 'twenties'.
        
        >>> register = CashRegister(5, 5, 5, 5, 5)
        >>> register.add(2, 'toonies')
        >>> register.toonies
        7
        >>> register.add(1, 'tens')
        >>> register.tens
        6
        """
        if denomination == 'loonies':
            self.loonies += count
        elif denomination == 'toonies':
            self.toonies += count
        elif denomination == 'fives':
            self.fives += count
        elif denomination == 'tens':
            self.tens += count
        elif denomination == 'twenties':                         
            self.twenties += count

    
    def remove(self, count, denomination):
        """ (CashRegister, int, str) -> NoneType

        Remove count items of denomination from the register.
        denomination is one of 'loonies', 'toonies',
        'fives', 'tens', and 'twenties'.
        
        >>> register = CashRegister(5, 5, 5, 5, 5)
        >>> register.remove(2, 'toonies')
        >>> register.toonies
        3
        >>> register.remove(1, 'tens')
        >>> register.tens
        4
        """
        if denomination == 'loonies':
            self.loonies -= count
        elif denomination == 'toonies':
            self.toonies -= count
        elif denomination == 'fives':
            self.fives -= count
        elif denomination == 'tens':
            self.tens -= count
        elif denomination == 'twenties':                         
            self.twenties -= count
        

if __name__ == '__main__':
    # A cash register with 5 loonies, 5 toonies, 5 fives, 5 tens, and 5 twenties,
    # for a total of $190.
    register = CashRegister(5, 5, 5, 5, 5)
    print(register.get_total())
    
    register.add(3, 'toonies')
    print(register.get_total())
    
    register.remove(2, 'twenties')
    print(register.get_total())
    
    cr1 = CashRegister(2, 0, 0, 0, 0)
    cr2 = CashRegister(0, 1, 0, 0, 0)
    cr3 = CashRegister(1, 1, 0, 0, 0)
    print (cr1)
    print (cr2)
    
    print (cr1 == cr2)
    print (cr2 == cr3)    
