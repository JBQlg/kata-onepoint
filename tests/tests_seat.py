import unittest
from booking_system.seat import Seat
import booking_system.utils as ut

class TestSeat(unittest.TestCase):
    
    def setUp(self):
        self.seat1 = Seat(row=3, col=2, category="ECONOMY", is_booked=False) # seat C4
        self.seat2 = Seat(row=5, col=1, category="BUSINESS", is_booked=True) # seat B6
    
    def test_initialization(self):
        """Test if the Seat is initialized correctly."""
        self.assertEqual(self.seat1.row, 3)
        self.assertEqual(self.seat1.col, 2)
        self.assertEqual(self.seat1.category, "ECONOMY")
        self.assertFalse(self.seat1.is_booked)
        
        self.assertEqual(self.seat2.row, 5)
        self.assertEqual(self.seat2.col, 1)
        self.assertEqual(self.seat2.category, "BUSINESS")
        self.assertTrue(self.seat2.is_booked)
    
    def test_seat_status(self):
        """Test if the seat status"""
        self.assertFalse(self.seat1.is_booked)  # Initially not booked
        self.seat1.is_booked = True  # Change status to booked
        self.assertTrue(self.seat1.is_booked)   # Now it should be booked
    
    def test_str_representation(self):
        """Test the str method of the Seat"""
        # note col is 1 mean B
        # wanted format : "Seat : C4 (ECONONY) - AVAILABLE"
        self.assertEqual(str(self.seat1), "Seat : C4 (ECONOMY) - AVAILABLE")
        self.assertEqual(str(self.seat2), "Seat : B6 (BUSINESS) - BOOKED")
    
    def test_coordinates_conversion(self):
        """Tests the conversion coordinates to string"""
        expected_str_seat1 = ut.reverse_coordinates_converter(self.seat1.col, self.seat1.row)
        expected_str_seat2 = ut.reverse_coordinates_converter(self.seat2.col, self.seat2.row)
        
        # Ensure the utility function is called correctly
        self.assertEqual(expected_str_seat1, "C4")  # Assuming column is C and row is 3
        self.assertEqual(expected_str_seat2, "B6")  # Assuming column is B and row is 5
