# import unittest
# from unittest.mock import patch
# from booking_system.reservation_handler import Reservation_handler
# from booking_system.flight import Flight
# from booking_system.passenger import Passenger
# from booking_system.seat import Seat
# from booking_system.plane import Plane
# from booking_system.reservation import Reservation
# class TestReservationHandler(unittest.TestCase):

#     def setUp(self):
#         self.reservation_handler = Reservation_handler()
#         Plane._id_counter = 1
#         Flight._id_counter = 1
#         # Reservation._id_counter = 1
#         self.plane = Plane("Airbus A320", 10, 6)
#         self.flight = Flight(departure="Paris", arrival="New York", date="2021-07-01", schedule="12:00", plane_id=self.plane.id)
#         self.passenger = Passenger("123456789", "John", "Doe", 34)
#         self.seat = Seat(row=0, col=0)
    
#     @patch('builtins.input', side_effect=['FL1','1', '123456789', 'y', 'John', 'Doe', '34', 'A1']) # we need to mock inputs
#     def test_create_reservation(self, mock_input):
#         """Test reserveation creation """
#         planes_list = [self.plane]
#         flights_list = [self.flight]
#         self.reservation_handler.create_reservation(flights_list, planes_list)
#         # Vérifier que la réservation a été ajoutée au vol
#         self.assertEqual(len(self.flight.reservations), 1)
#         self.assertEqual(self.flight.reservations[0].passengers[0].passport_number, "123456789")
#         self.assertEqual(self.flight.reservations[0].seats[0].row, 0)
#         self.assertEqual(self.flight.reservations[0].seats[0].col, 0)
#         # Vérifier que le siège a été assigné
#         self.assertFalse(self.flight.is_seat_available(Seat(row=0, col=0)))

#     # @patch('builtins.input', side_effect=['y', 'RES1', '1', 'Jane', 'Doe', '29'])  # Modifier passager 2
#     # def test_modify_reservation_modify_passenger(self, mock_input):
#     #     """Test de la modification d'un passager"""
#     #     flights_list = [self.flight]
#     #     planes_list = [self.plane]
#     #     print("resa")
#     #     for f in flights_list:
#     #         for r in f.reservations:
#     #             print(r)
        
#     #     # Modifier le deuxième passager (Jane Smith devient Jane Doe, 29 ans)
#     #     self.reservation_handler.modify_reservation("1", flights_list, planes_list)

#     #     # Vérifier que le passager a bien été modifié
#     #     modified_passenger = self.flight.reservations[0].passengers[1]
#     #     self.assertEqual(modified_passenger.firstname, 'Jane')
#     #     self.assertEqual(modified_passenger.lastname, 'Doe')
#     #     self.assertEqual(modified_passenger.age, 29)

# #     @patch('builtins.input', side_effect=['y', '123456789'])  # Mock input pour annuler la réservation
# #     def test_cancel_reservation(self, mock_input):
# #         """Test de l'annulation d'une réservation."""
# #         # Ajouter une réservation
# #         reservation = self.reservation_handler.add_reservation([self.passenger], [self.seat], self.flight)
        
# #         # Simuler l'annulation de la réservation
# #         self.reservation_handler.concel_reservation(reservation)
        
# #         # Vérifier que la réservation est bien annulée
# #         self.assertEqual(reservation.statut, "CANCELLED")
# #         for seat in reservation.seats:
# #             self.assertFalse(seat.is_booked)

# #     @patch('builtins.input', side_effect=['123456789', 'John', 'Doe', '34', 'A1'])  # Mock de l'input pour assigner un siège
# #     def test_assign_seat(self, mock_input):
# #         """Test d'assignation d'un siège avec des entrées simulées."""
# #         planes_list = [self.plane]
# #         flights_list = [self.flight]
        
# #         # Créer une réservation avec un siège
# #         self.reservation_handler.assign_seat(self.flight, self.passenger, "A1", planes_list)
        
# #         # Vérifier que le siège a bien été assigné
# #         self.assertTrue(self.flight.is_seat_available(Seat(row=0, col=0)) == False)  # Le siège A1 est occupé

# #     # @patch('builtins.input', side_effect=['y', 'RES1'])  # Simuler l'input pour afficher les détails de la réservation
# #     # def test_print_reservation_details(self, mock_input):
# #     #     """Test de l'affichage des détails d'une réservation."""
# #     #     # Ajouter une réservation
# #     #     reservation = self.reservation_handler.add_reservation([self.passenger], [self.seat], self.flight)
        
# #     #     # Capturer l'affichage des détails de la réservation
# #     #     with patch('builtins.print') as mock_print:
# #     #         self.reservation_handler.print_reservation_details([self.flight])
# #     #         mock_print.assert_any_call(f"Reservation details : ")
# #     #         mock_print.assert_any_call(reservation)

# # if __name__ == "__main__":
# #     unittest.main()
