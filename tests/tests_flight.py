import unittest
from booking_system.flight import Flight
from booking_system.seat import Seat
from booking_system.reservation import Reservation
from booking_system.plane import Plane
from booking_system.passenger import Passenger

class TestFlight(unittest.TestCase):
    
    def setUp(self):
        """Create a flight for the tests (with reservations and seats)"""
        self.flight = Flight(plane_id="PL123", departure="Paris", arrival="New York", date="2024-05-01", schedule="12:00", reservations=[])
        self.seat1 = Seat(row=1, col=2)
        self.seat2 = Seat(row=1, col=3)
        self.passenger = Passenger("123456789", "John", "Doe", 34)
        self.seat1.is_booked = True
        self.flight.reservations = [
            Reservation("FL1", passengers=[self.passenger], seats=[self.seat1]),
        ]
        
    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.flight), "Flight FL1 : Paris to New York (10:00) on plane PL123")
        
    def test_is_seat_available(self):
        """Test the is_seat_available method"""
        self.assertTrue(self.flight.is_seat_available(Seat(row=1, col="A")))
        self.flight.reservations.append(Reservation(seats=[Seat(row=1, col="A")]))
        self.assertFalse(self.flight.is_seat_available(Seat(row=1, col="A")))
        
    def test_display_plane_plan(self):
        """Test the display_plane_plan method"""
        self.assertEqual(self.flight.display_plane_plan([Plane(id="PL123", row_nb=2, col_nb=2)]), "      A  B \n 1   O  O \n 2   O  O \n")
        self.assertEqual(self.flight.display_plane_plan([Plane(id="PL123", row_nb=2, col_nb=3)]), "      A  B  C \n 1   O  O  O \n 2   O  O  O \n")