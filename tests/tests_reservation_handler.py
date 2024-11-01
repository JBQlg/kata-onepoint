import unittest
from unittest.mock import patch
from booking_system.reservation_handler import Reservation_handler
from booking_system.flight import Flight
from booking_system.passenger import Passenger
from booking_system.seat import Seat
from booking_system.plane import Plane
from booking_system.reservation import Reservation
class TestReservationHandler(unittest.TestCase):

    def setUp(self):
        self.reservation_handler = Reservation_handler()
        Plane._id_counter = 1
        Flight._id_counter = 1
        Reservation._id_counter = 1
        self.plane = Plane("Airbus A320", 10, 6)
        self.flight = Flight(departure="Paris", arrival="New York", date="2025-07-01", schedule="12:00", plane_id=self.plane.id)
        self.passenger = Passenger("123456789", "John", "Doe", 34)
        self.seat = Seat(row=0, col=0)
    
    @patch('builtins.input', side_effect=['FL1','1', '123456789', 'John', 'Doe', '34', 'A1']) # we need to mock inputs
    def test_create_reservation(self, mock_input):
        """Test reserveation creation """
        planes_list = [self.plane]
        flights_list = [self.flight]
        self.reservation_handler.create_reservation(flights_list, planes_list)
        # Vérifier que la réservation a été ajoutée au vol
        self.assertEqual(len(self.flight.reservations), 1)
        self.assertEqual(self.flight.reservations[0].passengers[0].passport_number, "123456789")
        self.assertEqual(self.flight.reservations[0].seats[0].row, 0)
        self.assertEqual(self.flight.reservations[0].seats[0].col, 0)
        # Vérifier que le siège a été assigné
        self.assertFalse(self.flight.is_seat_available(Seat(row=0, col=0),[self.plane]))

    @patch('builtins.input', side_effect=['y', 'RES1', 'y', '1' ,'123123123', 'Jane', 'Doe', '29'])
    def test_modify_reservation_modify_passenger(self, mock_input):
        """Test passenger modification"""
        flights_list = [self.flight]
        planes_list = [self.plane]
        
        flights_list = self.reservation_handler.modify_reservation("1", flights_list, planes_list)
        modified_passenger = self.flight.reservations[0].passengers[0]
        self.assertEqual(modified_passenger.firstname, 'Jane')
        self.assertEqual(modified_passenger.lastname, 'Doe')
        self.assertEqual(modified_passenger.age, '29')

    @patch('builtins.input', side_effect=['y', 'RES1', 'y', '2', 'B3'])
    @patch('booking_system.reservation_handler.Reservation_handler.fill_seat', return_value=Seat(row=1, col=2)) 
    def test_modify_reservation_modify_seat(self, mock_input, mock_fill_seat):
        """Test modification seat"""
        flights_list = [self.flight]
        planes_list = [self.plane]
        flights_list = self.reservation_handler.modify_reservation("2", flights_list, planes_list)
        modified_seat = self.flight.reservations[0].seats[0]
        self.assertEqual(modified_seat.row, 1)
        self.assertEqual(modified_seat.col, 2) 

    @patch('builtins.input', side_effect=['FL1', '2', '123456789', 'John', 'Doe', '34', 'B3', '987654321', 'Jane', 'Doe', '30', 'B4'])
    def test_create_reservation_multiple_passengers(self, mock_input):
        """Test creation of a reservation with multiple passengers."""
        planes_list = [self.plane]
        flights_list = [self.flight]
        self.reservation_handler.create_reservation(flights_list, planes_list)
        self.assertEqual(len(self.flight.reservations), 2)
        reservation = self.flight.reservations[1]
        self.assertEqual(len(reservation.passengers), 2)  
        self.assertEqual(len(reservation.seats), 2)  
        self.assertEqual(reservation.passengers[0].passport_number, "123456789")
        self.assertEqual(reservation.passengers[1].passport_number, "987654321")

    @patch('builtins.input', side_effect=['y', 'INVALID_ID', 'n'])
    def test_modify_reservation_invalid_id(self, mock_input):
        """Test modification with an invalid reservation ID."""
        flights_list = [self.flight]
        planes_list = [self.plane]
        with self.assertRaises(ValueError):
            self.reservation_handler.modify_reservation("1", flights_list, planes_list)
        
    @patch('builtins.input', side_effect=['y', 'RES1', 'y','123456789','Z99'])
    def test_modify_reservation_invalid_seat_format(self, mock_input):
        """Test modification seat with invalid format, with several passengers"""
        flights_list = [self.flight]
        planes_list = [self.plane]
        with self.assertRaises(ValueError):
            self.reservation_handler.modify_reservation("2", flights_list, planes_list)

    @patch('builtins.input', side_effect=['y', 'RES1', 'y', '3']) 
    def test_modify_reservation_cancel_reservation(self, mock_input):
        """Test cancel reservation"""
        flights_list = [self.flight]
        planes_list = [self.plane]

        flights_list = self.reservation_handler.modify_reservation("3", flights_list, planes_list)
        for f in flights_list:
            for r in f.reservations:
                print(r)
        self.assertEqual(self.flight.reservations[0].statut, "CANCELLED")
        #check all seats of the reservation are free
        for seat in self.flight.reservations[0].seats:
            self.assertFalse(seat.is_booked) 
