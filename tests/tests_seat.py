import unittest
from booking_system.seat import Seat
import booking_system.utils as ut

class TestSeat(unittest.TestCase):
    
    def setUp(self):
        self.seat1 = Seat(row=3, col=2, category="ECONOMY", is_booked=False)
        self.seat2 = Seat(row=5, col=1, category="BUSINESS", is_booked=True)
    
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
        """Test if the seat status (booked or available) is correctly handled."""
        self.assertFalse(self.seat1.is_booked)  # Initially not booked
        self.seat1.is_booked = True  # Change status to booked
        self.assertTrue(self.seat1.is_booked)   # Now it should be booked
    
    def test_str_representation(self):
        """Test the string representation of the Seat."""
        self.assertEqual(str(self.seat1), "Seat : C3 (ECONOMY) - AVAILABLE")
        self.assertEqual(str(self.seat2), "Seat : B5 (BUSINESS) - BOOKED")
    
    def test_coordinates_conversion(self):
        """Test the seat's reverse coordinates converter from the utils module."""
        expected_str_seat1 = ut.reverse_coordinates_converter(self.seat1.col, self.seat1.row)
        expected_str_seat2 = ut.reverse_coordinates_converter(self.seat2.col, self.seat2.row)
        
        # Ensure the utility function is called correctly
        self.assertEqual(expected_str_seat1, "C3")  # Assuming column is C and row is 3
        self.assertEqual(expected_str_seat2, "B5")  # Assuming column is B and row is 5
