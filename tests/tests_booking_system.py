import unittest
from unittest.mock import patch, MagicMock
from bookingSystem import BookingSystem
from booking_system.flight_handler import Flight_handler
from booking_system.plane_handler import Plane_handler
from booking_system.reservation_handler import Reservation_handler

class TestBookingSystem(unittest.TestCase):

    def setUp(self):
        """Setup the BookingSystem instance for tests."""
        self.system = BookingSystem()
        self.system.flight_handler = Flight_handler()
        self.system.plane_handler = Plane_handler()
        self.system.reservation_handler = Reservation_handler()

    # @patch('builtins.input', side_effect=['1', 'FL123', '1', '123123123', 'John', 'Doe', '30', 'A1'])
    # def test_create_reservation(self, mock_input):
    #     """Test the process of creating a reservation."""
    #     # Mock the plane and flight lists
    #     self.system.flight_handler.flights = [MagicMock(id='FL1')]
    #     self.system.plane_handler.planes = [MagicMock(id='P1')]
        
    #     # Call the main menu to create a reservation
    #     self.system.main_menu_handler()

    #     # Check if the reservation was added to the flight
    #     flight = self.system.flight_handler.flights[0]
    #     self.assertEqual(len(flight.reservations), 1)
    #     reservation = flight.reservations[0]
    #     self.assertEqual(reservation.passengers[0].firstname, "John")
    #     self.assertEqual(reservation.seats[0].row, 0)  # A1 corresponds to row 0

    # @patch('builtins.input', side_effect=['6', 'Boeing 737', '12', '6', '5'])
    # def test_create_plane(self, mock_input):
    #     """Test adding a new plane."""
    #     # Call the main menu to create a plane
    #     self.system.main_menu_handler()
        
    #     # Check if the plane was added to the plane handler
    #     self.assertEqual(len(self.system.plane_handler.planes), 1)
    #     plane = self.system.plane_handler.planes[0]
    #     self.assertEqual(plane.model, "Boeing 737")
    #     self.assertEqual(plane.row_nb, 12)
    #     self.assertEqual(plane.col_nb, 6)

    # @patch('builtins.input', side_effect=['7', 'FL123', 'Paris', 'New York', '12:00', '2024-05-01', '5'])
    # def test_create_flight(self, mock_input):
    #     """Test adding a new flight."""
    #     # Mock the available planes
    #     self.system.plane_handler.planes = [MagicMock(id='P1', model='Boeing 737')]
        
    #     # Call the main menu to create a flight
    #     self.system.main_menu_handler()
        
    #     # Check if the flight was added to the flight handler
    #     self.assertEqual(len(self.system.flight_handler.flights), 1)
    #     flight = self.system.flight_handler.flights[0]
    #     self.assertEqual(flight.departure, 'Paris')
    #     self.assertEqual(flight.arrival, 'New York')
    #     self.assertEqual(flight.schedule, '12:00')
    #     self.assertEqual(flight.date, '2024-05-01')
    #     self.assertEqual(flight.plane_id, 'P1')

    # @patch('builtins.input', side_effect=['9', 'P1', '5'])
    # def test_delete_plane(self, mock_input):
    #     """Test deleting a plane."""
    #     # Mock the plane to delete
    #     self.system.plane_handler.planes = [MagicMock(id='P1')]
        
    #     # Call the main menu to delete the plane
    #     self.system.main_menu_handler()

    #     # Check if the plane was deleted
    #     self.assertEqual(len(self.system.plane_handler.planes), 0)

    # @patch('builtins.input', side_effect=['10', 'FL123', '5'])
    # def test_delete_flight(self, mock_input):
    #     """Test deleting a flight."""
    #     # Mock the flight to delete
    #     self.system.flight_handler.flights = [MagicMock(id='FL123')]
        
    #     # Call the main menu to delete the flight
    #     self.system.main_menu_handler()

    #     # Check if the flight was deleted
    #     self.assertEqual(len(self.system.flight_handler.flights), 0)

    # def test_show_help(self):
    #     """Test showing the help documentation."""
    #     with patch('builtins.print') as mock_print:
    #         self.system.show_help()
    #         mock_print.assert_called()  # Ensure print was called


