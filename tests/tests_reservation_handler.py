import unittest
from unittest.mock import patch
from booking_system.reservation_handler import Reservation_handler
from booking_system.passenger import Passenger
from booking_system.flight import Flight
from booking_system.seat import Seat
from booking_system.plane import Plane

class TestReservationHandler(unittest.TestCase):

    def setUp(self):
        """Initialisation des instances nécessaires pour les tests."""
        self.reservation_handler = Reservation_handler()
        self.plane = Plane("Airbus A320", 10, 6)
        self.flight = Flight(departure="Paris", arrival="New York", date="2021-07-01", schedule="12:00", plane_id=self.plane.id)
    
    @patch('builtins.input', side_effect=['123456789', 'John', 'Doe', '34', 'A1'])  # Mock de plusieurs appels à input
    def test_create_reservation(self, mock_input):
        """Test de la création de réservation avec simulation d'entrées utilisateur."""
        planes_list = [self.plane]
        flights_list = [self.flight]
        
        # Exécuter la méthode create_reservation avec les entrées simulées
        self.reservation_handler.create_reservation(flights_list, planes_list)
        
        # Vérifier que la réservation a été ajoutée au vol
        self.assertEqual(len(self.flight.reservations), 1)
        self.assertEqual(self.flight.reservations[0].passengers[0].passport_number, "123456789")
        self.assertEqual(self.flight.reservations[0].seats[0].row, 0)
        self.assertEqual(self.flight.reservations[0].seats[0].col, 0)

    @patch('builtins.input', side_effect=['y', 'RES1'])  # Simuler un input pour rechercher la réservation
    def test_modify_reservation(self, mock_input):
        """Test de la modification de réservation avec simulation d'entrées utilisateur."""
        # Ajouter une réservation
        passenger = Passenger("123456789", "John", "Doe", 34)
        seat = Seat(row=0, col=0)
        reservation = self.reservation_handler.add_reservation([passenger], [seat], self.flight)
        
        # Tester la modification de la réservation
        flights_list = [self.flight]
        planes_list = [self.plane]
        
        # Simuler le choix de modifier la réservation
        with patch('builtins.input', side_effect=['1', '123456789', 'Jane', 'Doe', '35']):
            self.reservation_handler.modify_reservation("1", flights_list, planes_list)
        
        # Vérifier que le passager a bien été modifié
        self.assertEqual(reservation.passengers[0].firstname, 'Jane')
        self.assertEqual(reservation.passengers[0].age, 35)

if __name__ == "__main__":
    unittest.main()
