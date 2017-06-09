import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    
    def test_swap_k_zero_swap(self):
        """ Test swap_k for k==0, any given List, L will remain as it is no swapping should take place"""
        L = [2, -4, 5, 0]
        expected = [2, -4, 5, 0]
        k = 0
        a1.swap_k(L, k)
        self.assertEqual(expected, L)
        
    def test_swap_k_zero_element_list(self):
        """ Test swap_k for k==0, empty List L, L will remain as it is no swapping should take place"""
        L = []
        expected = []
        k = 0
        a1.swap_k(L, k)
        self.assertEqual(expected, L)    
        
    def test_swap_k_one_element_list(self):
        """Test swap_k for List having only 1 element len(L) == 1 """
        L = [7]
        expected = [7]
        k = 1
        a1.swap_k(L, k)
        self.assertEqual(expected, L)
    
    def test_swap_k_1st_even_size_list_full_swap(self):
        """Test swap_k for List L such that len(L) == 2 i.e. first even number. Full swap should take place"""
        L = [9,5]
        expected = [5,9]
        k = 1
        a1.swap_k(L, k)
        self.assertEqual(expected, L)
        
    def test_swap_k_middlenumber_notswapped(self):
        """Test swap_k for the case where middle number not swapped"""
        L = [9,5,3]
        expected = [3,5,9]
        k = 1
        a1.swap_k(L, k)
        self.assertEqual(expected, L)
        
    def test_swap_k_full_swap(self):
        """ Test swap_k for the case all members for the given list swapped"""
        L = [1,2,3,4]
        expected = [3,4,1,2]
        k = 2
        a1.swap_k(L, k)
        self.assertEqual(expected, L)    
        
    def test_swap_middlelist_notswapped(self):
        "Test swap_k for the case where middle list not swapped"
        L = [1, 2, 3, 4, 5, 6]
        expected = [5, 6, 3, 4, 1, 2]
        k = 2
        a1.swap_k(L, k)
        self.assertEqual(expected, L)   
        

if __name__ == '__main__':
    unittest.main(exit=False)
