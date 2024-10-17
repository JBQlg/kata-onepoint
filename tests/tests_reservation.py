import unittest
from booking_system.reservation import Reservation
from booking_system.passenger import Passenger
from booking_system.seat import Seat

class TestReservation(unittest.TestCase):
    
    def setUp(self):
        Reservation._id_counter = 1 # reset the counter
        self.passenger1 = Passenger(passport_number="A12345678", firstname="John", lastname="Doe", age=30)
        self.passenger2 = Passenger(passport_number="A87654321", firstname="Jane", lastname="Doe", age=28)
        
        self.seat1 = Seat(row=3, col=2, category="ECONOMY", is_booked=False)
        self.seat2 = Seat(row=4, col=3, category="ECONOMY", is_booked=False)
        
        self.reservation = Reservation(
            flight_id="FL123",
            passengers=[self.passenger1, self.passenger2],
            seats=[self.seat1, self.seat2]
        )
    
    def test_initialization(self):
        """Test if the Reservation is initialized correctly.
        """
        self.assertEqual(self.reservation.flight_id, "FL123")
        self.assertEqual(len(self.reservation.passengers), 2)
        self.assertEqual(len(self.reservation.seats), 2)
        self.assertEqual(self.reservation.statut, "PENDING")
        self.assertTrue(self.reservation.id.startswith("RES"))
    
    def test_str(self):
        """Test the string funtion."""
        expected_str = (
            f"Reservation {self.reservation.id} pour le vol FL123 :\n"
            f"Passager: {self.passenger1} - Siège: {self.seat1} - Statut: PENDING\n"
            f"Passager: {self.passenger2} - Siège: {self.seat2} - Statut: PENDING\n"
        )
        self.assertEqual(str(self.reservation), expected_str)
    
    def test_confirm_reservation(self):
        """Test if the reservation can be confirmed and seats are booked."""
        self.reservation.confirm()
        self.assertEqual(self.reservation.statut, "CONFIRMED")
        for seat in self.reservation.seats:
            self.assertTrue(seat.is_booked)
    
    def test_cancel_reservation(self):
        """Test if the reservation can be cancelled and seats are released."""
        # First confirm the reservation, then cancel it
        self.reservation.confirm()
        self.reservation.cancel()
        
        self.assertEqual(self.reservation.statut, "CANCELLED")
        for seat in self.reservation.seats:
            self.assertFalse(seat.is_booked)

