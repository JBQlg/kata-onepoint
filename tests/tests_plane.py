import unittest
from booking_system.plane import Plane

class TestPlane(unittest.TestCase):
    
    def setUp(self):
        Plane._id_counter = 1 # reset the counter
        self.plane = Plane(model="Boeing 747", row_nb=10, col_nb=6)
    
    def test_initialization(self):
        """Test if the Plane is initialized correctly."""
        self.assertEqual(self.plane.model, "Boeing 747")
        self.assertEqual(self.plane.row_nb, 10)
        self.assertEqual(self.plane.col_nb, 6)
        self.assertTrue(self.plane.id.startswith("P"))
    
    def test_initialization_invalid_values(self):
        """Test init with invalid values."""
        with self.assertRaises(ValueError): 
            Plane(model="Boeing 747", row_nb=-1, col_nb=6) 
        with self.assertRaises(ValueError):
            Plane(model="Boeing 747", row_nb=10, col_nb=-3)
        with self.assertRaises(ValueError):
            Plane(model="", row_nb=10, col_nb=6)  
    
    def test_id_counter(self):
        """Test if the ID counter works correctly for multiple planes."""
        plane2 = Plane(model="Airbus A320", row_nb=8, col_nb=4)
        self.assertNotEqual(self.plane.id, plane2.id)
        self.assertTrue(plane2.id.startswith("P"))
        self.assertEqual(plane2.id, "P2")
    
    def test_str(self):
        """Test the string function of the Plane."""
        print("Plane 1 ID : ", self.plane.id)
        self.assertEqual(str(self.plane), "Plane P1 : Boeing 747 (10 x 6)")

