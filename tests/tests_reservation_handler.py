import unittest
from booking_system.reservation_handler import Reservation_handler
from booking_system.flight import Flight
from booking_system.plane import Plane
from booking_system.passenger import Passenger
from booking_system.seat import Seat

class TestReservationHandler(unittest.TestCase):
    
    def setUp(self):
        """Set up instances for testing Reservation_handler."""
        self.handler = Reservation_handler()
        self.plane = Plane(model="Boeing 747", row_nb=10, col_nb=6)
        self.flight = Flight(departure="Paris", arrival="New York", date="2023-10-05", schedule="14:00", plane_id=self.plane.id)
        self.passenger1 = Passenger(passport_number="A12345678", firstname="John", lastname="Doe", age=30)
        self.passenger2 = Passenger(passport_number="A87654321", firstname="Jane", lastname="Doe", age=28)
        self.seat1 = Seat(row=3, col=2, category="ECONOMY", is_booked=False)
        self.seat2 = Seat(row=4, col=3, category="ECONOMY", is_booked=False)

        # Set up a list of flights and planes for testing
        self.flights_list = [self.flight]
        self.planes_list = {self.plane.id: self.plane}
    
    def test_create_reservation(self):
        """Test if a reservation is created and confirmed successfully."""
        self.handler.create_reservation(flights_list=self.flights_list, planes_list=self.planes_list)
        self.assertEqual(len(self.flight.reservations), 1)
        self.assertEqual(self.flight.reservations[0].statut, "CONFIRMED")
    
    def test_add_reservation(self):
        """Test adding a reservation to a flight."""
        reservation = self.handler.add_reservation([self.passenger1], [self.seat1], self.flight)
        self.assertEqual(len(reservation.reservations), 1)
        self.assertEqual(reservation.reservations[0].statut, "CONFIRMED")
        self.assertTrue(self.seat1.is_booked)
    
    def test_build_passenger(self):
        """Test the building of a passenger."""
        passenger = self.handler.build_passenger("A98765432", "Jane", "Smith", 35)
        self.assertEqual(passenger.firstname, "Jane")
        self.assertEqual(passenger.lastname, "Smith")
        self.assertEqual(passenger.age, 35)
    
    def test_assign_seat_valid(self):
        """Test seat assignment with a valid seat."""
        seat = self.handler.assign_seat(self.flight, self.passenger1, "C4", self.planes_list)
        self.assertIsNotNone(seat)

    def test_assign_seat_invalid_format(self):
        """Test seat assignment with an invalid seat format."""
        with self.assertRaises(ValueError):
            self.handler.assign_seat(self.flight, self.passenger1, "XYZ", self.planes_list)

    def test_assign_seat_out_of_range(self):
        """Test seat assignment with a seat that doesn't exist in the plane."""
        with self.assertRaises(ValueError):
            self.handler.assign_seat(self.flight, self.passenger1, "H12", self.planes_list)

    def test_modify_reservation_passenger(self):
        """Test modifying a passenger in a reservation."""
        reservation = self.handler.add_reservation([self.passenger1], [self.seat1], self.flight)
        updated_resa = self.handler.modify_reservation_passenger(reservation, "A12345678")
        self.assertNotEqual(updated_resa.passengers[0].firstname, "John")  # The passenger should be replaced

    def test_modify_reservation_seat(self):
        """Test modifying a seat in a reservation."""
        reservation = self.handler.add_reservation([self.passenger1], [self.seat1], self.flight)
        updated_resa = self.handler.modify_reservation_seat(self.flight, reservation, self.planes_list)
        self.assertNotEqual(updated_resa.seats[0], self.seat1)  # The seat should be changed
    
    def test_cancel_reservation(self):
        """Test cancelling a reservation."""
        reservation = self.handler.add_reservation([self.passenger1], [self.seat1], self.flight)
        cancelled_resa = self.handler.concel_reservation(reservation)
        self.assertEqual(cancelled_resa.statut, "CANCELLED")
        self.assertFalse(self.seat1.is_booked)

    def test_get_reservation_by_passport(self):
        """Test retrieving a reservation by passenger's passport number."""
        reservation = self.handler.add_reservation([self.passenger1], [self.seat1], self.flight)
        found_reservation = self.handler.get_reservations_by_passport(self.flights_list, "A12345678")
        self.assertEqual(found_reservation.id, reservation.id)

    def test_get_reservation_by_id_resa(self):
        """Test retrieving a reservation by ID."""
        reservation = self.handler.add_reservation([self.passenger1], [self.seat1], self.flight)
        found_reservation = self.handler.get_reservation_by_id_resa(self.flights_list, reservation.id)
        self.assertEqual(found_reservation.id, reservation.id)
    
    def test_invalid_reservation_modification(self):
        """Test handling invalid modification choice."""
        with self.assertRaises(ValueError):
            self.handler.modify_reservation("5", self.flights_list, self.planes_list)  # Invalid choice for modification


if __name__ == '__main__':
    unittest.main()
