import unittest
from booking_system.plane import Plane
from booking_system.plane_handler import Plane_handler

class TestPlaneHandler(unittest.TestCase):
    
    def setUp(self):
        self.plane_handler = Plane_handler()
    
    def test_create_plane(self):
        """Test the creation of a plane and check the planes list"""
        plane = self.plane_handler.create_plane(model="Boeing 747", row_nb=10, col_nb=6)
        self.assertEqual(len(self.plane_handler.planes), 1)
        self.assertEqual(self.plane_handler.planes[0].model, "Boeing 747")
        self.assertEqual(self.plane_handler.planes[0].row_nb, 10)
        self.assertEqual(self.plane_handler.planes[0].col_nb, 6)
        

    def test_create_plane_invalid_values(self):
        """Test creating a plane with invalid values."""
        with self.assertRaises(ValueError):
            self.plane_handler.create_plane(model="", row_nb=10, col_nb=6) 
        with self.assertRaises(ValueError):
            self.plane_handler.create_plane(model="Boeing 747", row_nb=-5, col_nb=6) 
        with self.assertRaises(ValueError):
            self.plane_handler.create_plane(model="Boeing 747", row_nb=10, col_nb=-3)  

    def test_delete_plane(self):
        """Test deleting a plane"""
        plane = self.plane_handler.create_plane(model="Boeing 747", row_nb=10, col_nb=6)
        self.plane_handler.delete_plane(plane.id)
        self.assertEqual(len(self.plane_handler.planes), 0)
        self.assertIsNone(self.plane_handler.get_plane(plane.id))

    def test_delete_non_existing_plane(self):
        """Test deleting a non-existing plane"""
        with self.assertRaises(ValueError):
            self.plane_handler.delete_plane("INVALID_ID")
    
    def test_get_plane(self):
        """Test retrieving a specific plane by ID."""
        plane = self.plane_handler.create_plane(model="Boeing 747", row_nb=10, col_nb=6)
        found_plane = self.plane_handler.get_plane(plane.id)
        self.assertEqual(found_plane, plane)
        # Test for non-existing plane
        self.assertIsNone(self.plane_handler.get_plane("INVALID_ID"))

