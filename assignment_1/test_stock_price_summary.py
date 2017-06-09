import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_no_loss_no_gain(self):
        """ Test for no loss no gain for 1 info only """
        expected = (0, 0)
        actual = a1.stock_price_summary([0])
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_no_info_at_all(self):
        """ Test for no given no information that is empty list given"""
        expected = (0, 0)
        actual = a1.stock_price_summary([])
        self.assertEqual(expected, actual)    
    
    def test_stock_price_summary_integers_gains(self):
        """Test stock_price_summary for integer list of gains only"""
        expected = (6, 0)
        actual = a1.stock_price_summary([1,2,3])
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_integers_losses(self):
        """Test stock_price_summary for integer list of losses only"""
        expected = (0, -6)
        actual = a1.stock_price_summary([-1,-2,-3])
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_integers(self):
        """Test stock_price_summary for gains and losses in integer list"""
        expected = (11.0, -7.0)
        actual = a1.stock_price_summary([3, 6,-3, 2,-4])
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_losses(self):
        """Test stock_price_summary for losses only"""
        expected = (0.0, -0.75)
        actual = a1.stock_price_summary([-0.3,-0.4,-0.05])
        self.assertEqual(expected, actual)
    
    def test_stock_price_summary_gains(self):
        """Test stock_price_summary for gains only"""
        expected = (1.0, 0.0)
        actual = a1.stock_price_summary([0.5,0.4,0.005,0.095])
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_losses_gains(self):
        """Test stock_price_summary for gains and losses"""
        expected = (0.14, -0.17)
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        self.assertEqual(expected, actual)
    
if __name__ == '__main__':
    unittest.main(exit=False)
