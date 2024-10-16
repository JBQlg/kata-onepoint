import unittest
from booking_system.plane import Plane
from booking_system.plane_handler import Plane_handler

class TestPlaneHandler(unittest.TestCase):
    
    def setUp(self):
        """Set up a PlaneHandler instance before each test."""
        self.plane_handler = Plane_handler()
    
    def test_create_plane(self):
        """Test the creation of a plane."""
        plane = self.plane_handler.create_plane(model="Boeing 747", row_nb=10, col_nb=6)
        self.assertEqual(len(self.plane_handler.planes), 1)
        self.assertEqual(self.plane_handler.planes[0].model, "Boeing 747")
        self.assertEqual(self.plane_handler.planes[0].row_nb, 10)
        self.assertEqual(self.plane_handler.planes[0].col_nb, 6)
    
    def test_get_planes(self):
        """Test the retrieval of all planes."""
        plane1 = self.plane_handler.create_plane(model="Boeing 747", row_nb=10, col_nb=6)
        plane2 = self.plane_handler.create_plane(model="Airbus A320", row_nb=8, col_nb=4)
        planes = self.plane_handler.get_planes()
        self.assertEqual(len(planes), 2)
        self.assertIn(plane1, planes)
        self.assertIn(plane2, planes)

    def test_get_plane(self):
        """Test retrieving a specific plane by ID."""
        plane = self.plane_handler.create_plane(model="Boeing 747", row_nb=10, col_nb=6)
        found_plane = self.plane_handler.get_plane(plane.id)
        self.assertEqual(found_plane, plane)
        
        # Test for non-existing plane
        self.assertIsNone(self.plane_handler.get_plane("INVALID_ID"))

