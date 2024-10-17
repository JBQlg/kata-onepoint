import unittest
from booking_system.flight_handler import Flight_handler
from booking_system.flight import Flight
from booking_system.seat import Seat
from booking_system.reservation import Reservation
from booking_system.plane import Plane

class TestFlightHandler(unittest.TestCase):
    
    def setUp(self):
        self.flight_handler = Flight_handler()
        
    def test_create_flight(self):
        """Flight creation test normal case"""
        self.flight_handler.create_flight(plane_id="PL123", departure="Paris", destination="New York", schedule="10:00", date="2025-01-01", reservations=[])
        # Check if the flight has been created
        self.assertEqual(len(self.flight_handler.flights), 1)
        # Check if the flight has the right attributes
        self.assertEqual(self.flight_handler.flights[0].departure, "Paris")
        self.assertEqual(self.flight_handler.flights[0].arrival, "New York")
        self.assertEqual(self.flight_handler.flights[0].schedule, "10:00")
        self.assertEqual(self.flight_handler.flights[0].date, "2025-01-01")
        self.assertEqual(self.flight_handler.flights[0].plane_id, "PL123")
        self.assertEqual(self.flight_handler.flights[0].reservations, [])
    
    def test_create_flight_invalid_date(self):
        """Test flight creation with invalid date"""
        with self.assertRaises(ValueError):
            self.flight_handler.create_flight(plane_id="PL123", departure="Paris", destination="New York", schedule="10:00", date="invalid-date", reservations=[])
    
    def test_delete_flight(self):
        """Flight delete test"""
        flight = self.flight_handler.create_flight(plane_id="PL123", departure="Paris", destination="New York", schedule="12:00", date="2025-05-01", reservations=[])
        self.flight_handler.delete_flight(flight.id)
        self.assertEqual(len(self.flight_handler.flights), 0)
        
        # Test deleting a flight that doesn't exist
        with self.assertRaises(ValueError):
            self.flight_handler.delete_flight("No flight with this id")
                    
    def test_get_flight(self):
        """Test find flight by ID"""
        flight = self.flight_handler.create_flight(plane_id="PL123", departure="Paris", destination="New York", schedule="12:00", date="2025-05-01", reservations=[])
        found_flight = self.flight_handler.get_flight(flight.id)
        self.assertEqual(found_flight, flight)
        self.assertIsNone(self.flight_handler.get_flight("INVALID_ID"))
    
    # def test_from_dict(self):
    #     """Test the from_dict method"""
    #     data = [
    #         {
    #             "id": "FL1",
    #             "departure": "Paris",
    #             "arrival": "New York",
    #             "date": "2025-05-01",
    #             "schedule": "12:00",
    #             "plane_id": "PL123",
    #             "reservations": []
    #         },
    #         {
    #             "id": "FL2",
    #             "departure": "Paris",
    #             "arrival": "New York",
    #             "date": "2025-05-01",
    #             "schedule": "16:00",
    #             "plane_id": "PL123",
    #             "reservations": []
    #         }
    #     ]
    #     handler = Flight_handler.from_dict(data)
    #     self.assertEqual(len(handler.flights), 2)
    #     self.assertEqual(handler.flights[0].id, "FL1")
    #     self.assertEqual(handler.flights[1].id, "FL2")
    #     self.assertEqual(handler.flights[0].departure, "Paris")
    #     self.assertEqual(handler.flights[1].departure, "Paris")
    #     self.assertEqual(handler.flights[0].arrival, "New York")
    #     self.assertEqual(handler.flights[1].arrival, "New York")
    #     self.assertEqual(handler.flights[0].date, "2025-05-01")
    #     self.assertEqual(handler.flights[1].date, "2025-05-01")
    #     self.assertEqual(handler.flights[0].schedule, "12:00")
    #     self.assertEqual(handler.flights[1].schedule, "16:00")
    #     self.assertEqual(handler.flights[0].plane_id, "PL123")
    #     self.assertEqual(handler.flights[1].plane_id, "PL123")
    #     self.assertEqual(handler.flights[0].reservations, [])
    #     self.assertEqual(handler.flights[1].reservations, [])
