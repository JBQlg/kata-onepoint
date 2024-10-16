import unittest
from booking_system.flight_handler import Flight_handler
from booking_system.flight import Flight
from booking_system.seat import Seat


class TestFlightHandler(unittest.TestCase):
    
    def setUp(self):
        self.flight_handler = Flight_handler()
        
    def test_create_flight(self):
        """Flight creation test"""
        self.flight_handler.create_flight(plane_id="PL123", departure="Paris", destination="New York", schedule="10:00", date="2022-01-01", reservations=[])
        # Check if the flight has been created
        self.assertEqual(len(self.flight_handler.flights), 1)
        # Check if the flight has the right attributes
        self.assertEqual(len(self.flight_handler.flights), 1)
        self.assertEqual(self.flight_handler.flights[0].departure, "Paris")
        self.assertEqual(self.flight_handler.flights[0].arrival, "New York")
        self.assertEqual(self.flight_handler.flights[0].schedule, "10:00")
        self.assertEqual(self.flight_handler.flights[0].date, "2022-01-01")
        self.assertEqual(self.flight_handler.flights[0].plane_id, "PL123")
        self.assertEqual(self.flight_handler.flights[0].reservations, [])
        
    def delete_flight(self):
        """Flight delete test"""
        flight = self.flight_handler.create_flight(plane_id="PL123", departure="Paris", destination="New York", schedule="12:00", date="2024-05-01", reservations=[])
        self.flight_handler.delete_flight(flight.id)
        self.assertEqual(len(self.flight_handler.flights), 0)
                    
    def test_get_flight(self):
        """Test find flight by ID"""
        flight = self.flight_handler.create_flight(plane_id="PL123", departure="Paris", destination="New York", schedule="12:00", date="2024-05-01", reservations=[])
        found_flight = self.flight_handler.get_flight(flight.id)
        self.assertEqual(found_flight, flight)
        self.assertIsNone(self.flight_handler.get_flight("INVALID_ID"))