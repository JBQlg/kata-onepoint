import unittest
from unittest.mock import patch, mock_open, MagicMock
from bookingSystem import BookingSystem
from booking_system.plane_handler import Plane_handler
from booking_system.flight_handler import Flight_handler
from booking_system.reservation_handler import Reservation_handler
import json


class TestBookingSystem(unittest.TestCase):
    # mock open to open and test the file
    @patch("builtins.open", new_callable=mock_open, read_data='{"planes": [], "flights": []}')
    def test_initialization(self, mock_file):
        """Test initialization and data loading from JSONfile."""
        system = BookingSystem()
        # Check if the handlers init
        self.assertIsInstance(system.flight_handler, Flight_handler)
        self.assertIsInstance(system.plane_handler, Plane_handler)
        self.assertIsInstance(system.reservation_handler, Reservation_handler)
        mock_file.assert_called_once_with(BookingSystem.DATA_FILE, 'r')

    # @patch('json.dump')
    # @patch('builtins.open', new_callable=mock_open)
    # def test_save_data(self, mock_file, mock_json_dump):
    #     """Test saving data to the JSON file."""
    #     system = BookingSystem()
    #     system.plane_handler.create_plane("Boeing 747", 10, 6)
    #     system.flight_handler.create_flight(plane_id="P1", departure="Paris", destination="New York", schedule="12:00", date="2025-01-01", reservations=[])
    #     system.save_data()
    #     #file should be open in write mode and data is saved
    #     mock_file.assert_called_once_with(system.DATA_FILE, 'w')
        # mock_json_dump.assert_called_once()
