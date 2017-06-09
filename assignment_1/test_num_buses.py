import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """
    
    # Add your test methods for a1.num_buses here.
    
    def test_num_buses_zero_persons(self):
        """Test num_buses for Zero person. To check Zero person needs Zero buses"""
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_num_buses_one_person(self):
        """Test num_buses for 1 person"""
        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(expected, actual)
        
    def test_num_buses_fifty_persons(self):
        """Test num_buses for fifty persons"""
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(expected, actual)
        
    def test_num_buses_fiftyone_persons(self):
        """Test num_buses for fifty one persons"""
        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(expected, actual)
   
    def test_num_buses_fivehundred_persons(self):
        """Test num_buses for five hundred and fifty five persons"""
        actual = a1.num_buses(555)
        expected = 12
        self.assertEqual(expected, actual)
                            

if __name__ == '__main__':
    unittest.main(exit=False)
