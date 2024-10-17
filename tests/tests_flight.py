import unittest
from booking_system.flight import Flight
from booking_system.seat import Seat
from booking_system.reservation import Reservation
from booking_system.plane import Plane
from booking_system.passenger import Passenger

class TestFlight(unittest.TestCase):
    
    def setUp(self):
        """Create a flight for the tests (with reservations and seats)"""
        Flight._id_counter = 1
        Plane._id_counter = 1
        self.plane = Plane("Airbus A320", 10, 6)
        self.plane2 = Plane("Airbus A320", 10, 6)
        self.flight = Flight(plane_id="P1", departure="Paris", arrival="New York", date="2025-05-01", schedule="12:00", reservations=[])
        self.flight2 = Flight(plane_id="P2", departure="Paris", arrival="New York", date="2025-05-01", schedule="16:00", reservations=[])
        self.seat1 = Seat(row=1, col=2)
        self.seat2 = Seat(row=1, col=3)
        self.passenger = Passenger("123456789", "John", "Doe", 34)
        self.seat1.is_booked = True
        self.flight.reservations = [
            Reservation("FL1", passengers=[self.passenger], seats=[self.seat1]),
        ]
        
    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.flight), "Flight FL1 : Paris to New York (2025-05-01 - 12:00) on plane P1")
        
    def test_is_seat_available(self):
        """Test the is_seat_available method"""
        self.assertTrue(self.flight.is_seat_available(Seat(row=1, col=0), [self.plane, self.plane2])) #A2
        self.flight.reservations.append(Reservation("FL1",passengers= [Passenger("123456789", "John", "Doe", 34)], seats=[Seat(row=1, col=0)]))
        self.seat1.is_booked = True#C2
        self.assertFalse(self.flight.is_seat_available(Seat(row=1, col=2), [self.plane, self.plane2] )) # seat 1 already booked
        
    def test_display_plane_plan(self):
        """Test the display_plane_plan method"""
        # taking into account the reservation made before 
        self.assertEqual(self.flight.display_plane_plan([self.plane, self.plane2]), "       A  B  C  |  D  E  F \n 1     0  0  0  |  0  0  0 \n 2     0  0  X  |  0  0  0 \n 3     0  0  0  |  0  0  0 \n 4     0  0  0  |  0  0  0 \n 5     0  0  0  |  0  0  0 \n 6     0  0  0  |  0  0  0 \n 7     0  0  0  |  0  0  0 \n 8     0  0  0  |  0  0  0 \n 9     0  0  0  |  0  0  0 \n10     0  0  0  |  0  0  0 \n")
        # no reservation made
        self.assertEqual(self.flight2.display_plane_plan([self.plane, self.plane2]), "       A  B  C  |  D  E  F \n 1     0  0  0  |  0  0  0 \n 2     0  0  0  |  0  0  0 \n 3     0  0  0  |  0  0  0 \n 4     0  0  0  |  0  0  0 \n 5     0  0  0  |  0  0  0 \n 6     0  0  0  |  0  0  0 \n 7     0  0  0  |  0  0  0 \n 8     0  0  0  |  0  0  0 \n 9     0  0  0  |  0  0  0 \n10     0  0  0  |  0  0  0 \n")
        
    def test_is_seat_out_of_bounds(self):
        """Test is_seat_available for a seat out of lpane bounds"""
        self.assertFalse(self.flight.is_seat_available(Seat(row=15, col=2), [self.plane, self.plane2]))  # Invalid row
        self.assertFalse(self.flight.is_seat_available(Seat(row=2, col=10), [self.plane, self.plane2]))  # Invalid column
    
    def test_create_flight_with_invalid_data(self):
        """test creating a flight with invalid data"""
        # should raise a ValueError
        with self.assertRaises(ValueError):
            Flight(plane_id=None, departure="Paris", arrival="New York", date="2025-05-01", schedule="12:00", reservations=[])
        with self.assertRaises(ValueError):
            Flight(plane_id="P1", departure="", arrival="New York", date="2025-05-01", schedule="12:00", reservations=[])
        with self.assertRaises(ValueError):
            Flight(plane_id="P1", departure="Paris", arrival="New York", date="invalid-date", schedule="12:00", reservations=[])

    def test_multiple_reservations(self):
        """Test multiple reservations on the same flight"""
        seat2 = Seat(row=1, col=3)
        passenger2 = Passenger("987654321", "Jane", "Doe", 29)
        self.flight.reservations.append(Reservation("FL1", passengers=[passenger2], seats=[seat2]))
        # seat 2 should be already booked
        self.assertFalse(self.flight.is_seat_available(seat2, [self.plane, self.plane2])) 
